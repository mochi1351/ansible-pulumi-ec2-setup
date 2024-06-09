import pulumi
import pulumi_aws as aws

config = pulumi.Config('aws')
region = config.require('region')

ami = aws.ec2.get_ami(
    most_recent=True,
    owners=["099720109477"], 
    filters=[{"name": "name", "values": ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]}]
)

security_group = aws.ec2.SecurityGroup('instance-sg',
    description='Enable SSH, HTTP, HTTPS, TCP, and UDP access',
    ingress=[
        {'protocol': 'tcp', 'from_port': 22, 'to_port': 22, 'cidr_blocks': ['0.0.0.0/0']},   
        {'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0']},   
        {'protocol': 'tcp', 'from_port': 443, 'to_port': 443, 'cidr_blocks': ['0.0.0.0/0']}, 
        {'protocol': 'tcp', 'from_port': 0, 'to_port': 65535, 'cidr_blocks': ['0.0.0.0/0']}, 
        {'protocol': 'udp', 'from_port': 0, 'to_port': 65535, 'cidr_blocks': ['0.0.0.0/0']}, 
    ]
)

key_pair = aws.ec2.KeyPair('my-keypair',
    public_key=config.require('ssh_public_key')
)

instance = aws.ec2.Instance('my-instance',
    instance_type=config.require('instance_type'),
    ami=ami.id,
    key_name=key_pair.key_name,
    security_groups=[security_group.name],
    root_block_device={
        'volume_size': config.require_int('volume_size'),
    },
    tags={
        'Name': 'my-instance',
    }
)

pulumi.export('instance_public_dns', instance.public_dns)
