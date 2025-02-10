from twittapi import TwitterApi

if __name__ == '__main__':
  x_rapidapi_key = '<YOUR_X_RAPIDAPI_KEY>'
  twitter = TwitterApi(x_rapidapi_key)

  username = 'taylorswift13'
  user_id = twitter.get_user_id_by_username(username)
  if user_id is None:
    print(f'User {username} not found')
    exit()
  
  tweets = twitter.get_user_tweets(user_id)
  print(tweets)
