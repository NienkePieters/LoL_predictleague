import os
import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    df = df.dropna(subset=["target"])

    #drop rows with negative values for earned gpm
    #drop rows with dpm values above 3000
    df = df.drop(df.index[df['earned gpm'] < 0])
    df = df.drop(df.index[df['dpm'] > 3000])

    df = df[['year', 'league','result', 'playername','target']]

    bestleagues = ["EU LCS", "NA LCS", "LMS", "LEC", "LCS", "LCK", "LPL", "PCS", "NA CS", "EU CS", "KeSPA", "LSPL", "LCK CL", "DC", "NASG", "Proving Grounds Circuit", "LVP DDH", "LFL", "LDL", "GPL", "EM", "LCSA"]
    #drop all games of people that did not play at least 1 game in these leagues
    keep_list = []
    for person in df['playername'].unique():
        #put person on keep_list if at least one of his matches was in the bestleagues
        if len(df.loc[df['playername']==person,['league']][df['league'].isin(bestleagues)]) > 0:
            keep_list.append(person)
    # drop people that did not play in the bestleagues
    df = df[df.playername.isin(keep_list) == True]

    return pd


