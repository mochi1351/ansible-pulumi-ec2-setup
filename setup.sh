#!/bin/bash

# Variables
EMAIL="your_email@example.com"
AWS_REGION="your_aws_region"
AWS_ACCESS_KEY="your_aws_access_key"
AWS_SECRET_KEY="your_aws_secret_key"

# Update and upgrade system packages
sudo apt update && sudo apt upgrade -y

# Install AWS CLI
sudo apt install awscli -y

# Configure AWS CLI
echo -e "$AWS_ACCESS_KEY\n$AWS_SECRET_KEY\n$AWS_REGION\njson" | aws configure

# Generate SSH key pair
ssh-keygen -t rsa -b 4096 -C "$EMAIL" -f ~/.ssh/id_rsa -N ""

# Install Ansible (using pip)
sudo apt install python3-pip -y
pip3 install ansible


