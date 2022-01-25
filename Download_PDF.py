import requests
from Tools import *


class Download_PDF:

    def run(i_url, i_cookie, i_pdf_endpoint):

        # Construct Endpoint
        # pdf_file = Tools.get_date_string() + i_pdf_endpoint

        # Example:
        # https://e-paper-reader.bergstraesser-anzeiger.de/bergstraesseranzeiger/931/fullpdf/
        https_url = "https://" + i_url + "/ePaper2/archive/" + pdf_file

        # https_url = "https://" + i_url + "/ePaper2/archive/" + pdf_file

        headers = {
            'Host': i_url,
            'Cookie': i_cookie,
        }

        # Fire Request
        res = requests.request("GET", url=https_url,
                               data=None, headers=headers)
        data = res.content

        # Write Request Return to File
        with open("./" + pdf_file, 'wb') as f:
            f.write(data)
