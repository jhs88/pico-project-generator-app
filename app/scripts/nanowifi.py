from network import WLAN, STA_IF
from binascii import hexlify
from time import sleep_ms

authTypes = {
    0: "OPEN",
    1: "WEP",
    2: "WPA-PSK",
    3: "WPA2-PSK",
    4: "WPA/WPA2-PSK"
}

wlan = WLAN(STA_IF)
wlan.active(True)

print("Scanning...")
while (True):
    scan_result = wlan.scan()
    result = [print("Channel:%d RSSI:%d Auth:%s BSSID:%s SSID:%s"%(ap[2], ap[3], authTypes[ap[4]], hexlify(ap[1], '-').decode('ASCII'), ap[0].decode('ASCII'))) for ap in scan_result if len(scan_result) > 0]
    print()
    sleep_ms(1000)