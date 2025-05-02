import pandas as pd 
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import math
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

def generate_svr(data_df: pd.DataFrame) -> None:
    kernels = ['linear', 'poly', 'rbf']
    gammas = ['scale', 'auto']
    Cs = [10, 100, 1000, 10000]

    for kernel in kernels:
        for gamma in gammas:
            for C in Cs:
                run_svr(data_df, kernel, gamma, C)


def run_svr(df: pd.DataFrame, kernel='rbf', gamma='scale', C=1) -> None:
    X = df.drop(['rank'], axis=1)
    y = df['rank']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, shuffle=False)
    svr = SVR(kernel=kernel, gamma=gamma, C=C)
    svr.fit(X_train, y_train)
    y_pred = svr.predict(X_test)
    
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    print(f'Kernel: {kernel} Gamma: {gamma} C: {C} R^2: {r2:0.3} MSE: {mse:0.9} RMSE: {math.sqrt(mse):0.6}')
    #print(f'{C}\t{r2:0.3}\t{mse:0.9}\t{math.sqrt(mse):0.6}')

