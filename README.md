# GitHub Action To Download a AzureML model

This is a github action that will download a specific model from an Azure Machine Learning workspace. 

Here is a action workflow example to run the notebook. 

```yaml
name: Download AzureML Model GitHub Action Demo 

on:
  push:
    branches: 
      - main
  workflow_dispatch:

jobs:
  train-model: 
    runs-on: ubuntu-latest
    steps:
    - name: Checkout
      uses: actions/checkout@v2

    - name: Download AzureML Model
      uses: SSC-DSAI/azureml-download-model-github-action@main
      with:
        model-name: ${{ secrets.MODEL_NAME }}
        resource-group: ${{ secrets.RESOURCE_GROUP }}
        spn-id: ${{ secrets.SPN_ID}}
        spn-pwd: ${{ secrets.SPN_PWD }}
        subs-id: ${{ secrets.SUBS_ID }}
        tenant-id: ${{ secrets.TENANT_ID}}
        workspace-name: ${{ secrets.WORKSPACE_NAME }}
```
