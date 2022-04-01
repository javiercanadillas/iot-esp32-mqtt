# Boot.py file, providing Wifi network connectivity

def get_credentials(filename: str):
    """Get WiFi SSID and password from JSON file"""
    import ujson
    try:
        os.stat(filename)
        with open(filename, 'r') as f:
            credentials = ujson.load(f)
            return(credentials['essid'], credentials['password'])
    except OSError:
        print("Cannot obtain credentials file")
        sys.exit()

def do_connect(essid: str, password: str):
    """Establishes WiFi connectivity"""
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(reconnects=10)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(essid, password)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

essid, password = get_credentials("credentials.json")
do_connect(essid, password)