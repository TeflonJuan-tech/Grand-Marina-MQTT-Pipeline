\# Grand Marina MQTT Pipeline



\*\*Status:\*\* Completed  

\*\*Project Type:\*\* IoT Telemetry Pipeline  

\*\*Security State:\*\* Insecure Baseline  

\*\*Architecture:\*\* Sensor → MQTT Broker → Dashboard  

\*\*Client Scenario:\*\* The Grand Marina / HYDROLOGIC Water Monitoring  



\---



\## Executive Summary



This project builds an insecure baseline MQTT pipeline for The Grand Marina’s HYDROLOGIC water monitoring environment.



A Python publisher simulates a HYDROLOGIC water sensor generating real-time water pressure and flow telemetry. The data is published to a Mosquitto MQTT broker and received by a Python subscriber that functions as a terminal-based monitoring dashboard.



The purpose of this project was to validate real-time Sensor → Broker → Dashboard telemetry before future security hardening, including TLS encryption, authentication, and topic-level access control.



\---



\## Pipeline Architecture



```mermaid

flowchart LR

&#x20;   Sensor\["HYDROLOGIC Sensor Publisher<br/>sensor\_publisher.py"]

&#x20;   Broker\["Mosquitto MQTT Broker<br/>localhost:1883"]

&#x20;   Dashboard\["Grand Marina Dashboard Subscriber<br/>dashboard\_subscriber.py"]

&#x20;   Output\["Formatted Terminal Dashboard"]



&#x20;   Sensor -->|"Publishes JSON telemetry every 2 seconds"| Broker

&#x20;   Broker -->|"Routes messages by MQTT topic"| Dashboard

&#x20;   Dashboard -->|"Parses and displays readings"| Output

