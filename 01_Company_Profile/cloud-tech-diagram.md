# ☁️ Athenex Cloud & Tech Stack – Architecture Diagram (Mermaid)

This diagram illustrates the hybrid multi-cloud and on-prem ecosystem at Athenex Solutions, covering SaaS, AI, DevOps, compliance, and customer trust layers.

```mermaid
graph TD
  %% Cloud Providers
  AWS[AWS<br/>(SaaS, IAM, Containers)]
  Azure[Azure<br/>(Enterprise IT, Identity)]
  GCP[GCP<br/>(AI/ML, Analytics)]
  OCI[OCI<br/>(Oracle Workloads)]
  Colo[Co-Location & On-Prem<br/>(R&D Labs, Legacy Interop, Edge AI)]

  %% Compute & DevOps
  Compute[Compute & Containers<br/>(EKS, AKS, GKE, microK8s)]
  DevOps[DevOps & IaC<br/>(GitHub Actions, Terraform, Jenkins)]

  %% Data & Observability
  Data[Data Platforms<br/>(S3, BigQuery, Oracle, PostgreSQL)]
  Observability[Observability<br/>(Grafana, Prometheus, Datadog)]

  %% Security & Compliance
  Security[Security & IAM<br/>(Vault, GuardDuty, Azure AD)]
  Compliance[Compliance Tooling<br/>(SOC 2, ISO, Drata, Vanta)]

  %% AI Stack
  AI[AI / LLM Stack<br/>(Vertex AI, OpenAI, LangChain, R&D Labs)]

  %% SaaS & Trust
  SaaS[SaaS Products<br/>(Regulated Cloud Platforms)]
  Trust[Customer Trust<br/>(Audit Readiness, CAIQ, RFPs)]

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
