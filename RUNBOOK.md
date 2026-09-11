# Customer Onboarding Runbook

## Step 1: Pre-check
- Verify AWS credentials, VPC, IAM permissions
- Check Linux: df -h, top, systemctl status

## Step 2: Onboard
- Connect environment
- Configure initial policies
- Time-to-first-value: <30 mins

## Step 3: Post-check
- Run ./health_check.sh
- Check logs: python3 check_logs.py
- Document in Confluence/KB

## Step 4: Escalation
- If fails, collect logs + API response, create JIRA ticket
