import time
import pandas as pd
import numpy as np
import csv
import datetime
from datetime import date
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april',
        'may', 'june']

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',
        'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
   
    cities = ''
    for item in CITY_DATA:
        if cities == '':
            cities += item.title()
        else:
            cities += ', ' + item.title()
 
    city = input('Please enter one of the following cities: {}\n'.format(cities)).lower()
    while city not in CITY_DATA:
        city = input('Invalid input. ' +
                    'please enter one of the following cities:\n{}\n'.format(cities)).lower()
 
    
#     print('***********************start**********************') 
    data_display = input('Would you like to show the first 5 rows of the data-> Yes or NO \n').lower()
    newcity= city+'.csv'
    if(datadisplay == 'yes'):
        
        with open(newcity, 'r') as file:
            reader = csv.reader(file)
            line_count = 0
            for row in reader:
                if line_count <= 5:
                    line_count = line_count+1
                    print(row)
            line_count = 0
#     print('***********************End**********************') 
    
    x = ''
    for item in months:
        if x == '':
            x += item
        else:
            x += ', ' + item.title()
 
    month = input('Please enter one of the following to filter by month:\n{}\n'.format(x)).lower()
    while month not in months and month != 'all':
        month = input("\nInvalid selection. " +
                      "Please enter one of the following options to filter by month. " +
                      "\n(All, {})\n".format(x)).lower()
 
    tempmonth= month
    month_num = datetime.datetime.strptime(month, '%B').month
    if month_num <10:
        
        month_num= str( month_num)
        month = '-0'+month_num+'-'
    else:
        month_num= str( month_num)
        month = '-'+month_num+'-'
    newMonth=[]    
    with open(newcity, 'r') as file:
            reader = csv.reader(file)
            line_count = 0
            data_display = input('Would you like to show the first 5 rows of the data-> Yes or NO \n').lower()
            if(datadisplay == 'yes'):
                for row in reader:
    #                 print('start')
                    if month in row[1]:
                        if line_count <=+ 5:
                            line_count = line_count+1
                            print(row)
                line_count = 0

          #If the string you want to search is in the row
#             print("String found in first row of csv")
#         break

    x = ''
    for item in days:
        if x == '':
            x += item.title()
        else:
            x += ', ' + item.title()
 
    day = input('Please enter one of the following to filter by day:\nAll, {}\n'.format(x)).lower()
    while day not in days and day != 'all':
        day = input("\nInvalid selection. " +
                    "Please enter one of the following options to filter by day." +
                    "\n(All, {})\n".format(x)).lower()
 
#     month_num = datetime.datetime.strptime(month, '%B').month
#     if month_num <10:
        
#         month_num= str( month_num)
#         month = '-0'+month_num+'-'
#     else:
#         month_num= str( month_num)
#         month = '-'+month_num+'-'
#     newMonth=[]    
    with open(newcity, 'r') as file:
            reader = csv.reader(file)
            line_count = 0
            datadisplay = input('Would you like to show the first 5 rows of the data-> Yes or NO \n').lower()
            newcity= city+'.csv'
            if(datadisplay == 'yes'):
                for row in reader:
    #                 print('start')
                    if month in row[1]:
                            li=list(row[1].split(" "))
                            li=li[0]
                            df = pd.Timestamp(li)
#                             print('start')
#                             print(day)
                            y=df.weekday_name
                               
                            y.replace(" ", "")
                            day.replace(" ", "")
                            if day == y:
                                if line_count <= 5:
                                    print(df.day_name)
                                    line_count = line_count+1
                                else:
                                    print('not found')
                    line_count = 0

    print('-'*40)
    month= tempmonth
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
 
    df = pd.read_csv(CITY_DATA.get(city))
 
    if 'Start Time' in df.columns:
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        if month != 'all':
            df = df[df['month'] == (months.index(month) + 1) ]
 
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
 
    if 'End Time' in df.columns:
        df['End Time'] = pd.to_datetime(df['End Time'])
 
    print('\nFILTER SECTION:\nCity: {}\nMonth: {}\n Day: {}'.format(city, month, day))
 
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nThe Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('Most common month', common_month)

    df['day_of_week'] = df['Start Time'].dt.weekday_name
    frequent_day = df['day_of_week'].mode()[0]
    print('Most frequent day', frequent_day)

    df['Start_hour'] = df['Start Time'].dt.hour
    frequent_hour = df['Start_hour'].mode()[0]
    print('Most frequent hour', frequent_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    df['Start Station'].mode()[0]

    df['Start Station'].mode()[0]

    df['Combined Trip Station'] = df['Start Station'] + 'travelling to ' + df['End Station']
    combined_stations = df['Combined Trip Station'].mode()[0]
    print(combined_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nTrip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print('Total time travelled', total_travel_time)

    mean_travel_time = df['Trip Duration'].mean()
    print('Average time travelled', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print(user_types)

    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print('There is no gender information')

    if 'Birth Year' in df:
        earliest = df['Birth Year'].max()
        print(earliest)
        most_recent = df['Birth Year'].min()
        print(most_recent)
        common_year_birth = df['Birth Year'].mode()[0]
        print(common_year_birth)
    else:
       print('There is no year of birth')
   


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
