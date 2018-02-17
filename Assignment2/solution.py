import pandas as pd
import numpy as np

#1. Read and merge the dataset into single dataframe
game=pd.read_csv('ign/ign.csv', index_col=0,usecols=range(7))
score=pd.read_csv('ign/ign_score.csv',index_col=0,usecols=range(5))
game_new=pd.merge(game,score,left_index=True, right_index=True)
header=list(game_new)
print('merged dataframe','\n')


#2. Provide the names of 10 movies rated highest.
movie_rating=game_new[['title','score']].values
movie_info=game_new.sort_values(['score'],ascending=False)
#print(movie_info['title'].head(10))

#3. Rank the movie names by their highest average rating scores.
#wrong
game_new['score'] = pd.to_numeric(game_new['score'].str.replace(' ',''), errors='force')
print(sorted( game_new.groupby('title')['score'].mean()))





