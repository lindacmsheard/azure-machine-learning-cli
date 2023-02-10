# FROM ubuntu:bionic

# # Install python
# RUN apt-get update -qq && \
#  apt-get install -y python3-pip tcl tk libz-dev libpng-dev

# RUN ln -f /usr/bin/python3 /usr/bin/python
# RUN ln -f /usr/bin/pip3 /usr/bin/pip
# RUN pip install -U pip

FROM python:slim

# Install azureml-mlflow
#RUN pip install azureml-mlflow

# Install non-python dependencies
RUN apt-get install -y --no-install-recommends \
    git \
    wget \
#    g++ \
#    gcc \
#    ca-certificates \
    curl \
    gdebi-core \
    && rm -rf /var/lib/apt/lists/*

# Install Miniconda
RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh \
    && echo "Running $(conda --version)" && \
    conda init bash && \
    . /root/.bashrc && \
    conda update conda \
    && echo "Now running $(conda --version)"

RUN curl -LO https://quarto.org/download/latest/quarto-linux-amd64.deb
RUN gdebi --non-interactive quarto-linux-amd64.deb

