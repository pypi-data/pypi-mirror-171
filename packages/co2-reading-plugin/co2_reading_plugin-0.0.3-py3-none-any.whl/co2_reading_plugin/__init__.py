# -*- coding: utf-8 -*-
from __future__ import annotations

import board
import click
from pioreactor.background_jobs.base import BackgroundJob
from pioreactor.background_jobs.leader.mqtt_to_db_streaming import produce_metadata
from pioreactor.background_jobs.leader.mqtt_to_db_streaming import register_source_to_sink
from pioreactor.background_jobs.leader.mqtt_to_db_streaming import TopicToParserToTable
from pioreactor.config import config
from pioreactor.utils import timing
from pioreactor.whoami import get_latest_experiment_name
from pioreactor.whoami import get_unit_name


def parser(topic, payload) -> dict:
    metadata = produce_metadata(topic)
    return {
        "experiment": metadata.experiment,
        "pioreactor_unit": metadata.pioreactor_unit,
        "timestamp": timing.current_utc_timestamp(),
        "co2_reading_ppm": float(payload),
    }


register_source_to_sink(
    TopicToParserToTable(
        "pioreactor/+/+/scd_reading/co2",
        parser,
        "co2_readings",
    )
)


class SCDReading(BackgroundJob):

    job_name = "scd_reading"

    published_settings = {
        "minutes_between_checks": {"datatype": "float", "unit": "min", "settable": True},
        "co2": {"datatype": "float", "unit": "ppm", "settable": False},
        "temperature": {"datatype": "float", "unit": "°C", "settable": False},
        "relative_humidity": {"datatype": "float", "unit": "%rH", "settable": False},
    }

    def __init__(  # config stuff, settable in activities
        self,
        unit,
        experiment,
        minutes_between_checks: float,
        skip_co2: bool = False,
        skip_temperature: bool = False,
        skip_relative_humidity: bool = False,
    ):
        super().__init__(unit=unit, experiment=experiment)

        self.minutes_between_checks = minutes_between_checks
        self.skip_co2 = skip_co2
        self.skip_temperature = skip_temperature
        self.skip_relative_humidity = skip_relative_humidity

        i2c = board.I2C()

        if config.get("scd_config", "adafruit_sensor_type") == "scd30":
            from adafruit_scd30 import SCD30

            self.scd = SCD30(i2c)
        elif config.get("scd_config", "adafruit_sensor_type") == "scd4x":
            from adafruit_scd4x import SCD4X

            self.scd = SCD4X(i2c)
            self.scd.start_periodic_measurement()
        else:
            self.logger.error(
                "'adafruit_sensor_type' in [scd_config] not found. Did you mean one of 'scd30' or 'scd4x'?"
            )
            raise ValueError(
                "'adafruit_sensor_type' in [scd_config] not found. Did you mean one of 'scd30' or 'scd4x'?"
            )

        self.record_scd_timer = timing.RepeatedTimer(
            self.minutes_between_checks * 60, self.record_scd, run_immediately=True
        )

        self.record_scd_timer.start()

    def set_minutes_between_checks(self, new_minutes_between_checks):
        self.record_scd_timer.interval = new_minutes_between_checks * 60
        self.minutes_between_checks = new_minutes_between_checks

    def on_sleeping(self):
        # user pauses
        self.record_scd_timer.pause()

    def on_sleeping_to_ready(self):
        self.record_scd_timer.unpause()

    def on_disconnect(self):
        self.record_scd_timer.cancel()

    def record_co2(self):
        self.co2 = self.scd.CO2

    def record_temperature(self):
        self.temperature = self.scd.temperature

    def record_relative_humidity(self):
        self.relative_humidity = self.scd.relative_humidity

    def record_scd(self):
        # determines which scd to record
        if not self.skip_co2:
            self.record_co2()
        if not self.skip_temperature:
            self.record_temperature()
        if not self.skip_relative_humidity:
            self.record_relative_humidity()


@click.command(name="scd_reading")
@click.option(
    "--minutes-between-checks",
    default=config.getfloat("scd_config", "minutes_between_checks"),
    show_default=True,
)
def click_scd_reading(minutes_between_checks):
    """
    Start reading CO2, temperature, and humidity from the scd sensor.
    """
    job = SCDReading(
        minutes_between_checks=minutes_between_checks,
        unit=get_unit_name(),
        experiment=get_latest_experiment_name(),
    )
    job.block_until_disconnected()


@click.command(name="co2_reading")
@click.option(
    "--minutes-between-checks",
    default=config.getfloat("scd_config", "minutes_between_checks"),
    show_default=True,
)
def click_co2_reading(minutes_between_checks):
    """
    Only returns CO2 readings.
    """
    job = SCDReading(
        minutes_between_checks=minutes_between_checks,
        unit=get_unit_name(),
        experiment=get_latest_experiment_name(),
        skip_temperature=True,
        skip_relative_humidity=True,
    )
    job.block_until_disconnected()
