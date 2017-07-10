# import library and files

import requests
from constant import *

# get_user_id function to get the user id


def get_user_id(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % request_url
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']      # use return if used this file in future instead of print
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()

# calling the function
# get_user_id(raw_input("enter"))
