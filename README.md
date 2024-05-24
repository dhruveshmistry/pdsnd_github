# Bike Share Data Analysis with Python
Project created: 24th of May 2024  
README created: 24th of May 2024

## Project Description
This is a database of bike share data for three U.S. cities: Chicago, Washington, and New York City. The coding prompts the user to select the city they want to look at, the month, and the day of the week and shows them that data.

## Installation Requirements
Python 3, NumPy, and pandas are required to run this program which can be downloaded from the web. A text editor such as Atom or Sublime can be helpful in visualising the code, but is not necessary.

## Usage Instructions
### The Datasets
There are three .csv files for each city discussed above in the database. Each includes the following data from the first six months of 2017:
1. Start Time (year-month-day, time)
2. End Time (year-month-day, time)
3. Trip Duration (in seconds)
4. Start Station
5. End Station
6. User Type (Subscriber or Customer)
The Chicago and New York City files also have a Gender column and a Birth Year column.

### Code Structure
The code is structured in the following order:
1. Libraries that help with data handling are imported (time, NumPy, and pandas)
   Note: the time library comes preinstalled with Python
2. The .csv files are loaded
3. The user is asked to type the city they want to look at, then the month, then the day of the week
4. The data is filtered depending on what the user inputs (first, city, then month, then day) and loaded
5. New columns are calculated and loaded (such as most frequent time of travel)
6. The code displays all the results for the user
7. The code asks the user if they would like to see raw data and responds accordingly
8. The user is given the option to restart once all input options have been exhausted

## Credits
The dataframe function is based on code found at: https://github.com/Moamen-Jamal/US-Bikeshare-Project/blob/5c4860b31f7153721b8d1e1c869bb6d731a6c062/bikeshare_2.py 
Used UdacityGPT to ask questions about the github project.
