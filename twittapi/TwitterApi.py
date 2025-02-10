import requests

class TwitterApi:
  def __init__(self, x_rapidapi_key: str):
    """
    Initialize the TwitterApi instance.

    Args:
      x_rapidapi_key (str): The API key for accessing the RapidAPI Twitter API.

    Raises:
      ValueError: If the x_rapidapi_key is not provided.
    """
    if not x_rapidapi_key:
      print(self.get_api_key_tutorial())
      raise ValueError('x_rapidapi_key is required')

    self.x_rapidapi_key = x_rapidapi_key
    self.host = 'twitter-x-api.p.rapidapi.com'
    self.base_api_url = f'https://{self.host}/api'
    self.headers = {
      'x-rapidapi-key': self.x_rapidapi_key,
      'x-rapidapi-host': self.host
    }

  @staticmethod
  def get_api_key_tutorial():
    """
    Provides a tutorial on how to obtain the API key for accessing the RapidAPI Twitter API: https://rapidapi.com/Lundehund/api/twitter-x-api

    Returns:
      str: A step-by-step guide to obtain the API key.
    """
    tutorial = """
    To obtain the API key for accessing the RapidAPI Twitter API, follow these steps:

    1. Go to the RapidAPI website: https://rapidapi.com
    2. Sign up for a free account or log in if you already have one.
    3. Navigate to the Twitter API page: https://rapidapi.com/Lundehund/api/twitter-x-api
    4. Subscribe to the API by selecting a pricing plan that suits your needs.
    5. After subscribing, you will be able to find your API key in the "Endpoints" tab or in the "API Key" section of your RapidAPI dashboard.
    6. Copy the API key and use it to initialize the TwitterApi class in your code.

    Note: Keep your API key secure and do not share it publicly.
    """
    return tutorial

  def _make_request(self, url: str, params: dict):
    try:
      res = requests.get(
        url,
        params=params,
        headers=self.headers
      )
      res.raise_for_status()
      return res.json()
    except requests.exceptions.HTTPError as http_err:
      print(f'HTTP error occurred: {http_err.response.status_code} - {http_err.response.text}')
      return None
    except requests.exceptions.RequestException as err:
      print(f'An error occurred: {err}')
      return None
  
  # User Endpoints
  def get_user_detail(self, username: str):
    """
    Retrieve the details of a Twitter user by their username.

    Args:
      username (str): The username of the Twitter user.

    Returns:
      dict: A dictionary containing the user's details.

    Raises:
      HTTPError: If the request to the Twitter API fails.
    """
    url = f'{self.base_api_url}/user/detail'
    params = {
      'username': username
    }
    return self._make_request(url, params)
  
  def get_user_id_by_username(self, username: str):
    """
    Retrieve the user ID of a Twitter user by their username.

    Args:
      username (str): The username of the Twitter user.

    Returns:
      str: The user ID of the Twitter user.

    Raises:
      HTTPError: If the request to the Twitter API fails.
    """
    user_detail = self.get_user_detail(username)
    return user_detail['user']['result']['rest_id'] if user_detail else None
  
  def get_user_followers(
    self,
    user_id: str,
    count: int = 20,
    cursor: str = None,
    is_simplify: bool = False
  ):
    """
    Retrieve the followers of a specified user.

    Args:
      user_id (str): The ID of the user whose followers are to be retrieved.
      count (int, optional): The number of followers to retrieve. Defaults to 20.
      cursor (str, optional): The cursor for pagination. Defaults to None.
      is_simplify (bool, optional): Whether to simplify the response. Defaults to False.

    Returns:
      dict: The response from the API containing the user's followers.

    Raises:
      HTTPError: If the request to the Twitter API fails.
    """
    url = f'{self.base_api_url}/user/followers'
    params = {
      'user_id': user_id,
      'count': count,
      'cursor': cursor,
      'is_simplify': is_simplify
    }
    return self._make_request(url, params)
  
  def get_user_verified_followers(
    self,
    user_id: str,
    count: int = 20,
    cursor: str = None,
    is_simplify: bool = False
  ):
    """
    Retrieve the verified followers of a specified user.

    Args:
      user_id (str): The ID of the user whose verified followers are to be retrieved.
      count (int, optional): The number of verified followers to retrieve. Defaults to 20.
      cursor (str, optional): The cursor for pagination. Defaults to None.
      is_simplify (bool, optional): Whether to simplify the response. Defaults to False.

    Returns:
      dict: The response from the API containing the user's verified followers.

    Raises:
      HTTPError: If the request to the Twitter API fails.
    """
    url = f'{self.base_api_url}/user/followers/blue-verified'
    params = {
      'user_id': user_id,
      'count': count,
      'cursor': cursor,
      'is_simplify': is_simplify
    }
    return self._make_request(url, params)
  
  def get_user_following(
    self,
    user_id: str,
    count: int = 20,
    cursor: str = None,
    is_simplify: bool = False
  ):
    """
    Retrieve the users followed by a specified user.

    Args:
      user_id (str): The ID of the user whose following list is to be retrieved.
      count (int, optional): The number of users to retrieve. Defaults to 20.
      cursor (str, optional): The cursor for pagination. Defaults to None.
      is_simplify (bool, optional): Whether to simplify the response. Defaults to False.

    Returns:
      dict: The response from the API containing the users followed by the specified user.

    Raises:
      HTTPError: If the request to the Twitter API fails.
    """
    url = f'{self.base_api_url}/user/following'
    params = {
      'user_id': user_id,
      'count': count,
      'cursor': cursor,
      'is_simplify': is_simplify
    }
    return self._make_request(url, params)
  
  def get_user_subscriptions(
    self,
    user_id: str,
    count: int = 20,
    cursor: str = None,
    is_simplify: bool = False
  ):
    """
    Retrieve the subscriptions of a specified user.

    Args:
      user_id (str): The ID of the user whose subscriptions are to be retrieved.
      count (int, optional): The number of subscriptions to retrieve. Defaults to 20.
      cursor (str, optional): The cursor for pagination. Defaults to None.
      is_simplify (bool, optional): Whether to simplify the response. Defaults to False.

    Returns:
      dict: The response from the API containing the user's subscriptions.

    Raises:
      HTTPError: If the request to the Twitter API fails.
    """
    url = f'{self.base_api_url}/user/subscriptions'
    params = {
      'user_id': user_id,
      'count': count,
      'cursor': cursor,
      'is_simplify': is_simplify
    }
    return self._make_request(url, params)
  
  def get_user_tweets(
    self,
    user_id: str,
    count: int = 20,
    cursor: str = None,
    is_simplify: bool = False
  ):
    """
    Retrieve the tweets of a specified user.

    Args:
      user_id (str): The ID of the user whose tweets are to be retrieved.
      count (int, optional): The number of tweets to retrieve. Defaults to 20.
      cursor (str, optional): The cursor for pagination. Defaults to None.
      is_simplify (bool, optional): Whether to simplify the response. Defaults to False.

    Returns:
      dict: The response from the API containing the user's tweets.

    Raises:
      HTTPError: If the request to the Twitter API fails.
    """
    url = f'{self.base_api_url}/user/tweets'
    params = {
      'user_id': user_id,
      'count': count,
      'cursor': cursor,
      'is_simplify': is_simplify
    }
    return self._make_request(url, params)
  
  def get_user_replies(
    self,
    user_id: str,
    count: int = 20,
    cursor: str = None,
    is_simplify: bool = False
  ):
    """
    Retrieve the replies of a specified user.

    Args:
      user_id (str): The ID of the user whose replies are to be retrieved.
      count (int, optional): The number of replies to retrieve. Defaults to 20.
      cursor (str, optional): The cursor for pagination. Defaults to None.
      is_simplify (bool, optional): Whether to simplify the response. Defaults to False.

    Returns:
      dict: The response from the API containing the user's replies.

    Raises:
      HTTPError: If the request to the Twitter API fails.
    """
    url = f'{self.base_api_url}/user/replies'
    params = {
      'user_id': user_id,
      'count': count,
      'cursor': cursor,
      'is_simplify': is_simplify
    }
    return self._make_request(url, params)
  
  def get_user_medias(
    self,
    user_id: str,
    count: int = 20,
    cursor: str = None,
    is_simplify: bool = False
  ):
    """
    Retrieve the media posts of a specified user.

    Args:
      user_id (str): The ID of the user whose media posts are to be retrieved.
      count (int, optional): The number of media posts to retrieve. Defaults to 20.
      cursor (str, optional): The cursor for pagination. Defaults to None.
      is_simplify (bool, optional): Whether to simplify the response. Defaults to False.

    Returns:
      dict: The response from the API containing the user's media posts.

    Raises:
      HTTPError: If the request to the Twitter API fails.
    """
    url = f'{self.base_api_url}/user/medias'
    params = {
      'user_id': user_id,
      'count': count,
      'cursor': cursor,
      'is_simplify': is_simplify
    }
    return self._make_request(url, params)
  
  # Tweet Endpoints
  def get_tweet_detail(self, tweet_id: str):
    """
    Retrieve the details of a specified tweet.

    Args:
      tweet_id (str): The ID of the tweet whose details are to be retrieved.

    Returns:
      dict: The response from the API containing the tweet's details.

    Raises:
      HTTPError: If the request to the Twitter API fails.
    """
    url = f'{self.base_api_url}/tweet/detail'
    params = {
      'tweet_id': tweet_id
    }
    return self._make_request(url, params)
  
  def get_tweet_retweeters(
    self,
    tweet_id: str,
    count: int = 20,
    cursor: str = None,
    is_simplify: bool = False
  ):
    """
    Retrieve the users who retweeted a specified tweet.

    Args:
      tweet_id (str): The ID of the tweet whose retweeters are to be retrieved.
      count (int, optional): The number of retweeters to retrieve. Defaults to 20.
      cursor (str, optional): The cursor for pagination. Defaults to None.
      is_simplify (bool, optional): Whether to simplify the response. Defaults to False.

    Returns:
      dict: The response from the API containing the tweet's retweeters.

    Raises:
      HTTPError: If the request to the Twitter API fails.
    """
    url = f'{self.base_api_url}/tweet/retweeters'
    params = {
      'tweet_id': tweet_id,
      'count': count,
      'cursor': cursor,
      'is_simplify': is_simplify
    }
    return self._make_request(url, params)
  
  def get_tweet_retweets(
    self,
    tweet_id: str,
    count: int = 20,
    cursor: str = None,
    is_simplify: bool = False
  ):
    """
    Retrieve the retweets of a specified tweet.

    Args:
      tweet_id (str): The ID of the tweet whose retweets are to be retrieved.
      count (int, optional): The number of retweets to retrieve. Defaults to 20.
      cursor (str, optional): The cursor for pagination. Defaults to None.
      is_simplify (bool, optional): Whether to simplify the response. Defaults to False.

    Returns:
      dict: The response from the API containing the tweet's retweets.

    Raises:
      HTTPError: If the request to the Twitter API fails.
    """
    url = f'{self.base_api_url}/tweet/retweets'
    params = {
      'tweet_id': tweet_id,
      'count': count,
      'cursor': cursor,
      'is_simplify': is_simplify
    }
    return self._make_request(url, params)
  
  def get_tweet_hidden_replies(
    self,
    tweet_id: str,
    count: int = 20,
    cursor: str = None,
    is_simplify: bool = False
  ):
    """
    Retrieve the hidden replies of a specified tweet.

    Args:
      tweet_id (str): The ID of the tweet whose hidden replies are to be retrieved.
      count (int, optional): The number of hidden replies to retrieve. Defaults to 20.
      cursor (str, optional): The cursor for pagination. Defaults to None.
      is_simplify (bool, optional): Whether to simplify the response. Defaults to False.

    Returns:
      dict: The response from the API containing the tweet's hidden replies.

    Raises:
      HTTPError: If the request to the Twitter API fails.
    """
    url = f'{self.base_api_url}/tweet/hidden-replies'
    params = {
      'tweet_id': tweet_id,
      'count': count,
      'cursor': cursor,
      'is_simplify': is_simplify
    }
    return self._make_request(url, params)
  
  # Search Endpoints
  def search_top(
    self,
    keyword: str,
    count: int = 20,
    cursor: str = None,
    is_simplify: bool = False
  ):
    """
    Search for top tweets based on a keyword.

    Args:
      keyword (str): The keyword to search for.
      count (int, optional): The number of results to retrieve. Defaults to 20.
      cursor (str, optional): The cursor for pagination. Defaults to None.
      is_simplify (bool, optional): Whether to simplify the response. Defaults to False.

    Returns:
      dict: The response from the API containing the search results.

    Raises:
      HTTPError: If the request to the Twitter API fails.
    """
    url = f'{self.base_api_url}/search/top'
    params = {
      'keyword': keyword,
      'count': count,
      'cursor': cursor,
      'is_simplify': is_simplify
    }
    return self._make_request(url, params)
  
  def search_latest(
    self,
    keyword: str,
    count: int = 20,
    cursor: str = None,
    is_simplify: bool = False
  ):
    """
    Search for the latest tweets based on a keyword.

    Args:
      keyword (str): The keyword to search for.
      count (int, optional): The number of results to retrieve. Defaults to 20.
      cursor (str, optional): The cursor for pagination. Defaults to None.
      is_simplify (bool, optional): Whether to simplify the response. Defaults to False.

    Returns:
      dict: The response from the API containing the search results.

    Raises:
      HTTPError: If the request to the Twitter API fails.
    """
    url = f'{self.base_api_url}/search/latest'
    params = {
      'keyword': keyword,
      'count': count,
      'cursor': cursor,
      'is_simplify': is_simplify
    }
    return self._make_request(url, params)
  
  def search_people(
    self,
    keyword: str,
    count: int = 20,
    cursor: str = None,
    is_simplify: bool = False
  ):
    """
    Search for people based on a keyword.

    Args:
      keyword (str): The keyword to search for.
      count (int, optional): The number of results to retrieve. Defaults to 20.
      cursor (str, optional): The cursor for pagination. Defaults to None.
      is_simplify (bool, optional): Whether to simplify the response. Defaults to False.

    Returns:
      dict: The response from the API containing the search results.

    Raises:
      HTTPError: If the request to the Twitter API fails.
    """
    url = f'{self.base_api_url}/search/people'
    params = {
      'keyword': keyword,
      'count': count,
      'cursor': cursor,
      'is_simplify': is_simplify
    }
    return self._make_request(url, params)
  
  def search_media(
    self,
    keyword: str,
    count: int = 20,
    cursor: str = None,
    is_simplify: bool = False
  ):
    """
    Search for media posts based on a keyword.

    Args:
      keyword (str): The keyword to search for.
      count (int, optional): The number of results to retrieve. Defaults to 20.
      cursor (str, optional): The cursor for pagination. Defaults to None.
      is_simplify (bool, optional): Whether to simplify the response. Defaults to False.

    Returns:
      dict: The response from the API containing the search results.

    Raises:
      HTTPError: If the request to the Twitter API fails.
    """
    url = f'{self.base_api_url}/search/media'
    params = {
      'keyword': keyword,
      'count': count,
      'cursor': cursor,
      'is_simplify': is_simplify
    }
    return self._make_request(url, params)
  
  def search_lists(
    self,
    keyword: str,
    count: int = 20,
    cursor: str = None,
    is_simplify: bool = False
  ):
    """
    Search for lists based on a keyword.

    Args:
      keyword (str): The keyword to search for.
      count (int, optional): The number of results to retrieve. Defaults to 20.
      cursor (str, optional): The cursor for pagination. Defaults to None.
      is_simplify (bool, optional): Whether to simplify the response. Defaults to False.

    Returns:
      dict: The response from the API containing the search results.

    Raises:
      HTTPError: If the request to the Twitter API fails.
    """
    url = f'{self.base_api_url}/search/lists'
    params = {
      'keyword': keyword,
      'count': count,
      'cursor': cursor,
      'is_simplify': is_simplify
    }
    return self._make_request(url, params)
  
  # List Endpoints
  def get_list_tweets(
    self,
    list_id: str,
    count: int = 20,
    cursor: str = None,
    is_simplify: bool = False
  ):
    """
    Retrieve the tweets from a specified list.

    Args:
      list_id (str): The ID of the list whose tweets are to be retrieved.
      count (int, optional): The number of tweets to retrieve. Defaults to 20.
      cursor (str, optional): The cursor for pagination. Defaults to None.
      is_simplify (bool, optional): Whether to simplify the response. Defaults to False.

    Returns:
      dict: The response from the API containing the list's tweets.

    Raises:
      HTTPError: If the request to the Twitter API fails.
    """
    url = f'{self.base_api_url}/list/tweets'
    params = {
      'list_id': list_id,
      'count': count,
      'cursor': cursor,
      'is_simplify': is_simplify
    }
    return self._make_request(url, params)
  
  def get_list_followers(
    self,
    list_id: str,
    count: int = 20,
    cursor: str = None,
    is_simplify: bool = False
  ):
    """
    Retrieve the followers of a specified list.

    Args:
      list_id (str): The ID of the list whose followers are to be retrieved.
      count (int, optional): The number of followers to retrieve. Defaults to 20.
      cursor (str, optional): The cursor for pagination. Defaults to None.
      is_simplify (bool, optional): Whether to simplify the response. Defaults to False.

    Returns:
      dict: The response from the API containing the list's followers.

    Raises:
      HTTPError: If the request to the Twitter API fails.
    """
    url = f'{self.base_api_url}/list/followers'
    params = {
      'list_id': list_id,
      'count': count,
      'cursor': cursor,
      'is_simplify': is_simplify
    }
    return self._make_request(url, params)
  
  def get_list_member(
    self,
    list_id: str,
    count: int = 20,
    cursor: str = None,
    is_simplify: bool = False
  ):
    """
    Retrieve the members of a specified list.

    Args:
      list_id (str): The ID of the list whose members are to be retrieved.
      count (int, optional): The number of members to retrieve. Defaults to 20.
      cursor (str, optional): The cursor for pagination. Defaults to None.
      is_simplify (bool, optional): Whether to simplify the response. Defaults to False.

    Returns:
      dict: The response from the API containing the list's members.

    Raises:
      HTTPError: If the request to the Twitter API fails.
    """
    url = f'{self.base_api_url}/list/member'
    params = {
      'list_id': list_id,
      'count': count,
      'cursor': cursor,
      'is_simplify': is_simplify
    }
    return self._make_request(url, params)
  
  # Job Endpoints
  def get_job_detail(
    self,
    job_id: str,
    is_simplify: bool = False
  ):
    """
    Retrieve the details of a specified job.

    Args:
      job_id (str): The ID of the job whose details are to be retrieved.
      is_simplify (bool, optional): Whether to simplify the response. Defaults to False.

    Returns:
      dict: The response from the API containing the job's details.

    Raises:
      HTTPError: If the request to the Twitter API fails.
    """
    url = f'{self.base_api_url}/job/detail'
    params = {
      'job_id': job_id,
      'is_simplify': is_simplify
    }
    return self._make_request(url, params)
  
  def search_job(
    self,
    keyword: str,
    count: int = 20,
    cursor: str = None,
    is_simplify: bool = False
  ):
    """
    Search for jobs based on a keyword.

    Args:
      keyword (str): The keyword to search for.
      count (int, optional): The number of results to retrieve. Defaults to 20.
      cursor (str, optional): The cursor for pagination. Defaults to None.
      is_simplify (bool, optional): Whether to simplify the response. Defaults to False.

    Returns:
      dict: The response from the API containing the search results.

    Raises:
      HTTPError: If the request to the Twitter API fails.
    """
    url = f'{self.base_api_url}/job/search'
    params = {
      'keyword': keyword,
      'count': count,
      'cursor': cursor,
      'is_simplify': is_simplify
    }
    return self._make_request(url, params)
  
  def search_job_location(self, query: str):
    """
    Search for jobs based on a location query.

    Args:
      query (str): The location query to search for.

    Returns:
      dict: The response from the API containing the search results.

    Raises:
      HTTPError: If the request to the Twitter API fails.
    """
    url = f'{self.base_api_url}/job/search/location'
    params = {
      'query': query,
    }
    return self._make_request(url, params)