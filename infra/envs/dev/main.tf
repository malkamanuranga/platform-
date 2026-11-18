terraform {
  required_version = ">= 1.6"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

module "vpc" {
  source = "../../modules/vpc"

  name = "platform-${var.environment}"
  cidr = var.vpc_cidr
  azs  = var.azs
  tags = {
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}
