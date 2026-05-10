import json
import random
import time
from datetime import datetime, timezone

import paho.mqtt.client as mqtt


BROKER_HOST = "localhost"
BROKER_PORT = 1883

DEVICE_ID = "GM-HYDROLOGIC-01"
LOCATION = "main-building"

TOPIC = "hydroficient/grandmarina/sensors/main-building/readings"


class WaterSensorMQTT:
    def __init__(self, device_id, location):
        self.device_id = device_id
        self.location = location
        self.counter = 0

    def generate_reading(self):
        self.counter += 1

        pressure_upstream = round(random.uniform(80.0, 84.0), 1)
        pressure_downstream = round(random.uniform(75.0, 78.5), 1)
        flow_rate = round(random.uniform(38.0, 43.0), 1)

        pressure_differential = round(pressure_upstream - pressure_downstream, 1)

        return {
            "device_id": self.device_id,
            "location": self.location,
            "counter": self.counter,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "pressure": {
                "upstream_psi": pressure_upstream,
                "downstream_psi": pressure_downstream,
                "differential_psi": pressure_differential
            },
            "flow": {
                "rate_gpm": flow_rate
            }
        }


def main():
    sensor = WaterSensorMQTT(DEVICE_ID, LOCATION)

    client = mqtt.Client()
    client.connect(BROKER_HOST, BROKER_PORT, 60)

    print(f"Starting device: {DEVICE_ID}")
    print(f"Location: {LOCATION}")
    print(f"Publishing to: {TOPIC}")
    print("Interval: 2 seconds")
    print("-" * 40)

    while True:
        reading = sensor.generate_reading()
        message = json.dumps(reading)

        client.publish(TOPIC, message)

        print(
            f"[{reading['counter']}] "
            f"Pressure: {reading['pressure']['upstream_psi']}/"
            f"{reading['pressure']['downstream_psi']} PSI, "
            f"Flow: {reading['flow']['rate_gpm']} gal/min"
        )

        time.sleep(2)


if __name__ == "__main__":
    main()