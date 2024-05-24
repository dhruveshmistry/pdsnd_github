import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['all','january', 'february', 'march', 'april', 'may', 'june']

days = ['all','saturday', 'sunday','monday', 'tuesday', 'wednesday', 'friday']
 
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s dive into US bikeshare data!')
    #assign initial values of strings city, month and day to empty string
    city_input=''
    month_input=''
    day_input=''
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city_input.lower() not in CITY_DATA:
        city_input = input("\nWhat's the name of the city? e.g., chicago, new york city, washington\n")
        if city_input.lower() in CITY_DATA:
            #get the name of the city
            city = CITY_DATA[city_input.lower()]
            
        else:
            #wrong input for the name of city
            print("Invalid entry, Please select from chicago, new york city, washington.\n")

    # get user input for month (all, january, february, ... , june)
    
    while month_input.lower() not in months:
        month_input = input("\nWhich month's data would you like to analyse? Choose 'all' or  january, february, march, april, may, june\n")
        if month_input.lower() in months:
            #get the month
            month = month_input.lower()
        else:
            #wrong input for the month
            print("Invalid entry, Please select from, 'all' or january, february, march, april, may, june.\n")


    # get user input for day of week (all, monday, tuesday, ... sunday)
   
    while day_input.lower() not in days:
        day_input = input("\nWhich day's data would you like to analyse? Select from 'all' or monday, tuesday, wednesday, thursday, friday, saturday, sunday\n")
        if day_input.lower() in days:
            
            day = day_input.lower()
        else:
            
            print("Invalid entry, Please enter 'all' or monday, tuesday, wednesday, thursday, friday, saturday, sunday\n")

    print('-'*40)
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
    # load data file into a dataframe
    df = pd.read_csv(city)
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df["day_of_week"] =df["Start Time"].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month)
        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]

    return df

def display_raw_data(df):
    """
    Displays raw data upon user request.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    start = 0
    end = 5

    display = input("\nWould you like to view individual trip data? Type 'yes' or 'no'\n").lower()

    if display == 'yes':
        while end <= df.shape[0] - 1:
            print(df.iloc[start:end,:])
            start += 5
            end += 5
            display = input("\nWould you like to continue? Type 'yes' or 'no'\n").lower()
            if display == 'no':
                break

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    
    print('Most commen month is : {} '.format(df['month'].mode()[0]))
    
    # display the most common day of week
    
    print("Most common day is: " + str(df['day_of_week'].mode()[0]))

    # display the most common start hour
     
    print("Most common start hour is: " + str(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (round(time.time() - start_time, 2)))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station is: {}".format(common_start_station))

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("Most commonly used end station is: {}".format(common_end_station))

    # display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("Most frequent combination of start station and end station trip is : " + str(frequent_combination.split("||")))

    print("\nThis took %s seconds." % (round(time.time() - start_time, 2)))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is: {}".format(str(total_travel_time)))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time is: {}".format(str(mean_travel_time)))

    print("\nThis took %s seconds." % (round(time.time() - start_time, 2)))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Count of user types: {} \n".format(str(user_types)))

    # Display counts of gender
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        gender = df['Gender'].value_counts()
        print("Count of user gender: {} \n".format(str(gender)))

        # Display earliest, most recent, and most common year of birth
        
        earliest_birth = int(df['Birth Year'].min())
        most_recent_birth = int(df['Birth Year'].max())
        most_common_birth = int(df['Birth Year'].mode()[0])
        print('Earliest birth: {}\n'.format(earliest_birth))
        print('Most recent birth: {}\n'.format(most_recent_birth))
        print('Most common birth: {}\n'.format(most_common_birth))


    print("\nThis took %s seconds." % (round(time.time() - start_time, 2)))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

    
# The dataframe function is based on code found at: https://github.com/Moamen-Jamal/US-Bikeshare-Project/blob/5c4860b31f7153721b8d1e1c869bb6d731a6c062/bikeshare_2.py