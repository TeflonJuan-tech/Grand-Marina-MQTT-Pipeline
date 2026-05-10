import json
from datetime import datetime

import paho.mqtt.client as mqtt


BROKER_HOST = "localhost"
BROKER_PORT = 1883

TOPIC = "hydroficient/grandmarina/#"


def print_dashboard_header():
    print("=" * 60)
    print("  GRAND MARINA WATER MONITORING DASHBOARD")
    print(f"  Connected at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print_dashboard_header()
        client.subscribe(TOPIC)
        print(f"\nSubscribed to: {TOPIC}")
    else:
        print(f"Failed to connect. Return code: {rc}")


def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode("utf-8")
        data = json.loads(payload)

        print("\n" + "─" * 40)
        print(f"  Location:  {data.get('location', 'Unknown')}")
        print(f"  Device ID: {data.get('device_id', 'Unknown')}")
        print(f"  Time:      {data.get('timestamp', 'Unknown')}")
        print(f"  Count:     #{data.get('counter', 'Unknown')}")
        print("─" * 40)

        pressure = data.get("pressure", {})
        flow = data.get("flow", {})

        print(f"  Pressure (upstream):    {pressure.get('upstream_psi', 'N/A')} PSI")
        print(f"  Pressure (downstream):  {pressure.get('downstream_psi', 'N/A')} PSI")
        print(f"  Flow rate:              {flow.get('rate_gpm', 'N/A')} gal/min")
        print(f"  Pressure differential:  {pressure.get('differential_psi', 'N/A')} PSI")

    except json.JSONDecodeError:
        print("\nReceived non-JSON message:")
        print(msg.payload.decode("utf-8", errors="replace"))

    except Exception as error:
        print(f"\nError processing message: {error}")


def main():
    client = mqtt.Client()

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER_HOST, BROKER_PORT, 60)
    client.loop_forever()


if __name__ == "__main__":
    main()