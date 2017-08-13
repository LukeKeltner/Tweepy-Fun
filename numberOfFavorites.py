import tweepy
from tweepy import OAuthHandler
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#Counts how many favorites a given tweet has from given users.  Right now it looks at Trump and Obama

#consumer_key, consumer_secret, access_token, and access_secret are personalized to any given user's twitter account.
#Therefore, I have omitted these from this public access.  However, here is a great tutorial to get your own...
#https://legacy-help.pro.photo/twitter-api-credentials/
consumer_key = '...'
consumer_secret = '...'
access_token = '...'
access_secret = '...'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#numerOfTweets has a max limit of 200
numberOfTweets = 50

#If you are interested in other users you can use http://gettwitterid.com/ to find their Username Id.
trump = '25073877'
obama = '813286'

trump_tweets = api.user_timeline(trump, count=numberOfTweets)
obama_tweets = api.user_timeline(obama, count=numberOfTweets)

trump_total_likes = 0
obama_total_likes = 0

trump_likes_over_time = []
obama_likes_over_time = []

for i in range(len(trump_tweets)):
	trump_total_likes = trump_total_likes + trump_tweets[i].favorite_count
	obama_total_likes = obama_total_likes + obama_tweets[i].favorite_count
	trump_likes_over_time.append(trump_tweets[i].favorite_count)
	obama_likes_over_time.append(obama_tweets[i].favorite_count)

x = list(range(len(trump_tweets)))

plt.scatter(x, trump_likes_over_time, color='red')
plt.scatter(x, obama_likes_over_time, color='blue')
plt.title('Obama and Trump Favorites Number Per Tweet (Past '+str(numberOfTweets)+' Tweets)')

red_patch = mpatches.Patch(color='red', label='Trump: Total Favorites = '+str(trump_total_likes))
blue_patch = mpatches.Patch(color='blue', label='Obama: Total Favorites = '+str(obama_total_likes))
plt.legend(handles=[red_patch, blue_patch])
plt.xlabel('Tweet Number (0: most recent, '+str(numberOfTweets)+': furthest back in time)')
plt.ylabel('Favorited Amount')

plt.show()


