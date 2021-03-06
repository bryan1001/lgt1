FROM ubuntu:xenial

# Ensure non-interactive mode
ENV DEBIAN_FRONTEND noninteractive

# Add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi

ENV PYTHONUNBUFFERED 1
ENV CODE_DIR /var/code

## START: GOSU
ENV GOSU_VERSION 1.10
ENV TF_BINARY_URL https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.11.0rc2-cp27-none-linux_x86_64.whl

RUN set -x \
    && apt-get update && apt-get install -y --no-install-recommends ca-certificates wget && rm -rf /var/lib/apt/lists/* \
    && dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \
    && wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch" \
    && wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc" \
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
    && rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu \
    && gosu nobody true \
    && apt-get purge -y --auto-remove ca-certificates wget

## END: GOSU

RUN mkdir ${CODE_DIR} && mkdir ${CODE_DIR}/instance && chown -R uwsgi:uwsgi ${CODE_DIR}
WORKDIR ${CODE_DIR}

ADD requirements.txt ${CODE_DIR}/requirements.txt

RUN BUILD_DEPS='gcc python-pip' \
    && apt-get update \
    && apt-get install -y --no-install-recommends python-dev libmysqlclient-dev $BUILD_DEPS \
    && pip install --upgrade pip \
    && pip install setuptools==28.3.0 \
    && pip install uwsgi==2.0.14 \
    && pip install -r requirements.txt \
    && pip install --upgrade $TF_BINARY_URL \
    && apt-get purge -y --auto-remove $BUILD_DEPS \
    && rm -rf /var/lib/apt/lists/*

ADD . ${CODE_DIR}

# CMD ["app.py"]
