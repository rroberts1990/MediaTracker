FROM ubuntu:latest
LABEL maintainer="rroberts"

COPY . /opt/StockTracker/
WORKDIR /opt/StockTracker/

# Install Python
RUN \
    apt-get update && \
    apt-get install -y python3 python3-pip python3-setuptools python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Install requirements
RUN \
    pip3 install --upgrade pip && \
    pip3 install wheel setuptools && \
    pip3 install -r requirements.txt