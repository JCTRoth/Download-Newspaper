# Python Docker Official Image
FROM python:3.8-alpine

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Needed for the pycurl compilation
ENV PYCURL_SSL_LIBRARY=openssl

# Add Packages Needed
RUN apk add -u --no-cache libcurl libstdc++ \
    && apk add -u --no-cache --virtual .build-deps build-base libffi-dev curl-dev \
    && rm -rf /var/cache/apk/*

# Copy Config Files to the container
WORKDIR /app
ADD . /app

COPY telegram-upload.session /app

# Install pip requirements
ADD install_py_libs.sh .
RUN ./install_py_libs.sh

# Switching to a non-root user
RUN addgroup -S app && adduser -S -G app app

# Run program
RUN cd /app
CMD ["python", "Main.py"]
