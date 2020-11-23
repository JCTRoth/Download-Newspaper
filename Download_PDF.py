import http.client
import mimetypes
from Tools import *


class Download_PDF:

    def run(i_url, i_cookie, i_boundary, i_pdf_endpoint):

        conn = http.client.HTTPSConnection(i_url)

        boundary = i_boundary

        headers = {
            'Host': i_url,
            'Cookie': i_cookie,
            'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
        }

        # Construct Endpoint
        pdf_file = "./" + Tools.get_date_string() + i_pdf_endpoint

        # Fire Request
        conn.request("GET", "/ePaper2/archive/" + pdf_file, None, headers)
        res = conn.getresponse()
        data = res.read()

        # Write Request Return to File
        with open(pdf_file, 'wb') as f:
            f.write(data)
