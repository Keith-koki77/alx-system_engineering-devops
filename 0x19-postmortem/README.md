# POSTMORTEM: Web Stack Outage Incident

## Issue Summary
* Start Time: October 9,2023, 10:45AM (EAT).
* End Time: October 9,2023, 3:30PM (EAT).
* The outage affected the user authentication service, leading to a complete disruption of user logins
* Approximately 65% of the users were unable to acccess their accounts during the outage.

## Root Cause:
* The root cause of the outage wasidentified as an unexpected configuration change in the authentication microservice, which resulted in the failure of user login.

## Timeline:
### Detection Time:
* October 9,2024,10:45AM(EAT)
### Detection Method:
* A monitoring alert triggered due to increased failed authentication attempts.
### Action:
* A thorough investigation on server logs was done to identify potential issues wit authentication service
* It was also thought a recent deployment of the software might have caused the outage.
### Misleading Paths:
* An exploration on network-related issues was done including DDoS attack, which was not the case.
* Database performance was thought to be the problem but proved otherwise.
### Escalation:
* The DevOps and DevSecOps teams were involved in due to the escelated incident, for a comprehensive investigation.
### Resolution:
* Rolled back the recent configuration change in the authentication microservice to the last known stable version.
* Implemented a hotfix to address the token verification failure.
* Conducted thorough testing to ensure the stability of the service.

## Root Cause and Resolution:
### Root Cause and Explanation:
* The unexpected configuration change in the authentication microservice introduced a bug that prevented the proper verification of user tokens. This was the cause of denial to the users service on login.
### Resolution Details:
* Rolled back the configuration to the previous stable version.
* Applied a hotfix to correct the token verification logic.
* Implemented additional checks in the deployment pipeline to catch similar configuration issues before reaching production.

## Corrective and Preventive Measures:
### Areasfor Improvement:
* Strengthen monitoring and alerting mechanisms to quickly detect unusual authentication patterns.
* Enhance collaboration betweeen deployment and operations team to ensure awareness of configuration changes.
### Tasks to Address the Issues:
* Implement a more robust configuration management process, including rigorous testing in a staging environment.
* Enhance logging to capture detailed information about configuration changes.
* conduct a post-incident review to identify additional improvements to the incident response process.
