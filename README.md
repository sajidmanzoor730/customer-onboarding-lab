# Customer Onboarding Lab — Orca Security CSE Practice

Simulates customer onboarding workflow: environment connection, initial config, health checks, alert triage.

## Workflow
1. Environment Connection — connect AWS account / lab VM
2. Initial Configuration — VPC, IAM role, CloudWatch
3. First Value — verify logs flowing
4. Troubleshooting — logs, APIs, CLI

## Runbook
See RUNBOOK.md for step-by-step customer onboarding steps.

## Automation
health_check.sh and check_logs.py automate onboarding verification.
