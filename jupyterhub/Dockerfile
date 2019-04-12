FROM jupyterhub/jupyterhub:0.9.4

RUN apt-get install -y git openssh-client

WORKDIR /app

COPY jupyterhub_config.py .

RUN wget https://raw.githubusercontent.com/jupyterhub/jupyterhub/0.9.4/examples/cull-idle/cull_idle_servers.py

RUN pip install \
    dockerspawner==0.10.0 \
    oauthenticator==0.8.0
