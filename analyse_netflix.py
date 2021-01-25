import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('~/Downloads/ViewingActivity-sample.csv')
#access the csv file, replace after the / with your file name
df = df.drop(['Profile Name', 'Attributes', 'Supplemental Video Type', 'Device Type', 'Bookmark', 'Latest Bookmark', 'Country'], axis=1)
#remove unnecessary comments
df['Start Time'] = pd.to_datetime(df['Start Time'], utc=True)
df = df.set_index('Start Time')
df.index = df.index.tz_convert('Europe/London')
#convert so everything is on the same timezone, replace with your timezone
#list of timezones: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
df = df.reset_index()
df['Duration'] = pd.to_timedelta(df['Duration'])
check_tv_show = input("Enter a tv show: ")
tv_show = df[df['Title'].str.contains(check_tv_show, regex=False)]
#change the office to whichever tv show you would like to analyse

tv_show = tv_show[(tv_show['Duration'] > '0 days 00:01:00')]

tv_show['weekday'] = tv_show['Start Time'].dt.weekday
tv_show['hour'] = tv_show['Start Time'].dt.hour

tv_show['weekday'] = pd.Categorical(tv_show['weekday'], categories= [0,1,2,3,4,5,6], ordered=True)

tv_show_by_day = tv_show["weekday"].value_counts()
tv_show_by_day = tv_show_by_day.sort_index()
#shows how much you watch a show per day


tv_show_by_day.plot(kind="bar", figsize=(20,10), title = "{0} Episodes watched per day".format(check_tv_show))
plt.show()
tv_show['hour'] = pd.Categorical(tv_show['hour'], categories=
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
    ordered=True)


tv_show_by_hour = tv_show['hour'].value_counts()


tv_show_by_hour = tv_show_by_hour.sort_index()


tv_show_by_hour.plot(kind='bar', figsize=(20,10), title='Office Episodes Watched by Hour')

print(tv_show_by_day)