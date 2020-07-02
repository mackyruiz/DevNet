#!/usr/bin/env python

import requests
from auth_token import get_token


def main():

    token = get_token()
    api_path = "https://sandboxdnac.cisco.com/dna"
    headers = {"Content-Type": "application/json", "X-Auth-Token": token}

    get_resp = requests.get(
        f"{api_path}/intent/api/v1/network-device", headers=headers
    )
   
   # import json; print(json.dumps(get_resp.json(), indent=2))


    if get_resp.ok:
        for device in get_resp.json()["response"]:
            print(f" ID: {device['id']} IP: {device['managementIpAddress']}")
    else:
        print(f"Device collection failed with code {get_resp.status_code}")
        print(f"Failure body: {get_resp.text}")
if __name__ == "__main__":
    main()

