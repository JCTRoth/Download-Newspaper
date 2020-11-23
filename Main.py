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

Download_PDF.run(url, cookie, boundary, pdf_endpoint)

upload_command = Tools.get_telegram_upload_command(
    "https://t.me/joinchat/XXXXXXXX", Tools.get_date_string() + pdf_endpoint)

pdf_path = "./" + Tools.get_date_string() + pdf_endpoint
print(pdf_path)
upload_command = Tools.get_telegram_upload_command(
    "https://t.me/joinchat/CNZubhsRKo0M81i-6Xko4w", pdf_path)

# Uploads PDF
upload_return = os.system(upload_command)
print("Uploaded returned: " + str(upload_return))
