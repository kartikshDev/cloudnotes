import subprocess, json, sys

costly = ["Microsoft.Compute/virtualMachines",
          "Microsoft.Network/publicIPAddresses",
          "Microsoft.Storage/storageAccounts",
          "Microsoft.Compute/disks"]

out = subprocess.run(["az", "resource", "list", "-o", "json"],
                     capture_output=True, text=True)
resources = json.loads(out.stdout)

found = 0
for r in resources:
    if r["type"] in costly:
        print("COSTS MONEY:", r["name"], "-", r["type"], "in", r["resourceGroup"])
        found += 1

print("Total resources:", len(resources), "| Costly:", found)

if found > 0:
    sys.exit(1)