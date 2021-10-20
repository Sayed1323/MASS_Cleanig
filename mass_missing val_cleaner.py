import pandas as pd
file_input = str(input("place the file:"))
if not ".csv" in file_input:
    file_input += ".csv"
data = pd.read_csv(file_input)
print(data.shape)
###################CLEANING ROWS###########################################
more_than = int(input("max count of missing values per row:"))
a = (data[data.isnull().sum(1) >= more_than])
data = data.drop(a.index, axis=0)
##########################CLEANING COLUMNS#################################
col_nul_vals = data.isnull().sum()
shape = data.shape
percent_nul_vals = (col_nul_vals/shape[0])*100
A= (percent_nul_vals >= 80)
B = dict(A)
C = []
for i in B:
    if B[i] == 1:
        C.append(i)
data.drop(C, axis=1, inplace=True)
print(data.shape)