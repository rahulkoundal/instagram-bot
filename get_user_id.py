#import file from other file
import  requests
import urllib
from constant import *

#get_user_id function
def get_user_id(insta_username):
  request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
  print 'GET request url : %s' %(request_url)
  user_info=requests.get(request_url).json()
  if user_info['meta']['code'] == 200:
      if len(user_info['data']):
          print user_info['data'][0]['id']
      else:
          print "user not exist"
  else:
      print "unable to acces the info"
      exit()


get_user_id(raw_input("enter username:>"))