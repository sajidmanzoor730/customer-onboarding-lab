#!/bin/bash
echo "Checking onboarding health..."
df -h
cat /var/log/syslog | tail -20
curl -s https://api.example.com/health | jq .
echo "Done"
