# Add Azure ML CLi
# az extension add -n azure-cli-ml

# Add the resource group in the configuration
# az configure --defaults group=$RESOURCE_GROUP

# Get last model
MODEL=$(az ml model list --model-name $MODEL_NAME --workspace-name $WORKSPACE_NAME | jq '.[-1].id')

echo $MODEL