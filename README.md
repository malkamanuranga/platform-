# Production Platform

A production-grade, multi-environment Kubernetes platform: IaC, CI/CD, GitOps,
supply-chain security, observability and disaster recovery.

## Roadmap
- [x] Day 1: repo, API, Docker, CI, security scans, Terraform bootstrap + VPC
- [ ] Day 2: EKS module, IRSA, ArgoCD install, app-of-apps
- [ ] Day 3: Helm chart, Kustomize overlays, Argo Rollouts canary
- [ ] Day 4: Prometheus, Grafana, Loki, Tempo, SLO burn-rate alerts
- [ ] Day 5: Kyverno, NetworkPolicies, External Secrets, Cosign signing
- [ ] Day 6: Velero backup/restore test, chaos experiments, k6 load test
- [ ] Day 7: runbooks, postmortem, cost report, diagrams

## Docs
- [Architecture](docs/architecture.md)
- [ADRs](docs/adr/)
- [Runbook template](docs/runbooks/TEMPLATE.md)
