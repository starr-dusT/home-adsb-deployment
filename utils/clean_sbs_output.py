import pandas as pd     
import numpy as np
import sys

col_nums = [4,6,7,10,11,12,13,14,15,17]
col_names = ["ID", "DATE", "TIME", "CALLSIGN", "HGT", "GS", "THD", "LAT", "LON", "SQAUWK"]

df = pd.read_csv(sys.argv[1], header=None, usecols=col_nums,names=col_names)

# preprocess csv
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x) # remove extra spaces
df = df.applymap(lambda x: np.nan if x == "" else x) # replace empty strings with null

# map callsign to all records with ID
call_map = df[df["CALLSIGN"].notna()].set_index("ID")["CALLSIGN"].to_dict()
df["CALLSIGN"] = df["ID"].map(call_map)
df = df[df["CALLSIGN"].notna()] # drop tracks with no callsign

sqwk_map = df[df["SQAUWK"].notna()].set_index("ID")["SQAUWK"].to_dict()
df["SQAUWK"] = df["ID"].map(sqwk_map)

# foward fill certain columns of data
int_cols = ["HGT", "GS", "THD", "SQAUWK"]
df[int_cols] = df.groupby("CALLSIGN")[int_cols].ffill()

# drop columns without new lat/lon data
df = df[df["LAT"].notna()]

# create various time and index cols needed for desired format
df["dt"] = pd.to_datetime(df["TIME"], format="%H:%M:%S.%f")
df["SECS"] = df["dt"].dt.hour * 3600 + df["dt"].dt.minute * 60 + df["dt"].dt.second + df["dt"].dt.microsecond / 1e6
df["HMS"] = df["TIME"].str.replace(":", "", regex=False) 
df["INDEX"] = (df.groupby("CALLSIGN").cumcount() + 1).astype(int)
df["ELAPS"] = df.groupby("CALLSIGN")["SECS"].transform(lambda x: x - x.iloc[0]).round(2)

output_df = df[["ID", "CALLSIGN", "SQAUWK", "HMS", "ELAPS", "INDEX", "LAT", "LON", "HGT", "GS", "THD"]]
output_df.to_csv(sys.argv[2], index=False)
