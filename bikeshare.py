import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

month1 = ['january','february','march','april','may','june']   
weekday = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']   
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
    cities = []
    for city in CITY_DATA:
        cities.append(city)
        
    while True:
        try:
            city = input("Would you like to see data for chicago, new york city, or washington? ")
            if city.lower() in cities:
                print("We will show you data for {} ".format(city.capitalize()))
                break
            else:
                print("That wasn't a valid input. Please enter city from either chicago, new york city, or washington")
                continue             
                
        except ValueError:
            print("That wasn't a valid input. Please enter city from either chicago, new york city, or washington")
            continue
        else:
            break
            
    
    # TO DO: get user input for month (all, january, february, ... , june)
 
    options = ['month','day','none']
    month = 0
    day = 0
    while True:
        try:
            choice1 = input("Would you like to filter the data by month, day, or not at all? Please enter 'none' for no filter: ")  
            if choice1.lower() in options:
                print("We will filter data by : {}".format(choice1.capitalize()))
                break
            else: 
                print("Please enter a valid value: Please enter if you Would like to filter the data by month, day, or not at all? Please enter 'none' for no filter: ")
                continue
        except ValueError:
            print("Please enter a valid value: Please enter if you Would like to filter the data by month, day, or not at all?: ")
            
    while True:
        try:
            if choice1.lower() == 'month':
                try:
                    month_choice = input("Which month - january, february, march, april, may, or june?: ")
                    if month_choice.lower() in month1:
                        month = month_choice.lower()
                        print("We will filter data by : {}".format(month.capitalize()))
                        break
                    else:
                        print("Please enter valid month from - january, february, march, april, may, or june")
                        continue
                except ValueError:
                    print("enter valid value")
                    continue

            elif choice1.lower() == 'day':
                try:
                    day_choice = input("Which day - Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday?: ")
                    if day_choice.capitalize() in weekday:
                        day = day_choice
                        print("We will filter the data by {}".format(day.capitalize()))
                        break
                    else:
                        print("Please enter valid day from - Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday")
                        continue
                except ValueError:
                    print("enter valid value")
                    continue

            elif choice1 == 'none':
                print("We will not filter the data")
                break

        except ValueError:
            print("Please specify - month or day or none")
            continue
                        
# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    print('-'*40)
    return city, month, day

                                     
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
        """


def load_data(city, month, day):
    filename = CITY_DATA.get(city.lower())
    df1 = pd.read_csv(filename) 
    df = pd.read_csv(filename)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    #print(df['month'].unique())
    df['day'] = df['Start Time'].dt.weekday_name
    #print(df['day'].unique())
    df['hour'] = df['Start Time'].dt.hour
    if month != 0:
        month = month1.index(month) + 1
        df = df[df['month'] == month]
        df.head()
    else:
        df = df
    if day != 0:
        df = df[df['day'] == day.capitalize()]
    else:
        df = df
    while True:
        x = input("Before filtering data and showing you stats related to data, would you like to see 5 raw lines of data ? - Input Yes or No: ")
        if x.capitalize() == 'Yes':
            print(df1.head())
            continue
        elif x.capitalize() == 'No':
            break
        else:
            print("Please enter valid input - Would you like to see 5 raw lines of data ? - Input Yes or No: ")
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    busy_month = df['month'].mode()[0]
    busy_month1 = month1[busy_month-1].capitalize()
    print("The most common month is: {}\n".format(busy_month1))
    # TO DO: display the most common day of week
    busy_day = df['day'].mode()[0]
    print("The most common day of week is: {}\n".format(busy_day))

    # TO DO: display the most common start hour
    busy_hour = df['hour'].mode()[0]
    print("The most common start hour is: {}:00:00\n".format(busy_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    df.fillna(0)
    # TO DO: display most commonly used start station
    popular_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is : {}".format(popular_station ))
    # TO DO: display most commonly used end station
    popular_station_end = df['End Station'].mode()[0]
    print("The most commonly used end station is : {}".format(popular_station_end ))

    # TO DO: display most frequent combination of start station and end station trip
    popular_station_combined = df.groupby(['Start Station','End Station']).size().idxmax()
    print("The most commonly used start station and end station is : {}".format(popular_station_combined))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df.fillna(0)
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print("Total travel time is : {} seconds".format(total_travel_time))
    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("Mean of travel time is : {} seconds".format(mean_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    df.fillna(0)
    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print("Count of user types is : {}".format(count_user_types))
    # TO DO: Display counts of gender
    # since washington.csv file does not have gender and birth year, hence applying this filter
    if city.capitalize() != 'Washington':
        count_gender = df['Gender'].value_counts()
        print("Counts of gender is : {}".format(count_gender))    

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth_yr = df['Birth Year'].min()
        print("Earliest year birth is : {}".format(earliest_birth_yr))
        latest_birth_yr = df['Birth Year'].max()
        print("Most recent year birth is : {}".format(latest_birth_yr))
        common_birth_yr = df['Birth Year'].mode()[0]
        print("Most common year birth is : {}".format(common_birth_yr))
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
