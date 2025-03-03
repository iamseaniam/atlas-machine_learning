#!/usr/bin/env python3
"""documentation"""
import requests
from collections import defaultdict


def get_launches_per_rocket():
    """Documentation"""
    url = "https://api.spacexdata.com/v4/launches"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data from SpaceX API")
        return

    launches = response.json()
    rocket_count = defaultdict(int)

    for launch in launches:
        rocket_id = launch.get("rocket", "")
        rocket_count[rocket_id] += 1

    rocket_names = {}
    rockets_response = requests.get("https://api.spacexdata.com/v4/rockets")
    if rockets_response.status_code == 200:
        for rocket in rockets_response.json():
            rocket_names[rocket["id"]] = rocket["name"]

    rocket_launch_list = [(rocket_names.get(rid, "Unknown Rocket"), count)
                          for rid, count in rocket_count.items()]

    rocket_launch_list.sort(key=lambda x: (-x[1], x[0]))

    for rocket_name, count in rocket_launch_list:
        print(f"{rocket_name}: {count}")


if __name__ == "__main__":
    get_launches_per_rocket()
# test
