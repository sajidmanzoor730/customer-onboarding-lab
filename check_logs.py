import json
print("Parsing logs for onboarding errors...")
# sample log triage
with open('/var/log/syslog') as f:
    for line in f:
        if "ERROR" in line:
            print(line)
