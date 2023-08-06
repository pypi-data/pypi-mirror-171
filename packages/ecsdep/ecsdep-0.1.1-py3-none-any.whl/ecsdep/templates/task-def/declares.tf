terraform {
  required_version = ">= 1.1.2"
  backend "s3" {
    bucket  = "states-data"
    key     = "terraform/ecs-cluster/dangolchain-cluster/task-def/dw-web/terraform.tfstate"
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

# variables -----------------------------------------------
variable "awslog_region" {
  default = "ap-northeast-2"
}

variable "stages" {
  default = {
    default = {
        env_service_stage = "production"
        hosts = ["dangolchain.com"]
        listener_priority = 15
        service_name = "dw-web"
        task_definition_name = "dw-web"
    }
    qa = {
        env_service_stage = "qa"
        hosts = ["qa.dangolchain.com"]
        listener_priority = 25
        service_name = "dw-web--qa"
        task_definition_name = "dw-web--qa"
    }
  }
}

variable "service_auto_scaling" {
  default = {
    desired = 1
    min = 1
    max = 3
    memory = 80
    cpu = 100
  }
}

variable "exposed_container" {
  default = [{
    name = "dangolchain-front"
    port = 80
  }]
}

variable "target_group" {
  default = {
    protocol = "HTTP"
    healthcheck = {
        path = "/ping"
        matcher = "200,304"
        timeout = 10
        interval = 60
        healthy_threshold = 2
        unhealthy_threshold = 10
    }
  }
}

variable "loggings" {
  default = ["dangolchain-front"]
}

variable "loadbalancing_pathes" {
  default = ["/*"]
}

variable "requires_compatibilities" {
  default = ["EC2"]
}

variable "service_resources" {
  default = {
    memory = 0
    cpu = 0
  }
}
