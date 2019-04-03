FROM jupyter/scipy-notebook:8b98bb97bdae

USER root

# APT packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    vim \
    nodejs \
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
