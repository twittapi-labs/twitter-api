from twittapi import TwitterApi

if __name__ == '__main__':
  x_rapidapi_key = '<YOUR_X_RAPIDAPI_KEY>'
  twitter = TwitterApi(x_rapidapi_key)

  keyword = 'disney'
  results = twitter.search_top(keyword)
  
  print(results)
