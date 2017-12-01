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
sql="SELECT `Year`,`AFRO`,`AMRO`,`China`,`EMRO`,`EURO`,`SEARO`,`WPRO_(excluding_China)`,`WPRO_(including_China)` FROM `Consumption12` "
cursor.execute(sql)
rows=cursor.fetchall()
#Transforming data into DataFrames
df=pd.DataFrame([[j for j in i] for i in rows])
#ypos=df.groupby(df[1])[1].count()
df1=df.head(25)
#print df1
#fig, ax=plt.subplots()


#values = ypos.values
#print values

#objects=["NA","VERY_LOW","LOW","MEDIUM","HIGH","VERY_HIGH"]

#count=np.arange(len(objects))

#explode = (0.5, 0, 0, 0,0,0)

#bar graph 
#plt.pie(values,labels=df)
#y_pos = np.arange(len(df1[0]))
# #y_pos =np.arange(len(df1[1]))
#bar_width=0.35
#opacity=0.4
#error_config={'ecolor':'0.3'}
year=df1[0]
afro=df1[1]
amro=df1[2]
euro=df1[5]
emro=df1[4]
china=df1[3]
searo=df1[6]
wpro=df1[7]
wproc=df1[8]
#print f
#print m

#ax.bar(y_pos,f,bar_width,align='center', color='b',alpha=opacity,label="female",error_kw=error_config)
#ax.bar(y_pos+bar_width,m,bar_width ,align='center', color='r',alpha=opacity,label="male",error_kw=error_config)
plt.plot(year,afro,label='afro',linewidth=4)
plt.plot(year,amro,label='amro',linewidth=3)
plt.plot(year,euro,label='euro',linewidth=3)
plt.plot(year,china,label='china',linewidth=7)
plt.plot(year,emro,label='emro',linewidth=3)
plt.plot(year,searo,label='searo',linewidth=3)
plt.plot(year,wpro,label='wpro',linewidth=3)
plt.plot(year,wproc,label='wproc',linewidth=3)
# #plt.bar(y_pos, df1[0], align='center', alpha=0.5,label="1-100")
#plt.xticks(y_pos, df1[2])
#plt.ylabel('***')
# plt.ylabel('Female percentage')
# plt.xlabel('Country')
plt.title('number of Cigarettes consumed by region')
plt.legend()
 
plt.show()

#plt.xticks(count,objects)
#plt.xlabel("SEVERITY")
#plt.ylabel("NO OF COUNTRIES")
#plt.show()



# Close the connection


db.close()
