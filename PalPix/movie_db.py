import pandas as pd

def movies():
    #set movie list database
    df = pd.read_csv('imdbtop250.txt')
    return df

#set sql engine
# eg = create_engine('sqlite://', echo=False)

# df.to_sql('title', con=eg)

# eg.execute('SELECT * FROM title').fetchall()
