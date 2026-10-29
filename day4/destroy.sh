#!/bin/bash
set -euo pipefail
terraform destroy -auto-approve
az group list -o table