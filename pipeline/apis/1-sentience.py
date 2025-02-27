#!/usr/bin/env python3
"""documentation"""
import requests


def sentientPlanets():
    """returns list of names of the home planets of all sentient species"""
    url = "https://swapi.dev/api/species/"
    planets = set()

    while url:
        response = requests.get(url)
        if response.status_code != 200:
            return []

        data = response.json()
        for species in data["results"]:
            classification = species.get("classification", "").lower()
            designation = species.get("designation", "").lower()

            if "sentient" in (classification, designation):
                homeworld = species.get("homeworld")
                if homeworld:
                    planet_response = requests.get(homeworld)
                    if planet_response.status_code == 200:
                        planet_data = planet_response.json()
                        planets.add(planet_data["name"])

        url = data["next"]

    return list(planets)
