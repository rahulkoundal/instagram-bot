import requests
from constant import *
from get_post_id import *

#def a fuction for like a user most recent post

def like_a_post(insta_username):
    post_id=get_post_id(insta_username)
    req_url=BASE_URL+'media/%s/likes' % post_id
    payload={'access_token' :APP_ACCESS_TOKEN}
    print 'GET request url %s' %req_url
    like_post=requests.post(req_url,payload).json()

    #check if server respond to our request or not
    if like_post['meta']['code'] == 200:
        print " successfully liked"

    else:
        print "like not apply"

#calling the defined function
like_a_post(raw_input("enter a  username: "))