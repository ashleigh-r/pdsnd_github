import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    person = input('\nWelcome! What is your name?\n')
    greeting = '\nHello, {}! Let\'s take a look at some US bikeshare data!'.format(person)
    print(greeting)

    cities = ['chicago', 'new york', 'washington']
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june',
              'july', 'august', 'september', 'october', 'november', 'december']
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nWould you like to see data for Chicago, New York, or Washington?\n').lower()
        if city not in cities:
            print('\nNot a valid city. Please try again.')
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nPlease select a month to continue (e.g. January or all).\n').lower()
        if month not in months:
            print('\nNot a valid month. Please reenter your response.')
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nWhat day of the week are you interested in (e.g. Sunday or all)?\n').lower()
        if day not in days:
            print('\nNot a valid day. Please try again.')
        else:
            break

    print('-'*40)
    return city, month, day

def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to alyze
59
        (str) month - name of the month to filter by, or "all" to apply no month filter
60
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
61
    Returns:
62
        df - Pandas DataFrame containing cityfilter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june',
                  'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day:', popular_day)

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', popular_station)

    # display most commonly used end station
    popular_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', popular_station)

    # display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'] + ' ' 'to' ' ' + df['End Station']
    frequent_trip = df['Start End'].mode()[0]
    print('Most Popular Trip:', frequent_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total = df['Trip Duration'].sum()
    print('Total Travel Time:', total)

    # display mean travel time
    mean = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if 'Gender' not in df.columns:
        print('\nGender column does not exist.\n')
    else:
        gender = df['Gender'].value_counts()
        print('\nCounts of Gender:\n', gender)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df.columns:
        print('Birth column does not exist.')
    else:
        popular_dob = df['Birth Year'].mode()[0]
        min_dob = df['Birth Year'].min()
        max_dob = df['Birth Year'].max()

        print('\nMost Common Date of Birth:', popular_dob)
        print('\nEarliest Date of Birth:', min_dob)
        print('\nMost Recent Date of Birth:', max_dob)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):

    """Asks user if they would like to see raw data."""

    raw_data = input('\nWould you like to see 5 lines of raw data? Please enter yes or no.\n').lower()
    if raw_data in 'yes':
        x = 0

        while True:
            print(df.iloc[x:x+5])
            x += 5

            more_data = input('\nWould you like to see 5 more lines of raw data? Enter yes or no.\n').lower()
            if more_data != 'yes':
                break

def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to start over and explore more data? Please enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
