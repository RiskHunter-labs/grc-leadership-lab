# ☁️ Athenex Solutions – Cloud & Hybrid Tech Stack Overview

_Athenex Solutions operates a cloud-first, hybrid-enabled architecture across AWS, Azure, GCP, and OCI, with strategic on-premise and co-location environments to meet compliance, sovereignty, and AI latency requirements._

---

## 1. Cloud Infrastructure Strategy

| Cloud Provider | Primary Usage |
|----------------|----------------|
| **AWS**        | Core SaaS hosting, IAM, container workloads (EKS), CDN (CloudFront) |
| **Azure**      | Enterprise IT systems, identity (Azure AD), M365, regulated client data zones |
| **GCP**        | AI/ML pipelines, LLM training & inference, analytics (BigQuery), DevSecOps environments |
| **OCI**        | Oracle-based workloads for healthcare and financial clients |
| **Colo / On-Prem** | Air-gapped R&D zones, legacy ERP interop, edge AI inference, regional BCDR |

---

## 2. Compute, Containers & Orchestration

| Layer                     | Technologies Used |
|---------------------------|-------------------|
| Virtual Compute           | AWS EC2, Azure VMs, GCP Compute Engine, On-Prem VM Hosts |
| Containerization          | Docker, AWS Fargate, Azure Container Instances |
| Kubernetes Orchestration  | Amazon EKS, Azure AKS, GCP GKE, Rancher, microK8s (on-prem edge) |
| Serverless                | AWS Lambda, Azure Functions, GCP Cloud Functions |

---

## 3. Data Platforms & Analytics

| Category         | Stack |
|------------------|-------|
| Relational DBs   | PostgreSQL, MySQL (RDS), Oracle DB (OCI/on-prem), SQL Server |
| NoSQL Databases  | DynamoDB, Firestore, CosmosDB, Redis, MongoDB Atlas |
| Data Lakes       | S3 + Athena, Azure Data Lake, GCP BigQuery |
| BI / Analytics   | Looker, Power BI, Tableau, Amazon QuickSight |

---

## 4. AI, ML & LLM Infrastructure

| Area                    | Tech Stack / Services |
|--------------------------|------------------------|
| AI Infrastructure       | GCP Vertex AI, Azure OpenAI, AWS SageMaker, OCI Data Science, on-prem R&D clusters |
| LLM Training / Hosting  | LLaMA 2, Mistral on GCP/Azure; sensitive training on air-gapped hardware |
| Model Serving           | Triton, TensorFlow Serving, SageMaker Endpoints, Edge Inference (K3s) |
| Prompt Orchestration    | LangChain, LlamaIndex, PromptFlow, Bedrock |
| AI Governance           | MLflow, ISO 42001 alignment, NIST AI RMF, GCP Explainable AI |

---

## 5. Security, IAM & Compliance

| Area                     | Stack |
|--------------------------|-------|
| IAM / SSO                | Azure AD, Okta, AWS IAM, GCP IAM |
| Secrets Management       | AWS Secrets Manager, Azure Key Vault, HashiCorp Vault |
| Cloud Security Monitoring| GuardDuty, Azure Sentinel, GCP Security Command Center, Wiz |
| SIEM & SOAR              | Splunk, Sentinel, Chronicle SOAR |
| Vulnerability Mgmt       | Tenable, Aqua, Prisma Cloud, Snyk |
| Compliance Tooling       | Drata, Vanta, AWS Artifact, Azure Compliance Manager |

---

## 6. DevOps & Infrastructure-as-Code

| Area               | Stack |
|--------------------|-------|
| CI/CD Pipelines    | GitHub Actions, GitLab CI, Azure DevOps, Jenkins, ArgoCD |
| Infrastructure as Code | Terraform (cloud + on-prem), Pulumi, CloudFormation, Bicep |
| Config Management  | Ansible, Chef, AWS Systems Manager, Azure Automation |
| Observability      | Prometheus, Grafana, Datadog, CloudWatch, Azure Monitor |

---

## 7. SaaS & Collaboration Stack

| Category             | Stack |
|----------------------|-------|
| Collaboration / Docs | M365, SharePoint, Slack, Confluence |
| Issue Tracking       | Jira, Azure DevOps Boards |
| Asset Management     | ServiceNow, Lansweeper |
| ITSM / Support       | Zendesk, Jira Service Management |

---

## 8. Hybrid Footprint: Co-Location & On-Prem Strategy

| Environment Type         | Description & Use Case |
|--------------------------|-------------------------|
| **Private Data Vaults**  | Co-located Oracle & SQL servers for HIPAA, SOX, financial records |
| **Edge AI Inference Nodes** | microK8s clusters for low-latency AI workloads in regulated markets |
| **Air-Gapped AI R&D Labs** | Internal facilities for model testing, red teaming, safety analysis |
| **Legacy ERP Gateways**  | Interoperability zones for financial and manufacturing clients |
| **Regional DR Sites**    | Hybrid disaster recovery across cloud and colocation backups |

---

## Summary

Athenex’s tech stack is designed for **secure, scalable, and compliance-first service delivery**. By combining multi-cloud agility with **selective on-prem control**, we meet the **most demanding requirements** in healthcare, finance, energy, and public sector environments. Our architecture supports:

- AI innovation (LLMs, agents, prompt chaining)
- Regulated cloud workloads with full observability
- Global data protection and sovereignty compliance
- Modular SaaS platforms with customer trust built-in
