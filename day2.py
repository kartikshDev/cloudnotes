# def check_port(port):
#     if port in [22, 80, 443]:
#         return "allowed"
#     else:
#         return "blocked"

# print(check_port(22))
# print (check_port(8080))




# def check_size(size):
#     if size in ["Standard_B1s", "Standard_B2s", "Standard_F2als_v6"]:
#         return "Create it boy" 
#     else:
#         return "you will be bankrupt"

# print(check_size("Standard_B1s"))
# print (check_size("Standard_B16s"))
# size = input("size")
# print (check_size(size))


# rule1 = {"name": "allow-ssh", "port": 22, "protocol" : "tcp", "priority":110 , "direction": "inbound", "action": "allow"}
# rule2 = {"name": "allow-http", "port": 80, "protocol" : "any", "priority":100 , "direction": "inbound", "action": "allow"}
# rules = [rule1, rule2]
# for rule in rules:
#     for key, value in rule.items():
#         print(key, value)

st_type1 = {'name': 'stdata', 'type': 'StorageV2', 'location': 'eastus', 'tier': 'hot'}
st_type2 = {'name': 'kv-data' , 'type' : 'KeyVault', 'sku' : "standard"}

rg_data = {"name": "rg-data", "resources": [st_type1, st_type2]}

vm_1 = {'name': 'vm-web', 'type': 'VM', 'size': 'Standard_B1s'}
vnet_1 = {'name': 'vnet-web', 'type': 'VNet', 'address_space': "10.0.0.0/16"}

rg_web = {"name": "rg-web", "resources": [vm_1, vnet_1]}

sub = [rg_web, rg_data]

for rg in sub:
    print(f"Resource Group: {rg['name']}")
    for resource in rg['resources']:
        print(f"  Resource Name: {resource['name']}, Type: {resource['type']}") 
        for key, value in resource.items():
          print("        ", key, "=", value)