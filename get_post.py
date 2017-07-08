#file to get user post

from constants import *
import requests

#get_posts function to get the user post
def get_posts():
    url=BASE_URL+'users/self/media/recent/?access_token=%s' %(APP_ACCESS_TOKEN)
    print "GET request url %s " % url
    request=requests.get(url).json()

#check the responce of the server
    
    if request['meta']['code']==200:
        if len(request['data']):
            print request['data'][0]['id']

        else:
            print "data not recieved"

    else:
        print "user does not exist"

get_posts()