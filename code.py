# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
#Code starts here
data = pd.read_csv(path)
#print(type(data))
#print(data.columns)
data.rename(columns={'Total':'Total_Medals'}, inplace=True)
data.head(10)


# --------------
#Code starts here
data.head()
data.columns

data['Better_Event'] = np.where(data['Total_Summer']> data['Total_Winter'],'Summer','Winter')
data['Better_Event'] = np.where(data['Total_Summer']==data['Total_Winter'],'Both',
data['Better_Event'])
print(data.head())
event_list = data['Better_Event'].value_counts().index.tolist()
better_event = event_list[0]
better_event


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]

top_countries.drop(top_countries.tail(1).index,inplace=True)

def top_ten(df,colname):
    country_list=[]
    top_10 = df.nlargest(10,colname)
    country_list = list(top_10['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')

common=[]
common_pre=[]
common_pre = [i for i in top_10_summer if i in top_10_winter]
common = [j for j in common_pre if j in top_10]
print(common)



# --------------
#Code starts here
import matplotlib.pyplot as plt

summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

summer_df.plot.bar(x='Country_Name',y='Total_Summer')
winter_df.plot.bar(x='Country_Name',y='Total_Winter')
top_df.plot.bar(x='Country_Name',y='Total_Medals')



# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']

summer_max_ratio = max(summer_df['Golden_Ratio'])
summer_country_gold = list(summer_df[summer_df['Golden_Ratio']==summer_max_ratio]['Country_Name'])[0]

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = max(winter_df['Golden_Ratio'])
winter_country_gold = list(winter_df[winter_df['Golden_Ratio']==winter_max_ratio]['Country_Name'])[0]

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = max(top_df['Golden_Ratio'])
top_country_gold = list(top_df[top_df['Golden_Ratio']==top_max_ratio]['Country_Name'])[0]

print(summer_country_gold,'s')
print(winter_country_gold,'w')
print(top_country_gold,'t')


# --------------
#Code starts here
print(data.tail(1))
data_1 = data.drop(data.iloc[-1:].index)
print(data_1.tail(1))

data_1['Total_Points'] = data_1['Gold_Total'].apply(lambda x:x*3) + data_1['Silver_Total'].apply(lambda x:x*2) + data_1['Bronze_Total'].apply(lambda x:x*1)

#data_1.reset_index(inplace=True)
most_points = max(data_1['Total_Points'])

best_country = list(data_1[data_1['Total_Points']== most_points]['Country_Name'])[0]
print(most_points)
print(best_country)





# --------------
#Code starts here
best = data[data['Country_Name']== best_country][['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()




