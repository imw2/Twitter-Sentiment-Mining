
from datetime import datetime, timedelta
import tweepy
import csv #Import csv

auth = tweepy.auth.OAuthHandler('', '')
auth.set_access_token('', '')

api = tweepy.API(auth)

now = datetime.today().now()
prev=now-timedelta(days=1)
now=now.strftime("%Y-%m-%d")
prev=prev.strftime("%Y-%m-%d")

# Open/create a file to append data to
csvFile = open('fileNameHere.csv', 'a',newline="")

#Use csv writer
csvWriter = csv.writer(csvFile)
#csvWriter = csv.DictWriter(csvFile, lineterminator = '\n')
c = 0
for tweet in tweepy.Cursor(api.search,
                           q = "#searchQueryHere",
                           since= prev,
                           until= now,
                           lang = "en",
                           count=1000).items():
    if (not tweet.retweeted) and ('RT @' not in tweet.text):
        # Write a row to the CSV file. I use encode UTF-8
        csvWriter.writerow([tweet.created_at, tweet.user.screen_name, tweet.text.encode('utf-8')])
    #print (tweet.created_at, tweet.text)
    c += 1
    print(c)
csvFile.close()

