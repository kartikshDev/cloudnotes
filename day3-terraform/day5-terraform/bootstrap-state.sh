set -euo pipefail

RG="tfstate-rg"
LOCATION="canadacentral"
SA="stkartikf$RANDOM"
SKU="Standard_LRS"
CONTAINER="tfstate"
az group create -n $RG -l $LOCATION --tags owner=kartik env=lab
az stroage account create -n $SA -g $RG -l $LOCATION --sku $SKU
az storage container create -n $CONTAINER --account-name $SA --auth-mode login
echo "Storage account : $SA"
