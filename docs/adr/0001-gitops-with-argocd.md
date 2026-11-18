# ADR-0001: Use GitOps with ArgoCD

- Status: Accepted
- Date: 2026-11-18

## Context
We need auditable, repeatable deployments across three environments with easy
rollback and drift detection.

## Decision
Use ArgoCD with an app-of-apps pattern. Git is the single source of truth for
cluster state. CI never talks to the cluster directly.

## Consequences
- (+) Full audit trail, PR-based approvals, automatic drift correction
- (+) No cluster credentials stored in CI
- (-) Extra component to operate and secure
- (-) Secrets need a separate solution (see future ADR on External Secrets)

## Alternatives considered
- Push-based deploys from CI (Helm in pipeline): simpler, but no drift detection
- Flux: comparable, but ArgoCD's UI and Rollouts integration fit our needs
