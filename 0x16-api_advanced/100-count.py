#!/usr/bin/python3
"""
Task 3. Count it!
"""

from collections import Counter
import requests
import re
import sys


def count_words(subreddit, word_list, hot_list=[], after=None):
    """
    Counts occurrences of keywords in hot article titles from a subreddit.
    """
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
                return count_words(subreddit, word_list, hot_list, after)
            else:
                # Once all data is collected, process the word counts
                word_count = Counter()
                lower_word_list = [word.lower() for word in word_list]

                for title in hot_list:
                    # Tokenize title into words and normalize case
                    words = re.findall(r'\b\w+\b', title.lower())
                    for word in words:
                        if word in lower_word_list:
                            word_count[word] += 1

                # Sort the results by count (descending) and alphabetically
                sorted_word_count = sorted(
                    word_count.items(),
                    key=lambda kv: (-kv[1], kv[0])
                )

                # Print the results
                for word, count in sorted_word_count:
                    print(f"{word}: {count}")

        else:
            # If status code is not 200, print nothing
            return

    except requests.RequestException:
        # In case of a request exception, print nothing
        return


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(
            sys.argv[0]
        ))
    else:
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])