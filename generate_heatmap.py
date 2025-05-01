import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 

def generate_heatmap(data_df: pd.DataFrame):
    corr = data_df.corr()

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

    corr.rename(columns=translate_dict, index=translate_dict, inplace=True)

    # Rysowanie wykresu heatmap
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="plasma", vmin=-1, vmax=1)
    plt.xticks(rotation=80)
    plt.yticks(rotation=0)
    plt.show()