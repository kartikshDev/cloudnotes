variable "subscription_id" {
  type = string
}

variable "location" {
  type    = string
  default = "canadacentral"
}

variable "prefix" {
  type    = string
  default = "day4"
}

variable "my_ip" {
  type = string
}

variable "vm_size" {
  type    = string
  default = "Standard_B2ats_v2"
}

variable "tags" {
  type = map(string)
  default = {
    owner = "kartik"
    env   = "lab"
  }
}

