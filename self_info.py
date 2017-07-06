import requests
from constant import APP_ACCESS_TOKEN,BASE_URL
import urllib
#SELF_INFO FUNCTION
#IT TELLS ABOUT THE USER INFORMATION FROM THE INSTAGRAM
def self_info():
  request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  user_info = requests.get(request_url).json()

#to check wheather server is reply or not
  #if reply 200 then server reply
  if user_info['meta']['code'] == 200:
    if len(user_info['data']):
      print 'Username: %s' % (user_info['data']['username'])
      print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
      print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
      print 'No. of posts: %s' % (user_info['data']['counts']['media'])
      iimagename=user_info['data']['profile_picture']
      imagename2=user_info['data']['id'] +'.jpeg'
      urllib.urlretrieve(iimagename,imagename2)
      print 'image downloaded'


    else:
      print 'User does not exist!'
  else:
    print 'Status code other than 200 received!'
