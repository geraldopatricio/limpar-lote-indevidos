from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os
 
class Safebox():
    @staticmethod
    def get_secret(key):
        try:
            vaulturi = f"https://rundeck-prod.vault.azure.net/"
            credential = DefaultAzureCredential()
            client = SecretClient(vault_url=vaulturi, credential=credential)
            return client.get_secret(key).value
        except:
            print("Chave não encontrada no ENV: ", key)
            return None
