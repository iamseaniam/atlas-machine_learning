#!/usr/bin/env python3
"""documentation"""
import requests
import datetime


def get_first_spacex_launch():
    """Documentation"""
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data from SpaceX API")
        return

    launches = response.json()
    if not launches:
        print("No upcoming launches found")
        return

    launches.sort(key=lambda x: x.get("date_unix", float('inf')))
    first_launch = launches[0]

    launch_name = first_launch.get("name", "Unknown Launch")
    date_unix = first_launch.get("date_unix", 0)
    date_local = datetime.datetime.fromtimestamp(
        date_unix).strftime("%Y-%m-%d %H:%M:%S")
    rocket_id = first_launch.get("rocket", "")
    launchpad_id = first_launch.get("launchpad", "")

    rocket_response = requests.get(
        f"https://api.spacexdata.com/v4/rockets/{rocket_id}")
    rocket_name = rocket_response.json().get(
        "name", "Unknown Rocket") if rocket_response.status_code == 200 else "Unknown Rocket"

    launchpad_response = requests.get(
        f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}")
    if launchpad_response.status_code == 200:
        launchpad_data = launchpad_response.json()
        launchpad_name = launchpad_data.get("name", "Unknown Launchpad")
        launchpad_locality = launchpad_data.get("locality", "Unknown Locality")
    else:
        launchpad_name, launchpad_locality = "Unknown Launchpad", "Unknown Locality"

    print(f"{launch_name} ({date_local}) {rocket_name} - {launchpad_name} ({launchpad_locality})")


if __name__ == "__main__":
    get_first_spacex_launch()
