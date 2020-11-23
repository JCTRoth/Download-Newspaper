#! /bin/bash

# Install Python Libs.
pip3 install --upgrade pip
python3 -m pip install json http.client mimetypes telegram-upload
printf "Use Sudo if Installation fails."