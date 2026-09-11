# KB Article: Environment Connection Failed — Troubleshooting Guide

**Audience:** Customer Success Engineer / Customer Admin
**Symptom:** Onboarding stuck at "Connecting environment" — logs show IAM permission error

### Symptoms
- Dashboard shows: `Connection Status: Failed`
- `health_check.sh` output: `ERROR: Unable to assume IAM role`
- `check_logs.py` finds: `ERROR: AccessDenied`

### Root Cause
1. IAM role missing SecurityAudit and ViewOnlyAccess
2. Wrong External ID
3. VPC CloudWatch logs not enabled

### Resolution Steps
1. Verify IAM Role:
aws iam get-role --role-name OrcaSecurityRole

2. Check Trust Policy — ensure External ID matches Orca console

3. Enable CloudTrail + CloudWatch:
aws cloudtrail describe-trails

4. Re-run health check:
./health_check.sh
python3 check_logs.py sample_logs.txt

5. If still fails, escalate:
- Collect health_check.sh output + API response JSON
- Create JIRA: CSE-XXX - Env connection failed for [customer]

### Prevention
- Documented in RUNBOOK.md Step 1 Pre-check
- Added automated check in health_check.sh
