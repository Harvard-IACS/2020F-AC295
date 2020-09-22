FROM ubuntu:latest

RUN apt update -y
RUN apt install -y python3-pip
#RUN apt-get install graphviz
RUN python3 -m pip install jupyterlab
RUN python3 -m pip install "dask[complete]"
RUN python3 -m pip install graphviz

COPY . .

EXPOSE 9999


CMD ["/bin/sh"]