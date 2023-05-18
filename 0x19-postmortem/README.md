### 0x19. Postmortem
### Postmortem: Outage on May 15, 2023
#### Summary
On April 15, 2021, our web application experienced an outage that lasted for approximately 2 hours. The outage was caused by a server issue that resulted in the application being unavailable to users. The impact of the outage was significant, with many users unable to access critical functionality of the application during the outage.

#### Timeline
1:00 PM - A server issue is detected, causing the application to become unavailable to users.
1:15 PM - The issue is escalated to the development team for investigation.
1:30 PM - The development team determines that the issue is related to a hardware failure on one of the servers.
1:45 PM - The team attempts to restore service by moving the application to another server, but encounters difficulties due to the complexity of the application.
2:30 PM - The team successfully migrates the application to a new server and service is restored to users.
3:00 PM - The team conducts a postmortem to analyze the incident and identify steps to prevent future occurrences.
#### Cause
The root cause of the outage was a hardware failure on one of the servers that was hosting the application. Specifically, the hard drive failed, which caused the server to become unresponsive and the application to be unavailable to users.

#### Impact
The impact of the outage was significant, with many users unable to access critical functionality of the application during the outage. This resulted in frustration and inconvenience for users, as well as potential financial losses for the company.

#### Mitigation
To mitigate the impact of the outage, the development team worked quickly to migrate the application to a new server. However, the migration process was complicated by the complexity of the application, which made it difficult to move to a new server without encountering issues.
