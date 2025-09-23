# 🌐 Cloud Resume Project — José Reyes

**Live site:** [https://josereyes.cloud](https://josereyes.cloud)

Welcome! This repository contains my **cloud-hosted résumé website**, built as part of the **Cloud Resume Challenge**. It demonstrates my ability to design secure cloud architectures, automate deployments, and integrate frontend + serverless backend services.

---

## 👀 What Recruiters Will See

### Homepage
![Homepage](./screenshots/homepage.png)  
*A clean, responsive landing page linking to my résumé and projects.*

### Résumé Section
![Résumé](./screenshots/resume.png)  
*My résumé, hosted on highly available AWS infrastructure.*

### Live Visitor Counter
![Visitor Counter](./screenshots/counter.png)  
*A DynamoDB-backed counter exposed via API Gateway + Lambda, displayed on the site.*

> 📌 Place your screenshots in a `screenshots/` folder at the repo root to make these images load.

---

## 🧭 Project Overview (Why It Matters)

This project is a production-style, full-stack cloud app that shows I can:

- **Architect secure, scalable systems** on AWS  
- **Automate deployments** with CI/CD (GitHub Actions → S3/CloudFront)  
- **Write and integrate code** across the stack (HTML/CSS/JS + Python Lambda)  
- **Work like a cloud/DevOps engineer**: IaC, least-privilege IAM, OAC, cache strategy  

Roles it aligns with: **Cloud Engineer, DevOps Engineer, Platform Engineer, SRE**.

---

## 🏗️ Architecture

```txt
Browser
   │
   ▼
CloudFront (CDN, TLS via ACM)
   │
   ├──► S3 (static site: HTML/CSS/JS)
   │
   └──► API Gateway
           │
           ▼
        Lambda (Python)
           │
           ▼
        DynamoDB (visitor counter)

DNS: Route 53 (A/AAAA alias to CloudFront)
