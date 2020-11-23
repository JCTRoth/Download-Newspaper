import time


class Tools:

    def get_date_string():
        # e.g. 20201116
        return time.strftime("%Y%m%d")

    def get_telegram_upload_command(group_url, file_path):
        return "telegram-upload --to " + group_url + " " + file_path
