# Ansible Pulumi EC2 Setup

Automate AWS EC2 instance deployment and configuration using Pulumi and Ansible.

## Overview

This project demonstrates how to deploy an AWS EC2 instance using Pulumi and configure it with Ansible. The setup includes:

- Deploying an EC2 instance with specific security group rules and an SSH key pair.
- Configuring the instance by updating and upgrading the system, creating a new user, disabling the root user, and installing necessary packages.

## Project Structure

ansible-pulumi-ec2-setup/
├── ansible.cfg
├── inventory
├── playbook.yml
├── group_vars/
│ └── all.yml
├── host_vars/
│ └── localhost.yml
├── roles/
│ ├── deploy_pulumi/
│ │ └── tasks/
│ │ └── main.yml
│ ├── configure_ec2/
│ │ ├── tasks/
│ │ │ └── main.yml
│ │ └── templates/
│ │ └── pulumi_script.py
└── files/
├── your-private-key
└── .gitignore


## Setup Instructions

### Prerequisites

- Install [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
- Install [Pulumi](https://www.pulumi.com/docs/get-started/install/)
- Install [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- Ensure you have Python3 and pip3 installed

### Configuration

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/ansible-pulumi-ec2-setup.git
    cd ansible-pulumi-ec2-setup
    ```

2. **Update `group_vars/all.yml` with your SSH public key and AWS region:**

    ```yaml
    ansible_user: ubuntu
    ```

3. **Update `host_vars/localhost.yml` with your AWS region, SSH public key, instance type, volume size, new username, and new user password:**

    ```yaml
    aws_region: us-west-2
    ssh_public_key: 'ssh-rsa AAAAB3...your-public-key... user@hostname'
    instance_type: t2.micro
    volume_size: 8
    new_username: newuser
    new_user_password: newpassword
    ```

4. **Ensure your private SSH key is located in the `files/` directory and update `.gitignore` to exclude it from being committed:**

    ```plaintext
    # Ignore SSH private key
    files/your-private-key
    ```

## Usage

1. **Run the Ansible playbook:**

    ```bash
    ansible-playbook playbook.yml
    ```

## Steps Included

1. **Deploy EC2 Instance:**
   - Installs Pulumi and its dependencies.
   - Uses Pulumi to deploy an AWS EC2 instance with specified configurations.

2. **Configure EC2 Instance:**
   - SSH into the deployed instance.
   - Update and upgrade the system packages.
   - Create a new user and add to the sudo group.
   - Disable the root user and password authentication.
   - Install git, curl, wget, docker, and docker-compose.
   - Add the new user to the docker group and ensure the Docker service is running.

## Contributing

Feel free to submit issues, fork the repository and send pull requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
