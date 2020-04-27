import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("fc6xJlJ1JPHfJ71V7WUqHtGMu", "Jk23x2s6EdZx8afzL8lqvWASCCDoOcW7BeKYlTZrSGws3WnQBG")
auth.set_access_token("1252816299899539459-bksy4WW9gcw2nUb09pI0perStRvNsa", "kzb4qZUd3fEex1ToTgkuomDAXvOs1aGMWloqbY3mehWup")

# Create API object to invoke Twitter API methods
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


# Create a tweet
# api.update_status("Hello TWEEPY")

# access token: 1252816299899539459-bksy4WW9gcw2nUb09pI0perStRvNsa
# access token secret: kzb4qZUd3fEex1ToTgkuomDAXvOs1aGMWloqbY3mehWup

# API key: fc6xJlJ1JPHfJ71V7WUqHtGMu
# API secret key: Jk23x2s6EdZx8afzL8lqvWASCCDoOcW7BeKYlTZrSGws3WnQBG


try:
    api.verify_credentials()
    print("AUTH OK")
except:
    print("ERROR DURING AUTH")

# timeline = api.home_timeline()
# for tweet in timeline:
#     print(f"{tweet.user.name} said {tweet.text}")


# Fetches user and prints in 20 most recent followers

user = api.get_user("GaspMrShane")
print("User details: ")
print(user.name)
print(user.description)
print(user.location)

print("Last 20 followes")
for follower in user.followers():
    print(follower.name)

# Methods for Tweets
api.update_status("Test tweet from tweepy python")

# Methods for following and un-following
api.create_friendship("GaspMrShane")
api.create_friendship("p_thilakaratne")
# api.destroy_friendship("GaspMrShane")
api.create_friendship("MathishiG")

# methods for your account

api.update_profile(description="ASTRONOMICAL")

# Methods for likes: marking the most recent tweet in your home

tweets = api.home_timeline(count=1)
tweet = tweets[0]
print(f"Liking tweet {tweet.id} of {tweet.author.name}")
api.create_favorite(tweet.id)

# Methods for Trends: list current trends for any geographical location

trends_result = api.trends_place(1)
for trend in trends_result[0]["trends"]:
    print(trend["name"])

# Methods for searches: brings up 10 most recent public tweets that are in English and contain the word "python"

for tweet in api.search(q="townsville", lang="en", rpp=1):
    print(f"{tweet.user.name}:{tweet.text}")

print(api.trends_available())

# Methods for streaming. It allows you to actively watch for tweets that match certain criteria in real time.







