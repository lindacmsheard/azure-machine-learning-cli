targetScope = 'subscription'

param project string = 'demo'
param rgName string = '${project}-${uniqueString(newGuid())}'
param rgLocation string

resource rg 'Microsoft.Resources/resourceGroups@2021-01-01' = {
  name: rgName
  location: rgLocation
}
