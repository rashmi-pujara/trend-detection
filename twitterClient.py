import sys
import tweepy as tw


def twitterAuth():
    """
        Setup Twitter API authentication.
        Replace keys and secrets with your own.

        @returns: tweepy.OAuthHandler object
    """

    try:
        consumerKey = "4KvUNbNFVKthKIPTzss9gO2e9"
        consumerSecret = "vr7lXG9jJtBSOjx5jxJIUoidAlTh85AOZoFnA3U8xg6wdIxZcE"
        accessToken = "2607948770-NGAAsCP3zP07ThHJvQWedkN7vj5zW0ovtaMmxBE"
        accessSecret = "pKTvLsbPGCTDBVqFcuEotKjBYM45xoXQkDvyccrWjvFUb"
    except KeyError:
        sys.stderr.write("Key or secret token are invalid.\n")
        sys.exit(1)

    auth = tw.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessSecret)

    return auth



def twitterClient():
    """
        Setup Twitter API client.

        @returns: tweepy.API object
    """

    auth = twitterAuth()
    client = tw.API(auth, wait_on_rate_limit=True)

    return client
