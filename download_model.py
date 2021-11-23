from azureml.core import Workspace
from azureml.core.authentication import ServicePrincipalAuthentication
from azureml.core.model import Model
import os

# Load .env variables
MODEL_NAME = os.getenv('MODEL_NAME')
RESOURCE_GROUP = os.getenv('RESOURCE_GROUP')
SPN_ID = os.getenv('SPN_ID')
SPN_PWD = os.getenv('SPN_PWD')
SUBS_ID = os.getenv('SUBS_ID')
TENANT_ID = os.getenv('TENANT_ID')
WORKSPACE_NAME = os.getenv('WORKSPACE_NAME')

def main():
    auth = ServicePrincipalAuthentication(
        tenant_id=TENANT_ID, 
        service_principal_id=SPN_ID, 
        service_principal_password=SPN_PWD
    )

    ws = Workspace(subscription_id = SUBS_ID, resource_group = RESOURCE_GROUP, workspace_name = WORKSPACE_NAME, auth=auth)

    # ws = Workspace.from_config(path='config.json', auth=auth)

    #model = Model(ws, name=MODEL_NAME)

    # print('Model found. Downloading (this may take a while...)')
    # model.download(target_dir='.', exist_ok=True)

    # # Rename the retrieved file to the path expected by API
    # model_path = Model.get_model_path(model_name=MODEL_NAME, _workspace=ws)
    # print('Success. Model downloaded to:')
    # print(model_path)
    # os.rename(model_path, 'api/trained_model.bin')
    # print('Model moved to api/trained_model.bin')


if __name__ == "__main__":
    main()