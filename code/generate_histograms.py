import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 

def generate_histograms(data_df: pd.DataFrame):    
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
        plt.figure(figsize=(12, 8))
        sns.histplot(data_df, x=column, bins=25, edgecolor='white')
        plt.xlabel(translate_dict[column])
        plt.ylabel('Liczba graczy')
        plt.show()