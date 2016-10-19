# -*- coding: utf-8 -*-
"""

    Query the LiveStories Partners API (Authenticated)

    You need to have a LiveStories account to use the authenticated API.
    You may create a key/secret at http://insight.livestories.com/team

    More details at https://developers.livestories.com

    (C) 2016 LiveStories - See https://github.com/LiveStories/developers/LICENSE.md

"""
import requests

from livestories.api.authorizer import Authorizer

API_URL = 'https://api.livestories.com/'
# API_KEY = 'eric'
# SECRET = '8kM94BChdAGQHCqY'

API_KEY = 'eric_2'
SECRET = '6AELq8ErUs62HysP'

# get an auth_string for your request. This needs to be for every request.
auth_string = Authorizer(API_KEY, SECRET).authorization_string('GET', API_URL + 'v1/dataset')

# Get a list of all the datasets.
r = requests.get(API_URL + "v1/dataset?" + auth_string)
print(r.status_code)
print(r.content)
