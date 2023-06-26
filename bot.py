import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  # to varify account
auth.set_access_token(access_token, access_token_secret)  

api = tweepy.API(auth)
user = api.verify_credentials()

print(f'My Twitter url: {user.url}')
print(f'Hi my name is:{user.name}; aka {user.screen_name}, and I created my account on {user.created_at}')
print(f'Take a look at my bio: {user.description}')
