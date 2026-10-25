#!/bin/bash
RG=rg-day2
LOC=canadacentral
MYIP=$(curl -4 -s ifconfig.me)
echo $MYIP
az group create -n $RG -l $LOC
az network vnet create -g $RG -n vnet-day2 --address-prefix 10.0.0.0/16 --subnet-name snet-web --subnet-prefix 10.0.1.0/24

#172.219.75.37
az network nsg create -g $RG -n nsg-web
az network nsg rule create -g $RG --nsg-name nsg-web -n allow-http --priority 100 --source-address-prefixes $MYIP --source-port-ranges '*'
az network nsg rule create -g $RG --nsg-name nsg-web -n allow-ssh --priority 110 --source-address-prefixes $MYIP --source-port-ranges '*' --destination-port-ranges 22 --access Allow --protocol Tcp
az network nsg rule list -g rg-day2  --nsg-name nsg-web -o table
az vm create -g $RG -n vm-web --image Ubuntu2204 --size Standard_F2als_v6 \
  --admin-username vmadmin --generate-ssh-keys \
  --vnet-name vnet-day2 --subnet snet-web --nsg "" \
  --custom-data cloud-init.yaml --public-ip-sku Standard

