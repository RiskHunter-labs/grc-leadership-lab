# 🗂️ Athenex Policy Taxonomy & Governance Hierarchy

This file outlines the governance structure and naming conventions used to develop, manage, and enforce policies across Athenex.

---

## 🔹 Policy Hierarchy

| Tier | Document Type | Purpose |
|------|---------------|---------|
| 1 | **Policy** | High-level, board-approved directives that define Athenex's principles and commitments (e.g., Information Security Policy) |
| 2 | **Standard** | Mandatory specifications and thresholds derived from policy (e.g., Encryption Standard, Access Control Standard) |
| 3 | **Procedure** | Step-by-step processes for implementing standards (e.g., Onboarding Procedure, Incident Response Procedure) |
| 4 | **Guideline** | Recommended practices or reference guidance (e.g., Secure Coding Guideline) |

---

## 🔹 Governance Process

- All policies and standards are reviewed **annually**
- Ownership is defined by function (e.g., IT owns the Access Control Standard; Legal owns the Data Sharing Policy)
- Changes require review and approval by the **SPR Council**
- Document metadata includes version history, control mappings, and approval date

---

## 🔹 Naming Convention

```
[Category]_[DocumentType]_[Version].md

Examples:
- Security_Policy_v1.0.md
- Privacy_Standard_DataRetention_v2.1.md
- AccessControl_Procedure_v1.2.md
```

---

## 🔁 Integration with Controls & Audits

- All Tier 1–3 documents are traceable to the SCF-based Controls Matrix
- Each document includes a control reference section (`Mapped Controls:`) to enable audit traceability
- GitHub repo structure mirrors this taxonomy under `/03_Artifacts/` and `/05_Controls_Mapping/`
