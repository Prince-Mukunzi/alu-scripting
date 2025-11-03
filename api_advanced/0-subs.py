#!/usr/bin/python3
"""
This Script returns the number of subscribers for a given subreddit
"""
import requests
import sys

def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ALU-Reddit-Task/0.2"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        return 0

    try:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except Exception:
        return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./script_name.py <subreddit>")
    else:
        subreddit = sys.argv[1]
        print(number_of_subscribers(subreddit))

