import pandas as pd
import glob
import os
import numpy as np
df=pd.read_csv('rupiall.txt',header=None,error_bad_lines=False)
df.dropna()
shuffle=df.reindex(np.random.permutation(df.index))
df.to_csv('rupi.csv',index=None)
shuffle.to_csv('valid.csv',index=None)
print(df.shape,shuffle.shape)




