import pandas as pd

df = None

def cleanword(word):

    global df
    try:
        df = pd.read_csv('../data/aceventura.txt, encoding=latin1')
        print("data loaded")
    except FileNotFoundError:
        print("data not loaded")
    return df

cleanword(df)