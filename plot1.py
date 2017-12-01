import MySQLdb
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


# Connect
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="kanna123",
                     db="TOBACCO CONTROL")

cursor = db.cursor()

# Execute SQL select statement
sql="SELECT `TA5_Data`,`ISO3` FROM `consumption` "
cursor.execute(sql)
rows=cursor.fetchall()
#Transforming data into DataFrames
df=pd.DataFrame([[j for j in i] for i in rows])
#ypos=df.groupby(df[1])[1].count()
df1=df.head(30)
print df1


#values = ypos.values
#print values

#objects=["NA","VERY_LOW","LOW","MEDIUM","HIGH","VERY_HIGH"]

#count=np.arange(len(objects))

#explode = (0.5, 0, 0, 0,0,0)

#bar graph usi
#plt.pie(values,labels=df)
y_pos = np.arange(len(df1[0]))
#performance = [10,8,6,4,2,1]
 
plt.bar(y_pos, df1[0], align='center', alpha=0.5,label=1-4000)
plt.xticks(y_pos, df1[1])
plt.ylabel('SEVERITY')
plt.title('tobacco usage')
plt.legend('con')
 
plt.show()

#plt.xticks(count,objects)
#plt.xlabel("SEVERITY")
#plt.ylabel("NO OF COUNTRIES")
#plt.show()



# Close the connection


db.close()
