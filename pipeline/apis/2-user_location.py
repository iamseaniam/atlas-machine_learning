#!/usr/bin/env python3
"""documentation"""
import requests
import sys
import time


def get_user_location(api_url):
    """Documentation"""
    response = requests.get(api_url)

    if response.status_code == 403:
        reset_time = int(response.headers.get(
            "X-RateLimit-Reset", time.time()))
        minutes_remaining = max(0, (reset_time - time.time()) // 60)
        print(f"Reset in {int(minutes_remaining)} min")
    elif response.status_code == 404:
        print("Not found")
    elif response.status_code == 200:
        user_data = response.json()
        print(user_data.get("location", "Location not available"))
    else:
        print("Error fetching user data")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-user_location.py <GitHub API URL>")
    else:
        get_user_location(sys.argv[1])
