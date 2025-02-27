#!/usr/bin/env python3
"""documentation"""
import requests


def availableShips(passengerCount):
    """returns lists of ships"""
    url = "https://swapi.dev/api/starships/"
    ships = []

    while url:
        response = requests.get(url)
        if response.status_code != 200:
            return []

        data = response.json()
        for ship in data["results"]:
            try:
                capacity = ship["passengers"].replace(
                    ",", "")
                if capacity.isdigit() and int(capacity) >= passengerCount:
                    ships.append(ship["name"])
            except (KeyError, ValueError):
                continue

        url = data["next"]

    return ships
