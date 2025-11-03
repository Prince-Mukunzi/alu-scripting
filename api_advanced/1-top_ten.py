#!bin/bash/python3
"""
Script for returning top 10 hot posts of a subreddit
"""
def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'ALU-Reddit-Task/0.1'}
    params = {'limit': 10}
    
    try:
	response = requests.get(url, headers=headers, params=params, allow_redirects=False)
	if response.status_code != 200:
	    print(None)
	    return
	data = response.json()
	posts = data.get('data', {}).get('children', [])

        for post in posts:
            print(post.get('data', {}).get('title'))

    except Exception:
        print(None)
