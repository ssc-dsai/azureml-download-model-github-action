# Add Azure ML CLi
az extension add -n azure-cli-ml

# Add the resource group in the configuration
az configure --defaults group=$RESOURCE_GROUP

# Login to Azure with a Service Principal
az login --service-principal -u $SPN_ID -p $SPN_PWD --tenant $TENANT_ID


# Get last model
MODEL=$(az ml model list --model-name $MODEL_NAME --workspace-name $WORKSPACE_NAME | jq '.[-1].id')

echo $MODEL