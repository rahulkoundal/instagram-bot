import urllib
import requests
from get_user_id import *
from constant import APP_ACCESS_TOKEN,BASE_URL


#def function for user information
def get_user_info(insta_username):
  user_id = get_user_id(insta_username)
  request_url = BASE_URL + 'users/%s?access_token=%s' % (user_id, APP_ACCESS_TOKEN)
  print ('GET request url : %s' % (request_url))
  user_info = requests.get(request_url).json()
  if user_info['meta']['code'] == 200:
      if len(user_info['data']):
          # usernam fetch
          # print 'Username: %s' % (user_info['data']['username'])
          insta_username = user_info['data']['username']
          print 'username:%s' % (insta_username)
          # no of followers,following,posts
          print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
          print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
          print 'No. of posts: %s' % (user_info['data']['counts']['media'])
      else:
          print ('There is no data for this user!')
  else:
      print ('Status code other than 200 received!')


get_user_info(raw_input("enter username:>"))