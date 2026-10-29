#!/bin/bash
set -euo pipefail

terraform init -input=false
terraform fmt -check
terraform validate
terraform plan -out tfplan

read -p "Apply? (yes/no) " ans
if [[ "$ans" == "yes" ]]; then
  terraform apply tfplan
  terraform output url
else
  echo "Cancelled."
fi