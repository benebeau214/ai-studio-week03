import csv
import pandas as pd

df = pd.read_csv("RAW_DATA.csv", encoding="cp949")

print(df.shape)
print(df.info())

'''
df.shape, df.info() 출력 결과

(500, 5)
<class 'pandas.DataFrame'>
RangeIndex: 500 entries, 0 to 499
Data columns (total 5 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   주문일자    500 non-null    str  
 1   상품명     500 non-null    str  
 2   카테고리    500 non-null    str  
 3   단가      500 non-null    str  
 4   수량      500 non-null    int64
dtypes: int64(1), str(4)
memory usage: 19.7 KB
None
'''

df["단가"] = (pd.to_numeric(df["단가"].astype(str).str.replace(",", ""), errors="coerce")).astype("Int64")
df["매출액"] = df["단가"] * df["수량"]
