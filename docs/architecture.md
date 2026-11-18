# Architecture Overview

## Goals
- Reproducible infrastructure (Terraform, remote state)
- Declarative delivery (GitOps with ArgoCD)
- Secure supply chain (scan, SBOM, sign, enforce)
- Observable by default (metrics, logs, traces, SLOs)
- Recoverable (tested backups, documented DR)

## Environments
| Env | Purpose | Promotion |
|---|---|---|
| dev | fast feedback | auto on merge to main |
| staging | prod-like validation | auto after dev health checks |
| prod | customer traffic | manual approval, canary rollout |

## Flow
Developer -> PR -> CI (test, scan, build, sign) -> image registry
-> GitOps repo update -> ArgoCD sync -> Argo Rollouts canary -> prod
