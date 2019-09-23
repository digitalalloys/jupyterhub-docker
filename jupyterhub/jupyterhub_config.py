## Generic
c.JupyterHub.admin_access = True
c.Spawner.default_url = '/lab'

## Authenticator
from oauthenticator.google import GoogleOAuthenticator
c.JupyterHub.authenticator_class = GoogleOAuthenticator

## Docker spawner
import os
import dockerspawner

admin_email = os.environ.get('ADMIN_EMAIL', None)
if admin_email:
    c.Authenticator.admin_users = {admin_email}

# Remove containers once they are stopped
c.DockerSpawner.remove_containers = True

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_CONTAINER']
network_name = os.environ['DOCKER_NETWORK_NAME']
c.DockerSpawner.network_name = network_name
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.extra_host_config = {'network_mode': network_name}
# See https://github.com/jupyterhub/dockerspawner/blob/master/examples/oauth/jupyterhub_config.py
c.JupyterHub.hub_ip = os.environ['HUB_IP']

# user data persistence
# see https://github.com/jupyterhub/dockerspawner#data-persistence-and-dockerspawner
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.format_volume_name = dockerspawner.volumenamingstrategy.escaped_format_volume_name
c.DockerSpawner.volumes = {
    'jupyterhub-user-{username}': notebook_dir,
    # 'jupyterhub-share': '/home/jovyan/share',
}

print_data_volume = os.environ.get('PRINTS_MEDIA_VOLUME', 'print-data')
print_data_cache_volume = os.environ.get('PRINT_DATA_CACHE_VOLUME', 'print-data-cache')
c.DockerSpawner.read_only_volumes = {
    print_data_volume: '/print-data',
    print_data_cache_volume: '/print-data-cache',
}
# Other stuff
c.Spawner.cpu_limit = int(os.environ.get('CPU_LIMIT', 1))
c.Spawner.mem_limit = os.environ.get('MEM_LIMIT', '10G')


## Services
c.JupyterHub.services = [
    {
        'name': 'cull_idle',
        'admin': True,
        'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
    },
]
