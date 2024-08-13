#!/usr/bin/python3
"""
Task 2. Recurse it!
"""

import requests
import sys


def recurse(subreddit, hot_list=[], after=None):
    """Recursively retrieves all hot article titles for a given subreddit."""
    # Set the base URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set up parameters for pagination
    params = {"limit": 100}
    if after:
        params["after"] = after

    # Set up headers to include a custom User-Agent
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        # Make the request to the Reddit API
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        # Check if the response status code indicates success
        if response.status_code == 200:
            # Parse the JSON data
            data = response.json()

            # Extract titles and add them to the hot_list
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])

            # Check if there is another page (pagination)
            after = data['data']['after']
            if after:
                # Recursively call the function to get the next page
                return recurse(subreddit, hot_list, after)
            else:
                # If no more pages, return the full list of titles
                return hot_list
        else:
            # If status code is not 200, return None
            return None
    except requests.RequestException:
        # In case of a request exception, return None
        return None


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")