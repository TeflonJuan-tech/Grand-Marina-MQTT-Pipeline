\# Grand Marina MQTT Pipeline



Project Type: IoT Telemetry Pipeline  

Security State: Insecure Baseline  

Architecture: Sensor → MQTT Broker → Dashboard  

Client Scenario: The Grand Marina / HYDROLOGIC Water Monitoring  



\---



\## Executive Summary



This project builds an insecure baseline MQTT pipeline for The Grand Marina’s HYDROLOGIC water monitoring environment.



A Python publisher simulates a HYDROLOGIC sensor generating real-time water pressure and flow telemetry. The data is published to a Mosquitto MQTT broker and received by a Python subscriber that functions as a terminal-based monitoring dashboard.



The purpose of this project was to validate real-time sensor-to-dashboard telemetry before future security hardening, including TLS encryption, authentication, and topic-level access control.



\---



\## Pipeline Architecture



```mermaid

flowchart LR

&#x20;   A\["HYDROLOGIC Sensor Publisher<br>sensor\_publisher.py"] --> B\["Mosquitto MQTT Broker<br>localhost:1883"]

&#x20;   B --> C\["Grand Marina Dashboard Subscriber<br>dashboard\_subscriber.py"]

&#x20;   C --> D\["Formatted Terminal Dashboard"]



&#x20;   A -->|"Publishes JSON readings every 2 seconds"| B

&#x20;   B -->|"Routes messages by MQTT topic"| C

&#x20;   C -->|"Parses and displays telemetry"| D



