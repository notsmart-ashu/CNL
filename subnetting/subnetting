import socket
def get_subnet_mask(ip):
    checkclass = ip.split('.')[0]
    cc = int(checkclass)
    mask = None
    if cc > 0:
        if cc <= 127:
            mask = "255.0.0.0"
            print("Class A IP Address")
            print("SUBNET MASK:\n" + mask)
        if cc >= 128 and cc <= 191:
            mask = "255.255.0.0"
            print("Class B IP Address")
            print("SUBNET MASK:\n" + mask)
        if cc >= 192 and cc <= 223:
            mask = "255.255.255.0"
            print("Class C IP Address")
            print("SUBNET MASK:\n" + mask)
        if cc >= 224 and cc <= 239:
            mask = "255.0.0.0"
            print("Class D IP Address Used for multicasting")
        if cc >= 240 and cc <= 254:
            mask = "255.0.0.0"
            print("Class E IP Address Experimental Use")
    return mask
ip = input("ENTER IP:")
mask = get_subnet_mask(ip)
networkAddr = ""
lastAddr = ""
ipAddrParts = ip.split(".")


# output
# ENTER IP:192.168.10.1
# Class C IP Address
# SUBNET MASK:
# 255.255.255.0
