import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import math

def generate_linear_graphs(data_df: pd.DataFrame):
    translate_dict = {
        'rank': 'Ranga',
        'countryRank': 'Ranga krajowa',
        'averageAccuracy': 'Średnia celność',
        'topPp': 'Najlepsze zagranie',
        'maxStreak': 'Maksymalna seria',
        'totalPlayCount': 'Liczba zagrań',
        'totalImprovementsCount': 'Liczba poprawionych wyników',
        'top1Count': 'Liczba najlepszych wyników',
        'averageRank': 'Średnia ranga',
        'sspPlays': 'Zagrania SS+',
        'ssPlays': 'Zagrania SS',
        'spPlays': 'Zagrania S+',
        'sPlays': 'Zagrania S',
        'aPlays': 'Zagrania A',
        'watchedReplays': 'Obejrzane powtórki przez gracza',
        'replaysWatched': 'Obejrzane powtórki przez innych',
    }

    for column in data_df.columns:
        if column != 'rank':
            X = data_df[[column]].values
            Y = data_df['rank'].values
            
            model = LinearRegression()
            model.fit(X, Y)
            Y_pred = model.predict(X)
            
            r2 = r2_score(Y, Y_pred)
            mse = mean_squared_error(Y, Y_pred)
            rmse = math.sqrt(mse)

            print(f'Atrybut: {column} R^2: {r2:0.3} MSE: {mse:0.9} RMSE: {rmse:0.6}')
            #print(f'{column} {r2:0.3} {mse:0.9} {rmse:0.6}')

            plt.figure(figsize=(10, 6))
            sns.regplot(x=column, y='rank', data=data_df, scatter_kws={'s': 10}, line_kws={'color': 'red'})
            plt.xlabel(translate_dict[column])
            plt.ylabel('Ranga')
            plt.ylim([Y.min(), Y.max()])
            plt.show()
