import time
from jnius import autoclass

def start_sovereign_tunnel():
    try:
        VpnService = autoclass('android.net.VpnService')
        Builder = autoclass('android.net.VpnService$Builder')
        builder = Builder()
        builder.setSession("Guard_Sovereign_Tunnel")
        builder.addAddress("10.8.0.2", 32)
        builder.addRoute("0.0.0.0", 0)
        builder.addDnsServer("1.1.1.1")
        builder.setMtu(1400)
        interface = builder.establish()
        while True:
            time.sleep(10)
    except: pass

if __name__ == '__main__':
    start_sovereign_tunnel()

