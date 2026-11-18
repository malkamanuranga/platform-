variable "project" {
  type    = string
  default = "platform"
}

variable "region" {
  type    = string
  default = "us-east-1"
}

variable "account_id" {
  type        = string
  description = "AWS account ID, keeps the bucket name globally unique"
}
