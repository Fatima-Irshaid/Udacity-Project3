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
    
    city = input(" Select the city name (chicago, new york city, washington) : ").lower()
    while city not in CITY_DATA.keys():
        print('Invalid!, please re-enter a valid data!')
        city = input(" Select the city name (chicago, new york city, washington) : ")

        
    # TO DO: get user input for month (all, january, february, ... , june)
    
    months = ["all","january","february","march","april","may","june"]
    month = input (" Select month :(all,january, february, march, april,may, june) ").lower()
    while month not in months:
        print("Invalid!, please re-enter a valid data!")
        month = input (" Select month :(all,january, february, march, april,may, june) ").lower()
 

    # TO DO:  # get user input for day of week (all, monday, tuesday, ... sunday)
    
    week_days = ["sunday","monday","tuesday","wednesday","thursday","friday","all"]
    day = input("select a day!").lower()
    while day not in week_days:
        print("Invalid!, please re-enter a valid data!")
        day = input("select a day!").lower()

                
    


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

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # TO DO: display the most common month
   
    months = ["january", "february", "march", "april","may","june"]
    the_most_common_month = df["Start Time"].dt.month.mode()[0]
    month = [months[the_most_common_month-1]]
    print(f'\nThe most common month when travelling is {month}\n')


        # TO DO: display the most common day of week

    days = ["saturday","sunday","monday","tuesday","wednesday","thursday","friday"]
    the_most_common_day = df["Start Time"].dt.day.mode()[0]
   
    print(f'\nThe most common day when travelling is {the_most_common_day}\n')
    
    
    # TO DO: display the most common start hour

    the_most_common_hour = df["Start Time"].dt.hour.mode()[0]
    
    print('\nThe most common hour when travelling is: {}\n'.format(the_most_common_hour))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_used_start_station= df['Start Station'].mode()[0]
    print('\nThe most start_station which is commonly used : {}\n'.format(most_used_start_station))
    
    # TO DO: display most commonly used end station
    most_used_end_station=df['End Station'].mode()[0]
    print('\nThe most end station which is commonly used : {}\n'.format(most_used_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    df["most_combined_trip"]=df["End Station"]+" "+df["Start Station"]
    print('\nThe most common trip is :{}\n'.format(df["most_combined_trip"].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
  

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration=df["Trip Duration"].sum().round()
    print('\nThe total travel_time is: {}\n'.format(total_trip_duration))

    # TO DO: display mean travel time
    mean_trip_duration=df['Trip Duration'].mean().round()
    print('\nThe mean travel_time is: {}\n'.format(mean_trip_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count=df["User Type"].value_counts().to_frame()
    print('\nCount of User_Types is: {}\n'.format(user_types_count))

    # TO DO: Display counts of gender
    if "Gender" in df:
        count_of_gender=df["Gender"].value_counts().to_frame()
        print('\nThe count of Gender is: {}\n'.format(count_of_gender))
    else:
        print('\nError!! the sellected dataset has no gender information. Please choose another dataset\n')

        # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year=int(df['Birth Year'].min())
        print('\nThe earliest year of birth is: {}\n'.format(earliest_birth_year))
    else:
        print('\nError!! the sellected dataset has no year of birth information. Please choose another dataset\n')


    if 'Birth Year' in df:
        most_recent_birth_year=int(df['Birth Year'].max())
        print('\nThe most Recent Year of Birth is: {}\n'.format(most_recent_birth_year))
    else:
        print('\nError!! the sellected dataset has no year of birth information. Please choose another dataset\n')

    if 'Birth Year' in df:
        Most_common_birth_year=int(df['Birth Year'].mode()[0])
        print('\nThe most Common Year of birth is: {}\n'.format(Most_common_birth_year))
    else:
        print('\nError!! the sellected dataset has no year of birth information. Please choose another dataset\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def display_raw_data(df):
    print("\nTime for checking raw data\n")
    index = 0
    answer = input("Raw data is ready to check. Would you like to display 5 rows of them now? Please answer yes or no: ").lower()
    
    while answer != "yes" and answer != "no":
        print("Invalid answer! Please answer yes or no.")
        answer = input("Raw data is ready to check. Would you like to display 5 rows of them now? Please answer yes or no: ").lower()
    
    if answer == "no":
        print("Alright, thank you.")
    else:
        while index + 5 < df.shape[0]:
            print(df.iloc[index:index+5])
            index += 5
            answer = input("Would you like to display the next 5 rows of raw data? Please answer yes or no: ").lower()
            
            if answer == "no":
                print("Alright! Thank you.")
          
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()

