FROM ubuntu:bionic

RUN apt-get update & apt-get upgrade
RUN apt-get install gnupg2

RUN apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
RUN echo "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64 /" | tee /etc/apt/sources.list.d/cuda.list

RUN apt-get update 
RUN apt-get -o Dpkg::Options::="--force-overwrite" install cuda-10-0 cuda-drivers