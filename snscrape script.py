import snscrape.modules.twitter as sntwitter
import pandas as pd
query = "pranandapaloh lang:id until:2022-08-31 since:2019-10-20"
tweets = []
limit = 999999999999
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.user.username, 
                       tweet.user.id,
                       tweet.user.created,
                       tweet.user.url,
                       tweet.user.displayname,
                       tweet.user.description,
                       #tweet.user.rawDescription,
                       #tweet.user.descriptionUrls,
                       tweet.user.linkUrl,
                       tweet.user.linkTcourl,
                       

                       
                       tweet.user.verified,
                       tweet.user.followersCount,
                       tweet.user.friendsCount,
                       tweet.user.statusesCount,
                       tweet.user.favouritesCount,
                       tweet.user.listedCount,
                       tweet.user.mediaCount,
                       tweet.user.location,
                       tweet.user.protected,
                       tweet.user.profileImageUrl,
                       tweet.user.profileBannerUrl,
                       tweet.user.label,


                       tweet.url, 
                       tweet.id,
                       tweet.date, 
                       tweet.content, 
                       #tweet.renderedContent,
                       


                       tweet.replyCount,
                       tweet.retweetCount,
                       tweet.likeCount,
                       tweet.quoteCount,
                       tweet.conversationId,
                       tweet.lang,
                       tweet.source,
                       tweet.sourceUrl,
                       tweet.sourceLabel,
                       #tweet.outlinks,
                       #tweet.tcooutlinks,

                       #tweet.media,
                       tweet.retweetedTweet,
                       tweet.quotedTweet,
                       #tweet.tcooutlinks,
                       tweet.inReplyToTweetId,
                       tweet.inReplyToUser,

                       #tweet.mentionedUsers,

                       tweet.coordinates,
                       tweet.place,
                       tweet.hashtags,
                       tweet.cashtags
                       ])
        

df = pd.DataFrame(tweets, columns=['Username',
                                   'User_Id',
                                   'User_Creation_Date',
                                   'User_Url',
                                   'User_Displayname',
                                   'User_Description',
                                   #'User_rawDescription',
                                   #'User_DescriptionUrls',
                                   'User_Description_Url',
                                   'User_Description_tcoURL',


                                   
                                   'User_Verified',
                                   'User_Followers_Count',
                                   'User_Friends_Count',
                                   'User_Statuses_Count',
                                   'User_Favourites_Count',
                                   'User_Listed_Count',
                                   'User_Media_Count',
                                   'User_Location',
                                   'User_Protected',
                                   'User_Profile_Image_Url',
                                   'User_Profile_Banner_Url',
                                   'User_Label',
                                   

                                   'Tweet_Url',
                                   'Tweet_Id',
                                   'Tweet_Date',
                                   'Tweet_Content', 
                                   #'Tweet_Rendered_Content',
                                   
                                   
                                   
                                   'Tweet_Reply_Count',
                                   'Tweet_Retweet_Count',
                                   'Tweet_Like_Count',
                                   'Tweet_Quote_Count',
                                   'Tweet_Conversation_Id',
                                   'Tweet_Lang',
                                   'Tweet_Source',
                                   'Tweet_Source_Url',
                                   'Tweet_Source_Label',
                                   #'Tweet_outlinks',
                                   #'Tweet_tcooutlinks',
                                   
                                   #'Tweet_Media',
                                   'Tweet_Retweeted_Tweet',
                                   'Tweet_Quoted_Tweet',
                                   #'Tweet_tcooutlinks',
                                   'Tweet_inReply_To_Tweet_Id',
                                   'Tweet_inReply_ToUser',
                                   
                                   #'Tweet_Mentioned_Users',
                                   
                                   'Tweet_Coordinates',
                                   'Tweet_Place',
                                   'Tweet_Hashtags',
                                   'Tweet_Cashtags'
                                   ])
print(df)
# to save to csv
df.to_csv('pranandapaloh.csv', mode='w+')