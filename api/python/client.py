# -*- coding: utf-8 -*-
"""

    Query the LiveStories Public API
    More details at https://developers.livestories.com/public

    (C) 2016 LiveStories - See https://github.com/LiveStories/developers/LICENSE.md

"""
import requests

API_URL = 'https://api.livestories.com/'
TEAM_ID = '5679cc9a4031050014bc4c59'  # Insert the team ID that's of interest to you!

# Get a list of all the public datasets for this team.
r = requests.get(API_URL + "v1/dataset?team=" + TEAM_ID)
print(r.status_code)
print(r.content)

# Get the details about a particular dataset
r = requests.get(API_URL + "v1/dataset/6bdf49c1-64aa-43bf-8393-60fb77d684cd/672855f9-65db-4ed5-9fd4-d996b9c80085")
print(r.status_code)
print(r.content)