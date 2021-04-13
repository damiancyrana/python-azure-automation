# New azure-identity authentication mechanism (old version used ServicePrincipalCredentials)
from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient
from msrestazure.azure_exceptions import CloudError

# Variables to get logging parameters
subscription_ID = input("Enter Subscription ID: ")
tenant_ID = input("Enter Tenant ID: ") # ID of the service principal’s tenant. Also called its ‘directory’ ID
client_ID = input("Enter Client ID: ") # The service principal’s client ID
client_secret = input("Enter Client Secret: ") # One of the service principal’s client secrets


def get_virtual_machines():
    """List all Virtual Machines"""
    all_virtual_machines = compute_client.virtual_machines.list_all()

    for virtual_machine in all_virtual_machines:
        print(f"Available virtual machines --> {virtual_machine.name}")


get_virtual_machines()
