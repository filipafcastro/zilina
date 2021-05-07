from glob import glob
import pandas as pd
import numpy as np

path_csv = r"data\traffic\*.csv"
files = glob(path_csv)

list_df = [] 
for file in files:
    df = pd.read_csv(file, delimiter=";", encoding='latin1')
    if "Dátum" in df.keys():
        continue
    df.drop(df.tail(1).index, inplace=True)
    list_df.append(df)
    
df_concat = pd.concat(list_df, ignore_index=True)
df_concat = df_concat.rename(columns = {'Dátum a èas': 'date'})
df_concat["date"] = pd.to_datetime(df_concat["date"])
df_concat['hastrip'] = np.where(df_concat['Hradza Berg ']!= 0, 1, 0)

# Get holidays info
holidays_file = r"data\holidays\holidays.csv"
holidays = pd.read_csv(holidays_file, sep=';')
holidays['date'] = (pd.to_datetime(holidays['date'], dayfirst=True)).dt.date

df_concat['is_holiday'] = 0

for i, holiday in holidays.iterrows():
    df_concat.loc[df_concat['date'].dt.date == holiday['date'], 'is_holiday'] = 1

#Get weather features
path_weather_csv = r"data\weather\*.csv"
files_weather = glob(path_weather_csv)
list_df = [] 
for file in files_weather:
    df = pd.read_csv(file)
    list_df.append(df)
df_concat_weather = pd.concat(list_df, ignore_index=True)
df_concat_weather["date"] = pd.to_datetime(df_concat_weather["date"])

df_concat_weather = df_concat_weather.drop_duplicates()
df_concat_weather["date_merge"]= df_concat_weather["date"].dt.date

df_concat["date_merge"]= df_concat["date"].dt.date
df_final =df_concat.merge(df_concat_weather, left_on="date_merge", right_on='date_merge')
df_final = df_final.rename(columns={"date_x":"date", "Hradza Berg ": "Hradza Berg", "Do Slovenska ": "Do Slovenska"})

columns_to_keep = ["date", "Hradza Berg", "Do Slovenska", "hastrip", "is_holiday", "tavg", "wspd", "pres"]
df_final = df_final[columns_to_keep]

cond = df_final["date"] > pd.Timestamp(2019, 1,1 )
df_final.loc[cond, :] = df_final.loc[cond, :].dropna()

df_final.to_csv("Berg_bicycle_counter_2016_2019.csv", index=False)

print("Finished!")