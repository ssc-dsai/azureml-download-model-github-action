# Get latest model
MODEL=$(az ml model list --model-name $MODEL_NAME --workspace-name $WORKSPACE_NAME | jq '.[-1].id')

echo $MODEL