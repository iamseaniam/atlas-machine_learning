#!/usr/bin/env python3
"""documentation"""
import requests
import sys
import time


def get_github_user_location(api_url):
    response = requests.get(api_url)

    if response.status_code == 404:
        print("Not found")
        return

    if response.status_code == 403:
        reset_time = int(response.headers.get(
            "X-RateLimit-Reset", time.time()))
        wait_minutes = (reset_time - time.time()) // 60
        print(f"Reset in {int(wait_minutes)} min")
        return

    if response.status_code == 200:
        user_data = response.json()
        location = user_data.get("location")
        print(location if location else "Location not available")
    else:
        print(f"Error: Received status code {response.status_code}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-user_location.py <GitHub API URL>")
        sys.exit(1)

    api_url = sys.argv[1]
    get_github_user_location(api_url)
