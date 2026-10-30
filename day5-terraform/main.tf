resource "azurerm_resource_group" "rg" {
  name     = "day5-rg"
  location = var.location
  tags     = var.tags
}

resource "azurerm_virtual_network" "vnet" {
  name                = "day5-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = var.location
  resource_group_name = azurerm_resource_group.rg.name
}

resource "azurerm_subnet" "subnets" {
  for_each             = { web = "10.0.1.0/24", app = "10.0.2.0/24", db = "10.0.3.0/24", test = "10.0.4.0/24"}
  name                 = each.key
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = [each.value]
}