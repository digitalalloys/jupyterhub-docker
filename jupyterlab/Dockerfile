FROM jupyter/scipy-notebook:d4cbf2f80a2a

USER root

# APT packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    vim \
    nodejs \
    git \
    openssh-client \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Python packages
ADD requirements.txt .
RUN pip install -r requirements.txt

# Jupyter labextensions
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager
RUN jupyter labextension install jupyter-matplotlib
RUN jupyter labextension install ipyvolume
RUN jupyter labextension install jupyter-threejs
RUN jupyter labextension install @jupyterlab/git
RUN jupyter serverextension enable --py jupyterlab_git
RUN jupyter labextension install @lckr/jupyterlab_variableinspector
