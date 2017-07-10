# import library and file

import requests
from constant import APP_ACCESS_TOKEN, BASE_URL
import urllib

# SELF_INFO FUNCTION IT TELLS ABOUT THE USER INFORMATION FROM THE instagram


def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % APP_ACCESS_TOKEN
    print 'GET request url : %s' % request_url
    user_info = requests.get(request_url).json()

#  to check wheather server is reply or not

    if user_info['meta']['code'] == 200:
            # len() function check whether server send the data
            if len(user_info['data']):
                # username fetch
                # print 'Username: %s' % (user_info['data']['username'])
                username = user_info['data']['username']
                print 'username:%s' % username
                # no of followers,following,posts
                print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
                print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
                print 'No. of posts: %s' % (user_info['data']['counts']['media'])
                # fetch profile photo from instgram
                image = user_info['data']['profile_picture']
                image1 = user_info['data']['id'] + '.jpeg'
                urllib.urlretrieve(image, image1)
                print 'image is downloaded'
            else:
                print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'

# calling to self_info function
self_info()



