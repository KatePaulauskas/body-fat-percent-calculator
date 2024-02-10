import gspread
from google.oauth2.service_account import Credentials
import datetime
import re

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('body-fat-percent-calculator')

def get_measurements_date():
    """
    Request the user to input the date, when measurements were taken
    """

    print('Welcome to Body Fat Percent Calculator\n')
    print('In order to use the Calculator, please use a skinfold caliper\n')
    while True:
        print('Enter the date measurements were taken in the following format: DD/MM/YYYY.\n')

        date_measurements_taken = input('Enter date here:\n')

        if validate_date(date_measurements_taken):
            print('Date is valid!\n')
            # Exit the loop after validating the date
            break

    # Return the validated date       
    return date_measurements_taken

def validate_date(value):
    """
    Validate the date is entered in the correct format.
    Raise ValueError if date is not entered in the correct format
    Source: https://www.tutorialspoint.com/How-to-do-date-validation-in-Python
    """

    date_format = '%d/%m/%Y'

    try:
        datetime.datetime.strptime(value, date_format)
        return True

    except ValueError:
        print("Incorrect date format. Try again\n")
        return False


date = get_measurements_date()

def get_user_name():
    """
    Request the user to input their name
    """

    while True:
        print('Enter your name. You can use letters, hyphens, apostrophes, and spaces (where appropriate)\n')

        user_name = input('Enter your name here:\n')

        if validate_user_name(user_name):
            print('Name is valid!\n')
            # Exit the loop after validatign the name
            break

    return user_name


def validate_user_name(name):
    """
    Validate user name entry contains only letters, hyphens, apostrophes, and spaces
    Raise error message if the name was not entered in the required format
    Sources: https://stackoverflow.com/questions/28495822/best-way-to-validate-a-name-in-python, https://docs.python.org/3/howto/regex.html
    """
    pattern = r"^[a-zA-Z][a-zA-Z' -]+$"
    if re.match(pattern, name):
        return True
    else:
        print("Invalid name. Please ensure it contains only letters, hyphens, apostrophes, and spaces (where appropriate).\n")
        return False

user_name = get_user_name()

def get_user_gender():
    """
    Request the user to input their gender
    """

    print('Enter your gender in the followign format: M or F.\n')

    user_gender = input('Enter your gender:\n')

    if user_gender == 'M' or user_gender == 'F':
        print('Gender is valid!\n')
        return user_gender
    else:
        print('Invalid input. Please enter M or F.\n')
        return get_user_gender()

user_gender = get_user_gender()

def get_user_weight():
    """
    Request the user to input their weight and validate it.
    Ensures that the input is a positive number, which can be a float.
    """
    while True:
        print('Enter your weight in kilograms in the followign format: 80.5.\n')
        user_weight = input("Enter your weight here:\n")

        try:
            weight = float(user_weight)
            if weight > 0:
                print("Weight is valid!\n")
                return weight
            else:
                print("Weight must be a positive number. Please enter a valid weight.\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value for weight.\n")

user_weight = get_user_weight()

def get_skinfold_measurements():
    """
    Provides instructions on how the measurements should be taken
    Requests the user to input the skinfold measurements.
    Runs a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 7 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    print('Equipment: Skinfold caliper.\n')
    print('Procedure:\n')
    print('Measurements are taken on the right side of body. Caliber needs to be perpendicular to the site analyzed.')
    print('The participant must relax the muscle group that is being assessed.')
    print('When skin fold is pinched, the practitioner should be taking reading at the middle of the pinched skin, not apex or base.')
    print('Wait 1 to 2 seconds after releasing caliber, record closest 0.5mm. Retake each site in order to obtain accurate readings.\n')
    print('Insturctions:\n')
    print('Tricep: vertical fold at the midpoint of the posterior side of tricep between shoulder and elbow with arm relaxed at the side.\n')
    print('Chest: diagonal fold half the distance between anterior axillary line and the nipple.\n')
    print ('Subscapular: diagonal fold 2cm from inferior angle of the scapula.\n')
    print('Midaxillary: at midaxillary line horizontal to xiphoid process of the sternum.\n')
    print('Suprailiac: diagonal fold parallel and superior to the iliac crest.\n')
    print('Abdominal: vertical fold 2cm to the right of the navel.\n')
    print ('Thigh: midpoint of the anterior side of the upper leg between the patella and top of thigh.\n')
    
    while True:
        print('Enter skinfold measurements in mm in the following order: tricep, chest, subscapular, midaxillary, abdominal, suprailiac, thigh.')
        print('Data should be 7 numbers, separated by commas, numbers can have fractional parts. Example: 10.5,5,12,11.7,25,20,33\n')

        measurements_str = input("Enter your measurements here:\n")

        skinfolds_measurements = measurements_str.split(",")

        if validate_skinfolds_measurements(skinfolds_measurements):
            print("Data is valid!")
            break
    return skinfolds_measurements


def validate_skinfolds_measurements(values):
    """
    Validates that there are exactly 7 values and attempts to convert
    all string values into integers. Raises ValueError if strings cannot
    be converted into int, or if there aren't exactly 7 values.
    """
    if len(values) != 7:
        print(f"Exactly 7 values required, you provided {len(values)}. Please try again.\n")
        return False
    try:
        converted_skinfolds_measurements = [float(value) for value in values]
    except ValueError:
        print("Invalid data: one or more entered values are not a number. Please try again.\n")
        return False

    return True


get_skinfold_measurements()