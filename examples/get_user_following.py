from twittapi import TwitterApi

if __name__ == '__main__':
  x_rapidapi_key = '<YOUR_X_RAPIDAPI_KEY>'
  twitter = TwitterApi(x_rapidapi_key)

  username = 'elonmusk'
  user_id = twitter.get_user_id_by_username(username)
  if user_id is None:
    print(f'User {username} not found')
    exit()
  
  following = twitter.get_user_following(user_id)
  print(following)
