# Cybersecurity-Incident-Response-Agent
Assist security teams by triaging incidents using multi-agent reasoning.


This project is a multi-agent cybersecurity triage assistant designed to analyze uploaded system logs or alert files. It includes a Log Parser Agent that reads raw log data and extracts suspicious events, failed logins, unusual IP activity, and anomaly patterns. The parsed findings are then passed to a Threat Intelligence Agent, which reasons about possible attack types, threat severity, and indicators of compromise. Finally, a Containment Advisor Agent uses that analysis to recommend practical incident response actions such as isolation, investigation, credential rotation, or monitoring. Together, these agents simulate a lightweight AI-assisted SOC workflow, and all incident sessions are stored so users can review past analyses and response recommendations.
