import urllib
from constant import *
from get_post_id import *
#def a fuction for comment on a post
def post_comment(insta_username):
    post_id=get_post_id(insta_username)
    comment=raw_input("write the comment:>")
    payload={'access_token':APP_ACCESS_TOKEN,'text':comment}
    request_url=BASE_URL+'media/%s/comments' %post_id
    print "POST request url %s" % request_url
    make_comment=requests.post(request_url,payload).json()

    #check what is the response from server
    if make_comment['meta']['code'] == 200:
        print "commect successfull posted "
    else:
        print "commect not posted"


#calling the defined function
post_comment(raw_input("username:"))