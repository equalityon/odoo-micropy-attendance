def check_and_install_urequests():
    import os
    if ('urequests.py' not in os.listdir('lib')):
        import upip 
        upip.install('micropython-urequests')

def clean_boot():
    # Empty and soft reboot
    f = open('boot.py')
    f.write('\n')
    import sys
    sys.exit()

# Connect to some nextor stored on wifi_networks file
def do_connect():
    import network
    from wifi_networks import networks_availables
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        available_net = wlan.scan()
        for net in available_net:
            net_str = net[0].decode('utf-8')
            if (net_str in networks_availables):
                wlan.connect(net_str, networks_availables[net_str])
        while not wlan.isconnected():
            pass
