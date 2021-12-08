terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "2.60.0"
    }
    random = {
      source = "hashicorp/random"
    }
  }

  # keeping a local backend. Uncomment to configure a remote backend in azure storage. Requires existing storage account 
  # outside of this infrastructure specifification
  #backend "azurerm" {
    #resource_group_name   = "utils"
    #storage_account_name  = "utilstorage"
    #container_name        = "terraform"
    #key                   = "my.project.tfstate"    # specify this on command line when running terraform init -backend=true (will prompt for key)
  #}
}

provider "azurerm" {
  
  # comment out these lines if authenticating via user/device login, e.g. if working in the cloud shell or with az login
  #subscription_id = "***************fcce"
  #client_id       = "***************eslf"
  #client_secret   = var.client_secret
  #tenant_id       = "***************db47"
  
  features {}
}

data "azurerm_client_config" "current" {}

variable "project" {
  type = string
  default = "demo"
}

variable "location" {
  type = string
  default = "uksouth"
}

resource "random_integer" "deployment" {
  min = 101
  max = 999
}

resource "azurerm_resource_group" "amlrg" {
  name     = "${var.project}${random_integer.deployment.id}"
  location = "uksouth"
  tags = {
    managed = "tf"
    audience = "bootcamp"
    purpose = "demo"
  }
}

output "rg" {
  value = azurerm_resource_group.amlrg.name
}

