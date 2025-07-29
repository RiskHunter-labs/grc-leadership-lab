# ☁️ Athenex Cloud & Tech Stack – Architecture Diagram (Mermaid)

This diagram illustrates the hybrid multi-cloud and on-prem ecosystem at Athenex Solutions, covering SaaS, AI, DevOps, compliance, and customer trust layers.

```mermaid
graph TD
  %% Cloud Providers
  AWS[AWS - SaaS, IAM, Containers]
  Azure[Azure - Enterprise IT, Identity]
  GCP[GCP - AI/ML, Analytics]
  OCI[OCI - Oracle Workloads]
  Colo[Colo/On-Prem - R&D Labs, Legacy Interop, Edge AI]

  %% Compute & DevOps
  Compute[Compute & Containers - EKS, AKS, GKE, microK8s]
  DevOps[DevOps & IaC - GitHub Actions, Terraform, Jenkins]

  %% Data & Observability
  Data[Data Platforms - S3, BigQuery, Oracle, PostgreSQL]
  Observability[Observability - Grafana, Prometheus, Datadog]

  %% Security & Compliance
  Security[Security & IAM - Vault, GuardDuty, Azure AD]
  Compliance[Compliance Tooling - SOC 2, ISO, Drata, Vanta]

  %% AI Stack
  AI[AI / LLM Stack - Vertex AI, OpenAI, LangChain, R&D Labs]

  %% SaaS & Trust
  SaaS[SaaS Products - Regulated Cloud Platforms]
  Trust[Customer Trust - Audit Readiness, CAIQ, RFPs]

  %% Connections
  AWS --> Compute
  Azure --> Compute
  GCP --> Compute
  OCI --> Compute
  Colo --> Compute

  AWS --> DevOps
  Azure --> DevOps
  GCP --> DevOps
  Colo --> DevOps

  Compute --> Data
  DevOps --> Observability
  Compute --> Security
  DevOps --> Compliance

  Data --> AI
  Security --> AI
  Compliance --> AI
  Colo --> AI

  AI --> SaaS
  DevOps --> SaaS
  SaaS --> Trust
  Compliance --> Trust

```
