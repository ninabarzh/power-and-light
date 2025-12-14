# Example authorisation clause for UU P&L

\[Testing Firm] is authorised to conduct security assessment of Unseen University 
Power & Light Co. industrial control systems as follows:

In scope:
- IP ranges 192.168.10.0/24 (Turbine Control), 192.168.20.0/24 (Distribution SCADA), 
  192.168.30.0/24 (Reactor Controls)
- Engineering workstations ENG-WS-01 through ENG-WS-04
- SCADA servers SCADA-PRIMARY and SCADA-BACKUP
- HMI workstations in main control room

Authorised activities:
- Passive network reconnaissance and traffic analysis
- Active network scanning at rates not exceeding 100 packets/second
- Enumeration of PLCs, RTUs, and SCADA components
- Reading PLC configurations and programs (download only, no upload)
- Testing authentication on HMIs and engineering workstations using provided test 
  credentials and common default credentials
- Web application security testing of SCADA and HMI web interfaces
- Social engineering testing of specified personnel (list attached)

Specifically prohibited activities:
- Any write operations to production PLCs
- Any commands that affect physical equipment state
- Any interaction with safety systems beyond passive observation
- Denial of service testing
- Testing during blackout periods (weekdays 16:00-20:00, weekends, holidays)
- Testing without prior coordination with on-site OT Engineering Manager

Time period:
- Testing authorised from 1 March 2026 to 31 March 2026
- Daily test windows: Weekdays 02:00-06:00 and 10:00-15:00
- Each test activity requires day-of approval from OT Engineering Manager

Authorised personnel:
- \[Named testers from Testing Firm]
- Must present authorisation letter and photo ID upon request

Incident reporting:
- Immediate notification (within 1 hour) to OT Engineering Manager for any finding 
  that creates immediate risk
- Daily brief summary of activities and preliminary findings
- Final report within 2 weeks of test completion

This authorisation is signed by \[Archchancellor], approved by Board of Governors 
\[date], with notification provided to \[City Emergency Services, National Cyber 
Security Centre, Insurance Provider].

Signed: \[Archchancellor]
Date: \[Date]
Witness: \[Senior Bursar]