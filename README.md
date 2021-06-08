# Newspaper Down And Up Loader
Each morning this MicroService downloads my newspaper and uploads it to my personal telegram group (single member  group).

![](.ReadMe/Newspaper_Downloader.png "Newspaper Downloader")

If you want to use this program you need a digital subscription of [Morgenweb.de](https://abo-bergstraesser-anzeiger.morgenweb.de/?hnr=paywall])

<br/>

## Setup
- Run install_py_libs as SU or with sudo
- Run Create_Config.js in browser
- Get Telegram Developer Key
- Get Telegram Group URL from Telegram Web
- Run Download_PDF.py for first config 


### Example Conifg
```sh
{
    "newsletter": {
        "url": "digitalezeitung-bergstraesser-anzeiger.morgenweb.de",
        "cookie_list": "xxxxxxxxxx",
        "pdf_endpoint": "_ba-be_0.pdf"
    },
    "upload_targets": {
        "telegram": "https://t.me/joinchat/xxxxxxxxx"
    }
}
```
###
```sh
chmod +x ~/Download-Newspaper/Run_Newspaper_Download.sh
```

### Run
```sh
crontab -e
```
### Add line
```sh
 10 7 * * * sh ~/Download-Newspaper/Run_Newspaper_Download.sh > /dev null 2>&1
```

### If you want another schedule:
```
*     *     *     *     *  Command
-     -     -     -     -
|     |     |     |     |
|     |     |     |     +----- Weekday (0 - 7) (Sunday is 0 and 7)
|     |     |     +------- Month (1 - 12)
|     |     +--------- Day (1 - 31)
|     +----------- Hour (0 - 23)
+------------- Minute (0 - 59)
```