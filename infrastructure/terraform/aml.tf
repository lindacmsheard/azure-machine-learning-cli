# provision of aml itself is commented out so we can demonstrate
# how to provision it with the Azure CLI, specifying an existing storage account. 


# # provision dependencies for Azure ML (app insights, key vault, linked storage account)
# resource "azurerm_application_insights" "appin" {
#   name                = "${var.project}${random_integer.deployment.id}-appinsights"
#   location            = azurerm_resource_group.amlrg.location
#   resource_group_name = azurerm_resource_group.amlrg.name
#   application_type    = "web"
# }

# # comment this out if referring to an org-central kv (not advised for inital experiments)
# resource "azurerm_key_vault" "kv" {
#   name                = "${var.project}${random_integer.deployment.id}-kv"
#   location            = azurerm_resource_group.amlrg.location
#   resource_group_name = azurerm_resource_group.amlrg.name
#   tenant_id           = data.azurerm_client_config.current.tenant_id
#   sku_name            = "standard"
# }

# associated storage account 
resource "azurerm_storage_account" "amlstorage" {
  name                     = "${var.project}${random_integer.deployment.id}storage"
  location                 = azurerm_resource_group.amlrg.location
  resource_group_name      = azurerm_resource_group.amlrg.name
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

output "amlstorage" {
    value = azurerm_storage_account.amlstorage.id
}


# # provision AML
# resource "azurerm_machine_learning_workspace" "aml" {
#   name                    = "${var.project}${random_integer.deployment.id}-aml"
#   location                = azurerm_resource_group.amlrg.location
#   resource_group_name     = azurerm_resource_group.amlrg.name
#   application_insights_id = azurerm_application_insights.appin.id
#   key_vault_id            = azurerm_key_vault.kv.id
#   storage_account_id      = azurerm_storage_account.amlstorage.id

#   identity {
#     type = "SystemAssigned"
#   }
# }