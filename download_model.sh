# Login to Azure with a Service Principal
az login --service-principal -u $SPN_ID -p $SPN_PWD --tenant $TENANT_ID
az extension add -n azure-cli-ml 
az configure --defaults group=$RESOURCE_GROUP

# Get Model ID
LIST=$(az ml model list --model-name $MODEL_NAME --workspace-name $WORKSPACE_NAME)

echo LIST