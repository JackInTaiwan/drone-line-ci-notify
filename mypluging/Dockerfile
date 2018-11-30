# test
#
#     docker build --rm=true -t jackintaiwan/mypluging .

FROM gliderlabs/alpine:3.2
MAINTAINER jack <jackconvolution@gmail.com>

RUN apk-install python3
RUN mkdir -p /opt/drone
COPY requirements.txt /opt/drone/
WORKDIR /opt/drone
RUN pip3 install -r requirements.txt
COPY plugin /opt/drone/

ENTRYPOINT ["python3", "/opt/drone/plugin/main.py"]
