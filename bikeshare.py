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
    city_list = ['chicago','new york city', 'washington']
    city = input('Please enter the city to analyze (chicago, new york city, washington\n) :').lower()
    while city not in city_list:
        print('Please enter a valid city')
        city = input('Please enter the city to analyze (chicago, new york city, washington\n) :').lower()
        
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input('Please enter a month:(january,february,march,april,may,june,all) ').lower()
        if month in month_list :
            break
        else:
            print('please enter a valid month')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    while True:
        day = input('please enter a day: (sunday,monday,tuesday,wednesday,thursday,friday,saturday,all) ').lower()
        if day in day_list:
            break
        else:
            print('please enter a valid day')

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
    
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january','february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
        
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
         
    return df  
      
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    import statistics
    print('The most common month is : ',format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    import statistics
    print('The most common day is : ',format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    import statistics
    print('The most common start hour is :',format(df['start hour'].mode()[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    import statistics
    print('The most common start station is :',format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
                                                     
    print('The most common end station is:{}',format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['popular_trip']=df['Start Station']+","+df['End Station']
    print('The most popular trip is :{}',format(df ['popular_trip'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time :',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('mean travel time : ',(df['Trip Duration'].mean()).round())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts().to_frame)

    # TO DO: Display counts of gender
    
    
    if city != 'washington':
        gender_count = df['Gender'].value_counts().to_frame()
        print(gender_count)
    else:
        print('No data available in Washington City for Gender')
    # TO DO: Display earliest, most recent, and most common year of birth
    
    if city != 'washington':
        
        print('The earliest year of birth is : ',int(df['Birth Year'].min()))
        print('The most recent year of birth is : ',int(df['Birth Year'].max()))
        print('The most common year of birth is : ',int(df['Birth Year'].mode()[0]))
    else:
        print('No data available in Washington City for Birth Year')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    # TO DO: Prompt the user to view 5 lines of raw data
    print('\nView 5 lines of raw data\n')
        
    i=0
    raw = input('Please would you like to view 5 rows of raw data?,(Please enter yes or no)\n:').lower()
    if raw not in ['yes','no']:
        print('Invalid response, Please enter yes or no')
        raw = input('Please would you like to view 5 rows of raw data?,(Please enter yes or no)\n:').lower()
    elif raw != 'yes':
        print('Have a nice day')
              
    else:
         while i+5 < df.shape[0]:
             print(df.iloc[i:i+5])
             i += 5
             raw = input ('Please would you like to view more 5 lines of raw data?(Please enter yes or no)\n:').lower()
             if raw == 'no':
                 print('Have a nice day...')
                 break
                  
        
           
                        
        
                                 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break           
            


if __name__ == "__main__":
	main()
