
def get_hashtag_tweets(verbose = 1, private = False):
    import json
    import tweepy
    import csv
    import sys
    import getpass
    from google.colab import files
    with open('twitter_credentials.json') as cred_data:
        info = json.load(cred_data)
        consumer_key = info['CONSUMER_KEY']
        consumer_secret = info['CONSUMER_SECRET']
        access_key = info['ACCESS_KEY']
        access_secret = info['ACCESS_SECRET']
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    if not private:
        hashtag = input('Enter keyword:-- ')
    else:
        hashtag = getpass.getpass('Enter keyword:-- ')
    # Open/Create a file to append data
    csvFile = open(hashtag[1:] + '_tweets.csv', 'w')
    #Use csv Writer
    csvWriter = csv.writer(csvFile, delimiter = '\t')
    csvWriter.writerow(['tweet_id' ,  'created_at', 'text',  'language', 'user_id' , 'screen_name', 'user_followers',
                           'user_friends' , 'is_verified'
                         ])
    for n, tweet in enumerate(tweepy.Cursor(api.search, q= hashtag, count= 400, tweet_mode = 'extended').items()):
      csvWriter.writerow([tweet.id_str,  str(tweet.created_at) , tweet.full_text, tweet.lang, tweet.user.id_str,
                          str(tweet.user.screen_name), str(tweet.user.followers_count),
                          str(tweet.user.friends_count), str(tweet.user.verified)])
      if verbose:
        sys.stdout.write('\r'+str(n) + ' tweets added to csv file')
        sys.stdout.flush()
get_hashtag_tweets()
