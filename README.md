# 🌐 Cloud Resume Project — José Reyes

**Live site:** [josereyes.cloud](https://josereyes.cloud)

Welcome! This repository contains my **cloud-hosted résumé website**, built as part of the **Cloud Resume Challenge**. It demonstrates my ability to design secure cloud architectures, automate deployments, and integrate frontend + serverless backend services.


### Homepage
![Homepage](screenshots/homepage.png)
*A clean, responsive landing page linking to my résumé and projects.*

### Résumé Section
![Résumé](screenshots/resume.png)
*My résumé, hosted on highly available AWS infrastructure.*

### Live Visitor Counter
![Visitor Counter](screenshots/counter.png)
*A DynamoDB-backed counter exposed via API Gateway + Lambda, displayed on the site.*

> If images don’t load on GitHub, ensure this repo contains `screenshots/homepage.png`, `screenshots/resume.png`, and `screenshots/counter.png`.

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

**Highlights**
- Private S3 bucket with **CloudFront Origin Access Control** (OAC)
- **HTTPS** everywhere (ACM cert in `us-east-1`)
- **Serverless** backend that scales automatically

---

## 🛠️ Skills Demonstrated

**Cloud & Infra**
- AWS: S3, CloudFront, Route 53, ACM, API Gateway, Lambda, DynamoDB
- Security: private S3 + CloudFront OAC, least-privilege IAM
- Reliability/Perf: global edge caching with CloudFront

**DevOps & Automation**
- CI/CD with GitHub Actions (push → deploy → cache invalidate)
- Infrastructure as Code (Terraform)
- Version control & code review workflows (Git/GitHub)

**Software Development**
- Frontend: HTML, CSS/SCSS, JavaScript (responsive)
- Backend: Python Lambda (API logic), JSON API integration
- Observability basics: CloudWatch logs for Lambda

---

## 🚀 Live Demo

- 🌐 **Website:** https://josereyes.cloud  
(If you don’t see fresh changes immediately, CloudFront may be serving cached assets; my pipeline can trigger invalidations.)

---

## 📂 Repository Layout

.
├─ Port_Website/ # Static frontend (HTML, CSS/SCSS, JS)
├─ infra/ # Terraform (provision S3, CF, Route 53, API, Lambda, DDB)
├─ .github/workflows/ # CI/CD pipeline(s)
├─ screenshots/ # Images used in this README
└─ (lambda deps, venv, editor configs as needed)

---

## 🔧 CI/CD (GitHub Actions)

Each push to `main` uploads the site to S3. I use a secure private-bucket pattern (readable by CloudFront via OAC):

```yaml
name: Upload site to S3

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@master
      - uses: jakejarvis/s3-sync-action@master
        with:
          args: --acl private --follow-symlinks --delete
        env:
          AWS_S3_BUCKET: ${{ secrets.AWS_S3_BUCKET }}
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          AWS_REGION: 'us-east-1'
          SOURCE_DIR: 'Port_Website'



