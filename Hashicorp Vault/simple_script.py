# import getpass
import hvac
import os
from pprint import pprint

VAULT_ADDR = 'http://127.0.0.1:8200'
# VAULT_TOKEN = getpass.getpass('Hashicorp Vault Token ID: ')
VAULT_TOKEN = os.getenv('VAULT_TOKEN')
# client = hvac.Client()
client = hvac.Client(
url = VAULT_ADDR,
token = VAULT_TOKEN
)

response = client.secrets.kv.read_secret_version(path='ap')

client.secrets.kv.v2.create_or_update_secret(
    path='ap',
    secret=dict(pssst= 'this is secret', client_id='123456789', client_secret= '987654321',repo_token= 'a1b2c3d4e5' ))

pprint(response)

client_id = response['data']['data']['client_id']
client_secret = response['data']['data']['client_secret']
repo_token = response['data']['data']['repo_token']

print("Client ID: " + client_id)
print("Client Secret: " + client_secret)
print("Repo Token: " + repo_token)