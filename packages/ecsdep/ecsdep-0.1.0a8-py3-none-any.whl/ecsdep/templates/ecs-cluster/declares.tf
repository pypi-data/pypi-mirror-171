terraform {
  required_version = ">= 1.1.2"
  backend "s3" {
    bucket  = "states-data"
    key     = "terraform/ecs-cluster/dangolchain-cluster/terraform.tfstate"
    region  = "ap-northeast-2"
    encrypt = true
    acl     = "bucket-owner-full-control"
  }
}

provider "aws" {
  region  = "ap-northeast-2"
}

variable "cluster_name" {
  default = "dangolchain-cluster"
}

variable "instance_type" {
  default = "t3.large"
}

variable "ami" {
  default = "amzn2-ami-ecs-hvm-*-x86_64-*"
}

variable "cors_hosts" {
  default = []
}

variable "cert_name" {
  default = "sns.co.kr"
}

variable "public_key_file" {
  default = "/app/dangolchain/dangolchain-daemon/dep/public-key.pem"
}

variable "autoscale" {
  default = {
    desired = 1
    min = 1
    max = 4
    cpu = 70
    memory = 70
  }
}

variable "az_count" {
  default = 2
}