FROM python:3.9.5-alpine
LABEL maintainer="Leandro de Souza Batista <linux.leandrosb@gmail.com>" 

WORKDIR /usr/src/app

RUN apk add --virtual .build-dependencies \
            --no-cache \
            python3-dev \
            build-base \
            linux-headers \
            pcre-dev
RUN pip install Flask==1.1.2 && \
    apk add --no-cache pcre

COPY modeloapi.py .

RUN apk del .build-dependencies && rm -rf /var/cache/apk/*
EXPOSE 5000

CMD [ "python", "./modeloapi.py" ]
