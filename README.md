\# Grand Marina MQTT Pipeline



\*\*System Type:\*\* IoT Water Monitoring Pipeline  

\*\*Architecture:\*\* Sensor → MQTT Broker → Dashboard  

\*\*Security State:\*\* Intentionally Insecure Baseline  



\---



\## Executive Summary



This project builds a working real-time IoT data pipeline for The Grand Marina water monitoring environment. A Python-based HYDROLOGIC sensor publisher generates realistic pressure and flow telemetry, sends the readings to a Mosquitto MQTT broker, and a Python subscriber dashboard receives and displays the readings in real time.



The goal of this project was to validate basic MQTT publish/subscribe behavior before adding future security controls such as TLS encryption, authentication, and topic-level access control.



\---



\## Architecture



```mermaid

flowchart LR

&#x20;   A\[HYDROLOGIC Sensor Publisher<br>sensor\_publisher.py] -->|Publishes JSON telemetry<br>Topic: hydroficient/grandmarina/sensors/main-building/readings| B\[Mosquitto MQTT Broker<br>Port 1883]

&#x20;   B -->|Routes messages| C\[Dashboard Subscriber<br>dashboard\_subscriber.py]

&#x20;   C -->|Displays pressure, flow,<br>timestamp, counter, and device ID| D\[Terminal Dashboard Output]



MQTT Topic Used

hydroficient/grandmarina/sensors/main-building/readings



The subscriber listens to all Grand Marina topics using:



hydroficient/grandmarina/#



Technologies Used

Python

Paho MQTT

Mosquitto MQTT Broker

JSON telemetry messages

Windows / Anaconda Prompt



Project Components

| File                      | Purpose                                                                           |

| ------------------------- | --------------------------------------------------------------------------------- |

| `sensor\_publisher.py`     | Simulates a HYDROLOGIC water sensor and publishes telemetry every 2 seconds       |

| `dashboard\_subscriber.py` | Subscribes to Grand Marina MQTT topics and displays incoming readings             |

| `screenshots/`            | Contains validation evidence for broker, publisher, subscriber, and full pipeline |



Telemetry Fields



Each published reading includes:



Device ID

Location

Counter

UTC ISO 8601 timestamp

Upstream pressure

Downstream pressure

Pressure differential

Flow rate



Screenshots

Mosquitto Broker Running



Publisher Sending Sensor Readings



Subscriber Dashboard Receiving Readings



End-to-End Pipeline Validation



How to Run

1\. Install dependencies

pip install paho-mqtt



2\. Start Mosquitto

mosquitto -v



3\. Start the subscriber dashboard

python dashboard\_subscriber.py



4\. Start the sensor publisher

python sensor\_publisher.py



Validation Results



The pipeline was successfully validated with:



Mosquitto running on port 1883

Publisher sending readings every 2 seconds

Subscriber receiving and parsing JSON messages

Incrementing message counters

Realistic variation in pressure and flow values

Matching telemetry between publisher and dashboard output



Security Note



This pipeline is intentionally insecure. It uses a local unauthenticated MQTT broker without TLS encryption. In a production IoT environment, this design would require:



TLS encryption

Device authentication

Broker access control

Topic-level authorization

Secure credential handling

Monitoring for abnormal publish/subscribe behavior



This insecure baseline will be useful for future comparison when security controls are added.



Key Learning Outcomes

Built an end-to-end MQTT pipeline

Practiced real-time IoT telemetry streaming

Implemented MQTT publish/subscribe architecture

Parsed and displayed structured JSON data

Troubleshot broker port conflicts and service issues

Documented pipeline validation using screenshots



Project Context



This project was completed as part of the Hydroficient IoT Cyber Defense Externship. It supports a larger smart water monitoring scenario involving MQTT-based telemetry, sensor data pipelines, and future IoT security hardening.





