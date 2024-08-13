#!/usr/bin/python3
"""
Task 0. How many subs?
"""

from requests import get, RequestException
from sys import argv


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    # Set the URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set up headers to include a custom User-Agent
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        # Make the request to the Reddit API
        response = get(url, headers=headers, allow_redirects=False)

        # Check if the response status code indicates success
        if response.status_code == 200:
            # Parse the JSON data
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # If status code is not 200, return 0
            return 0
    except RequestException:
        # In case of a request exception, return 0
        return 0


if __name__ == '__main__':
    if len(argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))