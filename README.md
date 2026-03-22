# Automated File Processing System (AWS Serverless + EC2)

# Overview
This project automates file upload, processing, and storage using AWS services.

# Architecture
EC2 → S3 (input bucket) → Lambda → S3 (output bucket)

# Tech Stack
- AWS EC2
- AWS Lambda
- Amazon S3
- IAM Roles
- VPC (Public + Private Subnet)
- Python

# Features
- Automated file upload from EC2 using Python
- Event-driven processing using Lambda
- Secure architecture using IAM roles
- Private subnet Lambda with NAT Gateway

# Key Learnings
- VPC design (CIDR, subnets, routing)
- IAM role troubleshooting
- Lambda VPC networking issues
- Debugging Python indentation errors

# Workflow
1. EC2 uploads file to S3
2. S3 triggers Lambda
3. Lambda processes file and stores in output bucket

# Challenges Faced
- Lambda failed in private subnet due to no internet access
- Fixed using NAT Gateway / S3 access
- Debugged file upload issue (indentation bug)
