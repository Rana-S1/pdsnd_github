import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city =input("Please enter the CITY NAME : " ).lower()
        if city == 'chicago' or city == 'washington' or city == 'new york city' :
            break
        else:
            print('Invalid input .. try again and chose :chicago or new york city or washington')
 
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month =input("Please enter the month : " ).lower()
        if month == 'all' or month == 'january' or month == 'february' or month == 'march' or \
           month == 'april' or month == 'may' or month == 'june':
             break
        else:
            print('Invalid input .. try again and choes: all, january, february, ... , june')
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('Please enter the day of the week : ').lower()
        if day == 'all' or day=='monday' or day=='tuesday' or day=='wednesday' or \
           day=='thursday' or day=='friday' or day=='saturday' or day=='sunday':
            break
            
        else:
            print('Invalid input .. try again and chose: all, monday, tuesday, ... sunday')

    print('*'*50)
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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
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

    # TO DO: display the most common month
    common_month=df['month'].mode()[0] 
    print('Most frequent month of travel is', common_month)

    # TO DO: display the most common day of week
    common_day=df['day_of_week'].mode()[0] 
    print('Most frequent day of travel is',common_day)


    # TO DO: display the most common start hour
    common_hour=df['hour'].mode()[0] 
    print('Most frequent hour of travel is',common_hour)
    


    ask=True
    i=0
    j=5

    while (ask):
        user_answer=input('Do you want print 5 rows? yes or no : ')
        if df.empty:
            print('No more data to display')
            break
            
        elif user_answer.lower()=='no':
            print('Thank you')
            break
      
        elif user_answer.lower()=='yes':
            print(df.iloc[i:j])
            i+=5
            j+=5
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_start_station=df['Start Station'].mode()[0]
    print('Most commonly used start station is: ',commonly_start_station)

    # TO DO: display most commonly used end station
    commonly_end_station=df['End Station'].mode()[0]
    print('Most commonly used end station is: ',commonly_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combination_start_end = df['Start To End'].mode()[0]
    print('Most frequent combination of start station and end station trip is: ' , combination_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total travel time is = ',total_travel)

    # TO DO: display mean travel time
    mean_travel=df['Trip Duration'].mean()
    print('mean travel time is = {} '.format(mean_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type=df['User Type'].value_counts()
    print('Counts of user types is:\n',format(count_user_type,',d'))
    print('\n')
    
    # TO DO: Display counts of gender
    if 'Gender' in df:
        
        # Only access Gender column in this case
        count_gender=df['Gender'].value_counts()
        print('Counts of gender is:\n',format(count_gender,'8,d'))
        print('\n')
    
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
    
    
    # TO DO: Display earliest, most recent, and most common year of birth
    
    if 'Birth Year' in df:
        
        earliest_year_of_birth=df['Birth Year'].min()
        print('Earliest year of birth is =',earliest_year_of_birth)
    
        recent_year_of_birth=df['Birth Year'].max()
        print('Recent year of birth is =',recent_year_of_birth)
    
        common_year_of_birth=df['Birth Year'].mode()[0]
        print('Common year of birth is =',common_year_of_birth)
        
    else:
        print('Birth Year cannot be calculated because Birth Year does not appear in the dataframe')    


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
