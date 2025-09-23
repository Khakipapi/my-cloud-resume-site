# 🌐 Cloud Resume Project — José Reyes

Live site: josereyes.cloud


## ⚡ Quick Impact Summary

- ✅ Built a **production-ready AWS system** with global distribution  
- ✅ Automated deployments using **Terraform + GitHub Actions**  
- ✅ Designed a **serverless backend** with API Gateway, Lambda, and DynamoDB  
- ✅ Applied **security best practices** (private S3, OAC, least-privilege IAM)  
- ✅ Delivered a **scalable, professional résumé site** hosted in the cloud  

## 🎯 Project Purpose

This project is more than just a résumé page — it’s a **real-world cloud application**.  
It was built as part of the **Cloud Resume Challenge**, a widely recognized test of cloud and DevOps skills.  

Through this project, I demonstrated:  
- **Cloud architecture design** on AWS  
- **Infrastructure as Code (IaC)** with Terraform  
- **Full-stack development** combining frontend + backend + APIs  
- **Automation & CI/CD pipelines** with GitHub Actions  

## 💡 Project Showcase

Here’s what this site demonstrates in action:

- **Professional Presentation**  
  Visitors land on a modern, responsive homepage that showcases my résumé and portfolio.  

- **Reliability & Availability**  
  The résumé is hosted on AWS S3 and delivered through CloudFront, ensuring fast, secure access worldwide.  

- **Dynamic Features**  
  A live visitor counter proves backend integration with DynamoDB, API Gateway, and Lambda.  

- **Automation Behind the Scenes**  
  Each code push triggers GitHub Actions to deploy updates automatically to AWS, showing CI/CD expertise.  

- **Scalability & Security**  
  Architecture is designed with private storage, least-privilege IAM, and serverless scaling.  

(Screenshots available in `screenshots/` folder: homepage.png, resume.png, counter.png)

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
