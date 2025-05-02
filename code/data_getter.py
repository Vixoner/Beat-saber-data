import requests
import json
import time

def main():
    all_data = []
    for i in range(100):
        url = "https://api.beatleader.xyz/players?sortBy=pp&page=" + str(i+1) + "&count=100&mapsType=ranked&ppType=general&friends=false"
        print(url)
        time.sleep(1)
        response = requests.get(url)
        all_data.append(response.json())

    with open('beatleader_rawdata.json', 'w') as f:
        json.dump(all_data,f)

if __name__ == "__main__":
    main()