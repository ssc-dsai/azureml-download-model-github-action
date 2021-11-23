from azureml.core import Workspace
from azureml.core.authentication import ServicePrincipalAuthentication
from azureml.core.model import Model
import os

# Load .env variables
CONFIG = os.getenv('CONFIG')
MODEL_NAME = os.getenv('MODEL_NAME')
SPN_ID = os.getenv('SPN_ID')
SPN_PWD = os.getenv('SPN_PWD')
TENANT_ID = os.getenv('TENANT_ID')

def main():
    auth = ServicePrincipalAuthentication(
        tenant_id=TENANT_ID, 
        service_principal_id=SPN_ID, 
        service_principal_password=SPN_PWD
    )

    print(CONFIG)

    #ws = Workspace(subscription_id = CONFIG["subscription_id"], resource_group = CONFIG["resource_group"], workspace_name = CONFIG["workspace_name"], auth=auth)

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