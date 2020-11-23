
### Run
```sh
crontab -e
```
### Add line
```sh
0 0   *   *   1,2,3,4,5   /YOUR_PATH/Main.py
```

### If you want to change the schedule:
```
*     *     *     *     *  Command
-     -     -     -     -
|     |     |     |     |
|     |     |     |     +----- Weekday (0 - 7) (Sunday is 0 und 7; oder Namen, siehe unten)
|     |     |     +------- Month (1 - 12)
|     |     +--------- Day (1 - 31)
|     +----------- Hour (0 - 23)
+------------- Minute (0 - 59; oder Namen, siehe unten)
```