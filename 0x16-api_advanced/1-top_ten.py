#!/usr/bin/python3
"""
Task 1. Top Ten
"""

import requests
import sys


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    # Set the URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set up headers to include a custom User-Agent
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        # Make the request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the response status code indicates success
        if response.status_code == 200:
            # Parse the JSON data
            data = response.json()
            # Extract and print the titles of the first 10 hot posts
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            # If status code is not 200, print None
            print(None)
    except requests.RequestException:
        # In case of a request exception, print None
        print(None)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])