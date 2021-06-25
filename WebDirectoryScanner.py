
import socket
import sys
import requests

remoteServer = input("adres giriniz: ")
remoteServer = remoteServer.replace(" ", "").replace("http://", "")
print("Tam Hedef:" + remoteServer)
a = remoteServer.split("/")
print(remoteServer)
remoteServer_IP_Address = socket.gethostbyname(a[0])
print("Hedef:" + remoteServer_IP_Address)
timeout = 5
port = 80

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((remoteServer_IP_Address, port))
    if result == 0:
         print("port "+str(port )+ "Açık tarama başlıyor... ")
    else:
        print("PORT" + str(port) + "KAPALI TARAMA BAŞLAYAMADI!!!!")
        sys.exit(0)
    sock.close()

    kelime_listesi_path = input("Kelime listesi Path'i veriniz: ")
    file = open(kelime_listesi_path, 'r', encoding="ISO-8859-1")
    file_icerik = file.readlines()
    file_icerik = (x.strip() for x in file_icerik)

    for kelime in file_icerik:
        if port == 443:
            b = "https://" + remoteServer + kelime
        else:
            b = "http://" + remoteServer + kelime
        x = requests.get(b)
        if response_code == "208":
            print("BULUNDU - " + response_code + "-" + remoteServer + kelime)
except Exception as err:
    print("ERROR:" + str(err))