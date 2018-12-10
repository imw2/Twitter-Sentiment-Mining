
import pandas as pd

year = "2018"

def main(tweet_file, new_file_name):
    currentDate = ""
    total = 0
    pos = 0
    neg = 0
    #open(new_file_name).close()
    tweetLibrary = pd.read_csv(tweet_file)
    tweetLibrary = tweetLibrary[['Date','User','Tweet','Sentiment']]
    
    for index, row in tweetLibrary.iterrows():
        date = row["Date"]
        tweet = row["Tweet"]
        sentiment = row["Sentiment"]
        
        if currentDate != date[0:date.index(year) + len(year)]:
            if currentDate != "":
                #write data to file
                Day = currentDate
                Positive = pos/total
                Negative = neg/total
                print(Day,",",pos,",",neg,",",total)
            currentDate = date[0:date.index(year) + len(year)]
            total = 0
            pos = 0
            neg = 0 
        else:
            if sentiment == "positive":
                pos += 1
            if sentiment == "negative":
                neg += 1
            total += 1
    #tweetLibrary.to_csv(new_file_name,sep=',')

main("..\\faangSentiment\\finalAmazonTwitterData.csv","..\\faangPercent\\percentageAmazonTwitterData.csv")
#main("..\\faangSentiment\\finalAppleTwitterData.csv","..\\faangPercent\\percentageAppleTwitterData.csv")
#main("..\\faangSentiment\\finalFacebookTwitterData.csv","..\\faangPercent\\percentageFacebookTwitterData.csv")
#main("..\\faangSentiment\\finalGoogleTwitterData.csv","..\\faangPercent\\percentageGoogleTwitterData.csv")
#main("..\\faangSentiment\\finalNetflixTwitterData.csv","..\\faangPercent\\percentageNetflixTwitterData.csv")
