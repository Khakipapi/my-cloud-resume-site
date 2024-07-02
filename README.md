# Jose Reyes Cloud Resume
![image](https://github.com/Khakipapi/my-cloud-resume-site/assets/74410806/4b49e0d8-c98e-4f05-8bcc-b8d3fc69369a)

## Introduction
This project showcases the cloud resume and portfolio of Jose Reyes, a skilled Cloud Engineer with expertise in Python, AWS, and Linux. The project includes static web pages hosted on AWS services such as Lambda, Route 53, CloudFront, and S3.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Documentation](#documentation)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Installation
To deploy this project, follow the steps below:

1. Clone the repository:
    ```sh
    git clone https://github.com/Khakipapi/cloud-resume.git
    ```

2. Set up your AWS credentials and configuration:
    ```sh
    aws configure
    ```

3. Deploy the infrastructure using Terraform:
    ```sh
    cd terraform
    terraform init
    terraform apply
    ```

4. Upload the static website files to the S3 bucket:
    ```sh
    aws s3 sync ./path/to/your/files s3://your-s3-bucket-name
    ```

## Usage
To access the deployed resume website, navigate to the CloudFront URL or the custom domain configured through Route 53.

## Features
- Static resume website
- Hosted on AWS S3 with CloudFront for CDN
- Serverless backend using AWS Lambda
- DNS management using AWS Route 53
- CI/CD pipeline using GitHub Actions
- Infrastructure as Code using Terraform

## Dependencies
- AWS CLI
- Terraform
- boto3 (Python SDK for AWS)

## Configuration
1. **AWS S3**: Store static website files.
2. **AWS Lambda**: Serverless function to handle backend operations.
3. **AWS CloudFront**: Content Delivery Network for the website.
4. **AWS Route 53**: DNS management for custom domain.
5. **GitHub Actions**: CI/CD pipeline for automatic deployment.

## Documentation
### Lambda Function (func.py)
This function increments the view count stored in DynamoDB each time the resume page is accessed.
```python
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloudresumetest')

def handler(event, context):
    response = table.get_item(Key={'ID': '0'})
    views = response['Item']['views']
    views = views + 1
    response = table.put_item(Item={'ID': '0', 'views': views})
    return views
