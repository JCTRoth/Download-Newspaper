import os
import json
from Config import *
from Tools import *
from Download_PDF import *

# Load Config from file
jsonConfig = config()
jsonConfig.read_config_file("config.json")

# Downloads PDF
pdf_endpoint = jsonConfig.config.get("newsletter").get("pdf_endpoint")
url = jsonConfig.config.get("newsletter").get("url")
cookie = jsonConfig.config.get("newsletter").get("cookie_list")
boundary = jsonConfig.config.get("newsletter").get("cookie_list")
telegram_url = jsonConfig.config.get("upload_targets").get("telegram")

Download_PDF.run(url, cookie, boundary, pdf_endpoint)

pdf_path = "./" + Tools.get_date_string() + pdf_endpoint
print("PDF Path: " + pdf_path)

# Check if file is valid
# e.g. on public holiday empty file will be downloaded
size_of_pdf = os.path.getsize(pdf_path)

print("PDF Size: " + str(size_of_pdf) + " byte")

# PDF with Error message in it is about 1101 byte
if size_of_pdf > 100000:
    upload_command = Tools.get_telegram_upload_command(telegram_url, pdf_path)

    # Upload PDF
    upload_return = os.system(upload_command)
    print("Uploaded returned: " + str(upload_return))
else:
    print("No Upload was done")
    # Remove not uploded file
    if os.path.exists(pdf_path):
        os.remove(pdf_path)
