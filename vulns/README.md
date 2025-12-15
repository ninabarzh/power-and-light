# Vulnerability assessment

Important Legal and Ethical Note: These scripts can demonstrate a critical security vulnerability. Using 4-digit p
asswords on industrial control systems (especially reactor controls!) is extremely dangerous. These scripts should 
only be used:

- For authorised penetration testing with written permission
- For educational purposes in controlled environments
- For security research on your own equipment

Important Notes:

    PLC must be in STOP mode for most upload operations

    Authorization required: PLC may need special access rights

    Password handling: snap7 doesn't directly support password setting in the Client class

    Block types: Different S7 families (300/400/1200/1500) have different capabilities

    Safety: Always test on offline/backup PLCs first

Alternative Approach for More Reliability:

For production use, consider using the S7 Communication Protocol directly or using libnodave instead of snap7, as snap7 has some limitations with newer S7 models and certain operations.

