import requests
import json

results_list = []
x= 1
with open("lukket.txt", "r") as i:
    for line in i:
        if "4, Src:" in line:
            gangster = line[34:-1]
            if ", Dst:" in gangster:
                sick = gangster[22:]
                print(sick)  # Print the IP for debugging purposes

                # Make the API request
                api_key = "a904663f1e2a4f96932c1473b5083eb0"
                url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={sick}"
                res = requests.get(url)

                if res.status_code == 200:
                    req = res.json()
                    results_list.append({
                        "ip": sick,
                        "lat": req.get("latitude"),
                        "long": req.get("longitude"),
                        "cont": req.get("country_name"),
                        "city": req.get("city")
                    })
                    x=x+1

# Store the results in a JSON file
with open("porter.json", "w") as x:
    json.dump(results_list, x, indent=1)