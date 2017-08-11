import tweepy
from tweepy import OAuthHandler
import matplotlib.pyplot as plt
import re 
import matplotlib.patches as mpatches

#Input any amount of words into the array "list_of_words" to find how many times Trump and Hillary have tweeted
#each word.  

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

#If you are interested in other users you can use http://gettwitterid.com/ to find their Username Id.
trump = '25073877'
hillary = '1339835893'

list_of_words = ['america', 'great', 'fake', 'thank', 'russia', 'witch', 'hunt', 'Trump']


def user_tweet_word(user):
	tweets = []
	retweet_count = []
	date = []
	statuses = api.user_timeline(user_id = user, count = 200)

	for i in range(len(statuses)):
		tweets.append(statuses[i].text)
		retweet_count.append(statuses[i].retweet_count)
		date.append(statuses[i].created_at)

	def word_bank(word):
		word_bank = []
		temp_word_bank = []
		temp_word_bank.append(word)
		temp_word_bank.append(word+'s')
		temp_word_bank.append(word+'es')
		temp_word_bank.append(word+'r')
		temp_word_bank.append(word+'er')
		temp_word_bank.append(word+'ing')
		temp_word_bank.append(word+'ly')
		temp_word_bank.append(word+'ed')

		for i in range(len(temp_word_bank)):
			temp_word_bank.append(temp_word_bank[i].capitalize())
			temp_word_bank.append(temp_word_bank[i].upper())

		for i in range(len(temp_word_bank)):
			word_bank.append(r'\b'+temp_word_bank[i]+r'\b')

		return word_bank


	def word_amount(word):
		wanted_word_number = 0
		split_tweets = [[]]
		split_tweets.remove([])

		word_variations = word_bank(word)

		for i in range(len(tweets)):
			split_tweets.append(tweets[i].split())

		for i in range(len(split_tweets)):
			for word in split_tweets[i]:
				for wanted_word in word_variations:
					if re.search(wanted_word, word):
						wanted_word_number = wanted_word_number + 1

		return wanted_word_number

	word_count = []

	for i in range(len(list_of_words)):
		word_count.append(word_amount(list_of_words[i]))

	print(word_count)

	y=[]
	for i in range(len(list_of_words)):
		y.append(word_count[i])

	return y


x = []
for i in range(len(list_of_words)):
	x.append(i)

y1 = user_tweet_word(trump)
y2 = user_tweet_word(hillary)

fix, ax = plt.subplots()
ax.scatter(x, y1, s = 100, color = 'red')
ax.scatter(x, y2, s = 100, color = 'blue')
plt.xticks(x, list_of_words)

trump_label = mpatches.Patch(color='red', label='Trump')
hillary_label = mpatches.Patch(color='blue', label='Hillary')

ax.set_title("Amount of Times User has Tweeted a Given Word (Past 200 tweets)")
ax.legend(handles=[trump_label, hillary_label])

plt.show()


