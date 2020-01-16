
import tweepy 

##def check_last_posts(new_post):
##    page_num = 1
##    while True:
##        timeline = api.user_timeline(page = page_num)
##        for post in timeline:
##            post = (post.text.encode('utf-8')
##            if not (post.startswith(b"RT")):
##                if post != new_post:
##                    return True
##                else:
##                    return False;
##        page_num+=1

  
# personal details
twitter_keys = {
    'consumer_key': 'gWopJ9Go4jLQwMuFOEP03e4bv',
    'consumer_secret': 'bDeBF2e3O3i0uUL1L5seQWva3SpyLfxIrq1KcBgGWXBpDjAR8k',
    'access_token_key': '1206358258820235265-QqFYcbyu6DSAvOAZmN9QCtf6kFi2T4',
    'access_token_secret': 'vdNyN97Rgii5eXyUrz3L0t7RI3nR8HShWiqWpOoFLL7Yo'
}
#Setup access to API
auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])

api = tweepy.API(auth)


#user_tweets = api.user_timeline(screen_name = "carpedatbooty", count = 5, include_rts = False, tweet_mode = 'extended')



#tweet posting
for tweet in tweepy.Cursor(api.home_timeline).items(5):
    #Make sure you're not the user
    if not api.get_user("AreZachs"):
        api.update_status(tweet.text)
        api.send_direct_message(screen_name = 'BDude1995', full_text = 'You made another horrible tweet. Please stop')
    
