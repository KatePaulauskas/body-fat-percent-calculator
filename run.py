import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('body-fat-percent-calculator')

def get_todays_date():
    """
    Request the user to input the date, when measurements were taken
    """
    print("Welcome to Body Fat Percent Calculator")
    print("Enter the date measurements were taken in the following format DD/MM/YYYY")

    date_measurements_taken = input("Enter date here:\n")