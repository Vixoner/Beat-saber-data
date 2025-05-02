import pandas as pd 
import json

from generate_linear_graphs import generate_linear_graphs
from generate_glm import generate_glm
from generate_svr import generate_svr
from remove_outliers import remove_outliers
from generate_heatmap import generate_heatmap
from generate_attribute_stats import generate_attribute_stats
from generate_histograms import generate_histograms
from data_processer import process
    
def main():
    # Wczytanie pliku z danymi
    with open('beatleader_rawdata.json', 'rb') as f:
        data = json.load(f)
    
    # Wstępne przetwarzanie
    data_df = pd.DataFrame(process(data))

    # Sprawdzenie czy nie ma wartości NULL
    print(data_df.info())

    generate_attribute_stats(data_df)  # Generowanie statystyk atrybutów
    generate_histograms(data_df)   # Generowanie histogramów atrybutów
    generate_heatmap(data_df)   # Generowanie macierzy korelacji zmiennych

    # Porzucenie 'Zagrania S'
    data_df = data_df.drop(['sPlays'], axis=1)
    
    # Usunięcie wartości odstających
    data_df = remove_outliers(data_df, 3)
    
    generate_linear_graphs(data_df)    # Generowanie danych i wykresów modelu liniowego
    generate_glm(data_df)   # Generowanie danych i wykresów modelu glm
    generate_svr(data_df)  # Generowanie danych modelu SVR


if __name__ == "__main__":
    main()