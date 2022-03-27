import pandas as pd
import openpyxl

varInputDataFile = "sample_data.csv"

#--------------------------------------------------------------------
## Make sample input data file.
#--------------------------------------------------------------------
df = pd.DataFrame([   ["홍길동", "https://www.google.com"]
                    , ["김이박", "https://www.naver.com"]
                    , ["김수한모거북이와두루미", "github.com"] ]
                    , columns=['NAME', 'URL'])
print(df)
df.to_csv(varInputDataFile, mode='w', index=False)

