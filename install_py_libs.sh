#! /bin/sh

# Install Python Libs.
apt install python3 python3-pip python3-pycurl
pip3 install --upgrade pip
python3 -m pip install --no-cache-dir http.client telegram-upload pycurl requests