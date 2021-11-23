import pandas as pd

df = pd.DataFrame({'animal': ['alligator', 'bee', 'falcon', 'lion',
                   'monkey', 'parrot', 'shark', 'whale', 'zebra']})
df2 = pd.DataFrame([[33,]*10])
df3 = pd.read_csv('C:\\Users\\valer\\OneDrive\\Desktop\\PDS\\luna7\\apr01_2019.csv')
#print(df2)
print(df3.shape)
print(df3.head())
############################################
df3.info(verbose=False, memory_usage="deep")
df3_2 = df3[["jdate", "last_az_cmd"]]
df3_2.info(verbose=False, memory_usage="deep")
df3.describe()