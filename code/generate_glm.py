import matplotlib.pyplot as plt 
import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
from sklearn.model_selection import train_test_split
import math
from sklearn.preprocessing import PolynomialFeatures

def generate_glm(data_df: pd.DataFrame):
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
            X = data_df[column].values
            Y = data_df['rank'].values

            X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, shuffle=True)

            train_sorted_indices = np.argsort(X_train)
            X_train_sorted = X_train[train_sorted_indices]
            Y_train_sorted = Y_train[train_sorted_indices]

            test_sorted_indices = np.argsort(X_test)
            X_test_sorted = X_test[test_sorted_indices]
            Y_test_sorted = Y_test[test_sorted_indices]

            plt.figure(figsize=(10, 6))
            plt.scatter(X_train_sorted, Y_train_sorted, label='Dane treningowe', alpha=0.5)
            plt.scatter(X_test_sorted, Y_test_sorted, label='Dane testowe', edgecolor='black', facecolor='none')

            r2_GLM2, mse_GLM2 = add_glm(2, 'red', X_train_sorted, Y_train_sorted, X_test_sorted, Y_test)
            r2_GLM3, mse_GLM3 = add_glm(3, 'pink', X_train_sorted, Y_train_sorted, X_test_sorted, Y_test)
            r2_GLM4, mse_GLM4 = add_glm(4, 'purple', X_train_sorted, Y_train_sorted, X_test_sorted, Y_test)

            plt.legend(prop={'size': 10})
            plt.xlabel(translate_dict[column])
            plt.ylabel('Ranga')
            plt.ylim([Y.min(), Y.max()])
            plt.show()

            print(f'Atrybut: {column}:')
            print(f'R^2: {r2_GLM2:0.3} MSE: {mse_GLM2:0.9} RMSE: {math.sqrt(mse_GLM2):0.6}')
            print(f'R^2: {r2_GLM3:0.3} MSE: {mse_GLM3:0.9} RMSE: {math.sqrt(mse_GLM3):0.6}')
            print(f'R^2: {r2_GLM4:0.3} MSE: {mse_GLM4:0.9} RMSE: {math.sqrt(mse_GLM4):0.6}')

            #print(f'{r2_GLM2:0.3} {mse_GLM2:0.9} {math.sqrt(mse_GLM2):0.6}')
            #print(f'{r2_GLM3:0.3} {mse_GLM3:0.9} {math.sqrt(mse_GLM3):0.6}')
            #print(f'{r2_GLM4:0.3} {mse_GLM4:0.9} {math.sqrt(mse_GLM4):0.6}')


def add_glm(degree, color, X_train, Y_train, X_test, Y_test):
    model_GLM = LinearRegression()
    gen_features = PolynomialFeatures(degree=degree, include_bias=True, interaction_only=False)

    X_train_poly = gen_features.fit_transform(X_train.reshape(-1, 1))
    X_test_poly = gen_features.fit_transform(X_test.reshape(-1, 1))

    model_GLM.fit(X_train_poly, Y_train)
    y_pred = model_GLM.predict(X_test_poly)

    plt.plot(X_test, y_pred, label=f'GLM{degree}', color=color, linewidth=3)

    r2 = r2_score(Y_test, y_pred)
    mse = mean_squared_error(Y_test, y_pred)

    return r2, mse
