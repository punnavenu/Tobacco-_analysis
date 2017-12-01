import MySQLdb
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


# Connect
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="kanna123",
                     db="15-19dataset")

cursor = db.cursor()

# Execute SQL select statement
sql="SELECT `ISO3`,`Male`,`Female` FROM `Agegroup` "
cursor.execute(sql)
rows=cursor.fetchall()
#Transforming data into DataFrames
df=pd.DataFrame([[j for j in i] for i in rows])
#ypos=df.groupby(df[1])[1].count()
df1=df.head(25)
print df1
fig, ax=plt.subplots()


#values = ypos.values
#print values

#objects=["NA","VERY_LOW","LOW","MEDIUM","HIGH","VERY_HIGH"]

#count=np.arange(len(objects))

#explode = (0.5, 0, 0, 0,0,0)

#bar graph 
#plt.pie(values,labels=df)
y_pos = np.arange(len(df1[2]))

bar_width=0.35
opacity=0.4
error_config={'ecolor':'0.3'}
male=df1[1]
female=df1[2]

ax.bar(y_pos,female,bar_width,align='center', color='r',alpha=opacity,label="female",error_kw=error_config)
#performance = [10,8,6,4,2,1]
ax.bar(y_pos+bar_width, male , bar_width ,align='center', color='b',alpha=opacity,label="male",error_kw=error_config)

#plt.bar(y_pos, df1[0], align='center', alpha=0.5,label="1-100")
plt.xticks(y_pos,df1[0])
plt.ylabel(' percentage of Smoking population ')
plt.xlabel('Country')
plt.title('smoking percentage above 15')
plt.legend()
plt.show()

#plt.xticks(count,objects)
#plt.xlabel("SEVERITY")
#plt.ylabel("NO OF COUNTRIES")
#plt.show()



# Close the connection


db.close()
