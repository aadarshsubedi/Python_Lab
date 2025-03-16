#cineb.net
import pandas as pd
data1={
    'Name': ['Jai','Prince','Gaurav','Amuj'],
    'Address': ['Nagpur','Kanpur','Allahabad','Kannauaj'],
    'Age': [27,24,22,32],
    'Qualification': ['Btech','B.A','Bcom','B.Homs'],
}
data2={
    'Name': ['Abhi','Ayushi','Dhiraj','Hitesh'],
    'Address': ['Nagpur','Kanpur','Allahabad','Kannauaj'],
    'Age': [17,14,12,52],
    'Qualification': ['Btech','B.A','Bcom','B.Homs'],
}
df=pd.DataFrame(data1,index=[0,1,2,3])
df1=pd.DataFrame(data1,index=[54,5,6,7])
#print(df,"\n\n",df1)

#print(pd.concat([df,df1]))
#print(df.join(df1,how='inner'))
print(pd.concat([df, df1], axis=1,ignore_index=True ,join='outer'))
