import pandas as pd
import numpy as np

month_se = pd.Series(['1월', '2월', '3월', '4월'])
income_se = pd.Series([9_500, 6_200, 6_050, 7_000])
expenses_se = pd.Series([5_040, 2_350, 2_300, 4_800])
df = pd.DataFrame({'월': month_se, '수익': income_se, '지출': expenses_se})

print(df)
print(np.argmax(income_se))
print(month_se[np.argmax(income_se)])
print(df['수익'].max())
print(df['수익'].mean())
print(df.columns)
print(df.index)
