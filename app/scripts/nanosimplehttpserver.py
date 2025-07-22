from network import WLAN, STA_IF
from binascii import hexlify
from time import sleep
import socket

from machine import Pin

led = Pin(15, Pin.OUT)

ssid = 'big boy'
password = 'kappakappa69'

authTypes = {
    0: "OPEN",
    1: "WEP",
    2: "WPA-PSK",
    3: "WPA2-PSK",
    4: "WPA/WPA2-PSK"
}

html = """<!DOCTYPE html>
<html>
    <head> <title>Pico W</title> </head>
    <body> <h1>Pico W</h1>
        <p>%s</p>
    </body>
</html>
"""

wlan = WLAN(STA_IF)
wlan.active(True)

scan_result = wlan.scan()
result = [print('Channel:%d RSSI:%d Auth:%s BSSID:%s SSID:%s' % (ap[2], ap[3], authTypes[ap[4]], hexlify(ap[1], '-').decode('ASCII'), ap[0].decode('ASCII'))) for ap in scan_result if len(scan_result) > 0]
print('\nConnecting to "%s..."' % ssid)

wlan.connect(ssid, password)
while not wlan.isconnected(): pass
print('Success:\nConnected to "%s"' % ssid)
status = wlan.ifconfig()
print( 'ip = ' + status[0] )

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('Listening on', addr)

# Listen for connections
while True:
    try:
        cl, addr = s.accept()
        print('Client connected from', '%s:%d\n' % addr)
        request = cl.recv(1024).decode('ascii')
        print(request)

        # request = str(request)
        led_on = request.find('/light/on')
        led_off = request.find('/light/off')
        print('\nLed on = %s' + str(led_on))
        print('Led off = %s\n' + str(led_off))

        stateis = ""

        if led_on == 6:
            led.value(1)
            stateis = "LED is ON"
            print(stateis)

        if led_off == 6:
            led.value(0)
            stateis = "LED is OFF"
            print(stateis)

        response = html % stateis

        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()

    except OSError as e:
        print('Connection closed')