# Grand-Marina-MQTT-Pipeline

IoT MQTT pipeline simulating real-time water sensor telemetry using Python and Mosquitto (Sensor → Broker → Dashboard)



\# Grand Marina MQTT Pipeline



\## Overview

This project simulates a real-time IoT data pipeline for water monitoring using MQTT. A Python-based sensor publisher generates realistic telemetry data and sends it to a Mosquitto broker, while a subscriber dashboard receives and displays the data in real time.



The pipeline follows a standard IoT architecture:



Sensor → Broker → Dashboard



\## Technologies Used

\- Python

\- MQTT (paho-mqtt)

\- Mosquitto Broker



\## Architecture



\- \*\*Publisher\*\*: Simulates a HYDROLOGIC water sensor device

\- \*\*Broker\*\*: Mosquitto MQTT server handling message routing

\- \*\*Subscriber\*\*: Dashboard that processes and displays sensor data



\## Features

\- Real-time data streaming every 2 seconds

\- JSON-formatted telemetry data

\- MQTT topic-based message routing

\- Dashboard-style terminal output

\- Graceful handling of non-JSON messages



\## Screenshots



\### Mosquitto Broker Running

!\[Mosquitto](screenshots/mosquitto-running.png)



\### Publisher Output

!\[Publisher](screenshots/publisher-output.png)



\### Subscriber Dashboard

!\[Subscriber](screenshots/subscriber-output.png)



\### End-to-End Pipeline

!\[Pipeline](screenshots/pipeline-side-by-side.png)



\## How to Run



\### 1. Install dependencies

```bash

pip install paho-mqtt



\### 2. Start Mosquitto

```bash

mosquitto -v



\### 3. Run Subscriber

```bash

python dashboard\_subscriber.py



\### 4. Run Publisher

```bash

python dashboard\_subscriber.py



\##Key Learning Outcomes



\-Built an end-to-end MQTT pipeline

\-Implemented real-time telemetry streaming

\-Practiced publish/subscribe architecture

\-Debugged broker port conflicts and service issues

\-Handled structured JSON data in Python



\##Security Note



This pipeline is intentionally insecure and uses an unauthenticated MQTT broker. In a production environment, TLS encryption, authentication, and topic access controls would be required.



