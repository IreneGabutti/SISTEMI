import subprocess

ipaddress = "192.160.10.0"
mask = 30

ipaddress_splitted = [int(i) for i in ipaddress.split(".")]

ipaddress_bin = 0
for e, group in enumerate(ipaddress_splitted):
    ipaddress_bin = ipaddress_bin + group*(2**(((3-e)*8)))

ipaddress_host = ipaddress_bin
for c in range(1,2**(32-mask)-1):
    ipaddress_host = ipaddress_host + 1
    l = '.'.join([str(int(bin(ipaddress_host)[i:i+8],2)) for i in range(2,34,8)])
    #print(l)
    p = subprocess.Popen(['ping', ipaddress], stdout=subprocess.PIPE) 
    ping = p.communicate()                                              

    if (ping[0].decode().count('Tempo approssimativo') > 0):
        print(f"Host {l} è attivo")
    else:
        print(f"Host {l} è inattivo")
