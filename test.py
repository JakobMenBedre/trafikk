from pythonping import ping 
import requests
import json
import sys
import time
ip = "ip"
lat = "latitude"
long = "longitude"
cont="country_name"
city="city"
original_stdout = sys.stdout
results = {}
results_list = []
broderhvafaen = 1
nummer_sent = 0


with open ("lukket.txt", "r") as i: #åpner lukket.txt som "i"
    for line in i: #for hver linje i "i" så kjører den de neste linjene med "i", som en variabel som inneholder linjen.
        
        if "4, Src:" in line: #leter etter "4, Src:" i linjen 
            gangster=(line[34:-1]) # hvis den finner det lagrer den det etter kolonne 34 i linje i en variabel som heter gangster.
            
            if ", Dst:" in gangster: #gjør det samme fsom den over men den leter etter ", Dst" i gangster
                sick = (gangster[22:-1]) #og så helt til slutt leter tar den bare det som er etter kolonne 22 i gangster og printer det
                print(sick)

                key = "6a5c5d5ae8a9421784a51e19fe8441aa" #keyen som brukes i res
                res = f"https://api.ipgeolocation.io/ipgeo?apiKey={key}&ip={sick}" # tar ip og key og bruker api.
                req = requests.get(res) #henter api i ny form
                requa = req.json() #tar den nye formen og gjør den 
                # ipagang = sick
                # for ipagang in requa:
                #     nummer_sent=nummer_sent+1
                #     print(nummer_sent)
                if req.status_code == 200:
                    results = {
                        "id": broderhvafaen,
                        "ip": sick,
                        "lat": requa["latitude"],
                        "long": requa["longitude"],
                        "cont": requa["country_name"],
                        "city": requa["city"],
                        "organ": requa["organization"],
                        "antall": nummer_sent
                    }
                    # lager dict med id, ip, latidue, longitude, navnet på landet signalet er sendt fra, byen i landet, og organisasjonen
                    broderhvafaen=broderhvafaen+1 #broderhvafaen er bare id-en til hver av arrayene i "porter.json"
                    results_list.append(results) #tar dataen i results og lagrer det som en table i results_list
with open ("porter.json", "w") as x: 
    json.dump(results_list, x, indent=1) #åpner porter.json i write som x og "dump"-er inn verdiene til "results_list".
