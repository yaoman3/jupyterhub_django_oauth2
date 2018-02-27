import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
from oauthenticator.generic import GenericOAuthenticator

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.JupyterHub.authenticator_class = GenericOAuthenticator

from jupyter_client.localinterfaces import public_ips
c.JupyterHub.hub_ip = public_ips()[0]

client_id = open(os.environ['OAUTH_CLIENT_ID_PATH']).read().strip()
client_secret = open(os.environ['OAUTH_CLIENT_SECRET_PATH']).read().strip()
c.GenericOAuthenticator.client_id = client_id
c.GenericOAuthenticator.client_secret = client_secret
logger.debug("ID: " + client_id)
logger.debug("SECRET: " + client_secret)

# c.JupyterHub.ip = '0.0.0.0'
