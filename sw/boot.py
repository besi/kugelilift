from network import WLAN, STA_IF
from time import sleep_ms
import secrets
import machine
import utime

enableWIFI = False

if enableWIFI:
    print("Starting WIFI connection")
else:
    print("Wifi is disabled in boot.py")

def try_connection(timeout = 12):

    while not wlan.isconnected() and timeout > 0:
        print('.', end='')
        sleep_ms(500)
        timeout = timeout - 1
    return wlan.isconnected();

wlan = WLAN(STA_IF)
wlan.active(True)

# Only for deep sleep ?
# print('connecting to last AP', end='')
# print(try_connection(3))
if not wlan.isconnected() and enableWIFI:
    ap_list = wlan.scan()
    ## sort APs by signal strength
    ap_list.sort(key=lambda ap: ap[3], reverse=True)
    ## filter only trusted APs
    ap_list = list(filter(lambda ap: ap[0].decode('UTF-8') in
              secrets.wifi.aps.keys(), ap_list))
    for ap in ap_list:
        essid = ap[0].decode('UTF-8')
        if not wlan.isconnected():
            print('connecting to "', essid, end='"')
            wlan.connect(essid, secrets.wifi.aps[essid])
            print(try_connection())


if enableWIFI:
    # Update the time
    from ntptime import settime
    settime()
    utime.sleep_ms(1000)

    import gc
    gc.collect()

    print(wlan.ifconfig()[0])
    import webrepl
    webrepl.start()

