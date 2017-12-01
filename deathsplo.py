import numpy as np
import matplotlib.pyplot as plt
import MySQLdb
import pandas as pd

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="kanna123",
                     db="15-19dataset")

cursor = db.cursor()

# Execute SQL select statement
sql="SELECT `ISO3`,`Male_data`,`Female_Data` FROM `Deaths` "
cursor.execute(sql)
rows=cursor.fetchall()
#Transforming data into DataFrames
df=pd.DataFrame([[j for j in i] for i in rows])
#ypos=df.groupby(df[1])[1].count()
df1=df.iloc[:50,:]
print df1
X = np.arange(len(df1[0]))
men=df1[1]
women=df1[2]
width=0.35
lst = df1[0].values[0:]
p1 = plt.bar(X, men ,width, color='g')
p2 = plt.bar(X, women, width,color='#98FB98',bottom=men)
print(lst)

plt.ylabel('percent of Deaths')
plt.title('Deaths by gender')
plt.xticks(X,lst,rotation=90)
#plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()

'''import matplotlib.pyplot as plt

A = [5., 30., 45., 22.]
B = [5., 25., 50., 20.]

X = range(4)

plt.bar(X, A, color = 'b')
plt.bar(X, B, color = 'pale green', bottom = A)
plt.show()'''
