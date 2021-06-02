import pandas as pd
import csv

#python book ebay scraper
df = pd.read_csv('output.csv')
df.head()
#print(df)

#displaying only books that have sold more than 0 and create a new csv file
filt = (df['total sold'] > 0)
zero_df = df.loc[filt]
zero_df.head()

#print(zero_df)

zero_df.to_csv('modified.csv')




#json data from post.json
posts_df = pd.read_json('posts.json')
posts_df.head()
#print(posts_df)

#posts_df.to_csv('posts.csv')
