# Runbook: <Alert / Scenario name>

- Owner: <team>
- Severity: SEV1 | SEV2 | SEV3
- Last reviewed: YYYY-MM-DD

## Symptoms
What the alert or user sees.

## Impact
Who and what is affected.

## Diagnosis
1. Check dashboard: <link>
2. `kubectl get pods -n <ns>`
3. `kubectl logs deploy/<name> -n <ns> --tail=100`

## Mitigation
Step-by-step actions to restore service (rollback, scale, failover).

## Escalation
Who to page and when.

## Follow-up
- [ ] Postmortem opened
- [ ] Alert tuned
