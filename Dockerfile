FROM ubuntu:latest
LABEL maintainer="rroberts"

RUN useradd mediatracker

COPY . /home/mediatracker

WORKDIR /home/mediatracker

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


RUN chmod +x boot.sh

RUN chown -R mediatracker:mediatracker ./
USER mediatracker

ENV FLASK_APP=media_tracker.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]