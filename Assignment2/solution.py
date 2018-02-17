import pandas as pd
import matplotlib.pyplot as plt

#1. Read and merge the dataset into single dataframe
game=pd.read_csv('ign/ign.csv', index_col=0,usecols=range(7))
game=game.dropna(axis=0)
scores=pd.read_csv('ign/ign_score.csv',index_col=0,usecols=range(5))
scores=scores.dropna(how='any', axis=0)
game_new=pd.merge(game,scores,left_index=True, right_index=True)
header=list(game_new)
print('merged dataframe','\n')


#2. Provide the names of 10 movies rated highest.
movie_info=game_new.sort_values(['score'],ascending=False)
print(movie_info['title'].head(10))

#3. Rank the movie names by their highest average rating scores.
movie_info['score'] = pd.to_numeric(movie_info['score'].str.replace(' ',''), errors='force')
movie_info['rank']=movie_info.groupby('title')['score'].transform('mean').rank(method='dense',ascending=False)
print(movie_info)

#4. Plot movie scores across each genre.
game_new.hist( column='score',by='genre',bins=10, xlabelsize=2,ylabelsize=2,figsize=(20,9))
plt.show()

#5. Find the group that provides the highest average movie ratings when split into genre groups.
movie_info['genre_mean_score']=movie_info.groupby('genre')['score'].transform('mean')
movie_info=movie_info.sort_values(['genre_mean_score'],ascending=False)
print(movie_info['genre'][0])

#6. Provide a table with the average rating of a movie by each genre group along with the movie title.
table=pd.pivot_table(movie_info, values='score',index=['genre','title'])
print(table)