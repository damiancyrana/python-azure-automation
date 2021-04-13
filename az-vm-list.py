# New azure-identity authentication mechanism (old version used ServicePrincipalCredentials)
from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient
from msrestazure.azure_exceptions import CloudError
import traceback  # Module to print exception information

# Variables to get logging parameters
subscription_ID = input("Enter Subscription ID: ")
tenant_ID = input("Enter Tenant ID: ")  # ID of the service principal’s tenant. Also called its ‘directory’ ID
client_ID = input("Enter Client ID: ")  # The service principal’s client ID
client_secret = input("Enter Client Secret: ")  # One of the service principal’s client secrets

# Service principal with secret and error handling (alternative approach Service principal with certificate)
try:
    credentials = ClientSecretCredential(
        tenant_id=tenant_ID,
        client_id=client_ID,
        client_secret=client_secret
    )

    compute_client = ComputeManagementClient(
        credential=credentials,
        subscription_id=subscription_ID
    )
# Examples of error handling
except CloudError as cloudError:
    if cloudError.status_code == 404:
        print("Page not found")
    elif cloudError.status_code != 404:
        print(f"Failed to retrieve server azure AD admin {cloudError.status_code}")
    else:
        print(f"A operation failed ---> {traceback.format_exc()}")
# Default message if no error is reported
else:
    print("All operations completed successfully!")


def get_virtual_machines():
    """List all Virtual Machines"""
    all_virtual_machines = compute_client.virtual_machines.list_all()

    for virtual_machine in all_virtual_machines:
        print(f"Available virtual machines --> {virtual_machine.name}")


get_virtual_machines()
