import requests
import time

key = input("License key: ")

url = "votre pastebin"

r = requests.get(url)

try:
    if key in r.text:
        print("Clé Validé")
        pass
    else:
        print("Clé Invalide")
        time.sleep(30)
        exit()
except:
    print("Erreur!")
    time.sleep(30)
    exit()   