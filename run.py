import gspread
from google.oauth2.service_account import Credentials
import datetime
import re

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("body-fat-percent-calculator")


def get_measurements_date():
    """
    Requests the user to input the date, when measurements were taken.
    Runs a while loop to collect a valid date from the user via the terminal until the data is valid
    """

    while True:
        print(
            "Enter the date measurements were taken in the following format: DD/MM/YYYY.\n"
        )

        date_measurements_taken = input("Enter date here:\n")

        if validate_date(date_measurements_taken):
            print("Date is valid!\n")
            # Exit the loop after validating the date
            break

    # Return the validated date
    return date_measurements_taken


def validate_date(value):
    """
    Validates the date is entered in the correct format.
    Raises ValueError if date is not entered in the correct format.
    Source: https://www.tutorialspoint.com/How-to-do-date-validation-in-Python
    """

    date_format = "%d/%m/%Y"

    try:
        entered_date = datetime.datetime.strptime(value, date_format)
        current_date = datetime.datetime.now()
        min_realistic_date = datetime.datetime.strptime("01/01/1900", date_format)
        if entered_date > current_date:
            print("The date cannot be in the future. Please try again.\n")
            return False
        elif entered_date < min_realistic_date:
            print("The date is unrealistically old. Please enter a more recent date.\n")
            return False

        return True

    except ValueError:
        print("Incorrect date format. Try again\n")
        return False


def get_user_name():
    """
    Request the user to input their name.
    Runs a while loop to collect a valid name from the user via the terminal until the name is valid.
    """

    while True:
        print(
            "Enter your name. You can use letters, hyphens, apostrophes, and spaces (where appropriate)\n"
        )

        user_name = input("Enter your name here:\n")

        if validate_user_name(user_name):
            print("Name is valid!\n")
            # Exit the loop after validatign the name
            break

    return user_name


def validate_user_name(name):
    """
    Validates user name entry contains only letters, hyphens, apostrophes, and spaces
    Raises error message if the name was not entered in the required format
    Sources: https://stackoverflow.com/questions/28495822/best-way-to-validate-a-name-in-python, https://docs.python.org/3/howto/regex.html
    """
    pattern = r"^[a-zA-Z][a-zA-Z' -]+$"
    if re.match(pattern, name):
        return True
    else:
        print(
            "Invalid name. Please ensure it contains only letters, hyphens, apostrophes, and spaces (where appropriate).\n"
        )
        return False


def get_user_gender():
    """
    Request the user to input their gender.
    Runs a while loop to collect a valid gender from the user via the terminal until the gender is valid.
    """

    print("Enter your gender in the followign format: M or F.\n")

    user_gender = input("Enter your gender:\n")

    if user_gender == "M" or user_gender == "F":
        print("Gender is valid!\n")
        return user_gender
    else:
        print("Invalid input. Please enter M or F.\n")
        return get_user_gender()


def get_user_age():
    """
    Requests the user to input their age and validates it.
    Ensures that the input is a positive number.
    Runs a while loop to collect a valid age from the user via the terminal until the age is valid.
    """
    while True:
        print("Enter your age in numerical format.\n")
        user_age = input("Enter your age here:\n")

        try:
            age = int(user_age)
            if age > 0:
                print("Age is valid!\n")
                return age
            else:
                print("Age must be a positive number. Please enter a valid age.\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value for age.\n")


def get_user_weight():
    """
    Requests the user to input their weight and validates it.
    Ensures that the input is a positive number, which can be a float.
    Runs a while loop to collect a valid weight from the user via the terminal until the weight is valid.
    """
    while True:
        print("Enter your weight in kilograms in the followign format: 80.5.\n")
        user_weight = input("Enter your weight here:\n")

        try:
            weight = float(user_weight)
            if weight > 0:
                print("Weight is valid!\n")
                return weight
            else:
                print(
                    "Weight must be a positive number. Please enter a valid weight.\n"
                )
        except ValueError:
            print("Invalid input. Please enter a numeric value for weight.\n")


def get_skinfold_measurements():
    """
    Provides instructions on how the measurements should be taken.
    Requests the user to input the skinfold measurements in the form
    of a string of 7 numbers separated by commas.
    Runs a while loop to collect a valid string of data from the user
    via the terminal until the data is valid.
    """

    print ("Would you like to view the information regarding the necessary equipment and procedures for conducting the measurements?")
    procedure_and_equiprment = input ("Enter your responce here: Y or N.\n")

    if procedure_and_equiprment == "Y":
        print("Equipment: Skinfold caliper.\n")
        print("Procedure:\n")
        print(
            "Measurements are taken on the right side of body. Caliber needs to be perpendicular to the site analyzed."
        )
        print("The participant must relax the muscle group that is being assessed.")
        print(
            "When skin fold is pinched, the practitioner should be taking reading at the middle of the pinched skin, not apex or base."
        )
        print(
            "Wait 1 to 2 seconds after releasing caliber, record closest 0.5mm. Retake each site in order to obtain accurate readings.\n"
        )

    elif procedure_and_equiprment == "N":
        print("No problem, we will skip to the next part.\n") 

    else:
        print("Invalid input. Please enter Y or N.\n")
        return procedure_and_equiprment

    print ("Would you like to review the instructions for taking the required skinfold measurements?")
    instructions = input ("Enter your responce here: Y or N.\n")

    if instructions == "Y":
        print("Insturctions:\n")
        print(
            "Tricep: vertical fold at the midpoint of the posterior side of tricep between shoulder and elbow with arm relaxed at the side.\n"
        )
        print(
            "Chest: diagonal fold half the distance between anterior axillary line and the nipple.\n"
        )
        print("Subscapular: diagonal fold 2cm from inferior angle of the scapula.\n")
        print(
            "Midaxillary: at midaxillary line horizontal to xiphoid process of the sternum.\n"
        )
        print("Suprailiac: diagonal fold parallel and superior to the iliac crest.\n")
        print("Abdominal: vertical fold 2cm to the right of the navel.\n")
        print(
            "Thigh: midpoint of the anterior side of the upper leg between the patella and top of thigh.\n"
        )

    elif instructions == "N":
        print("No problem, we will skip to the next part.\n") 

    else:
        print("Invalid input. Please enter Y or N.\n")
        return instructions   

    while True:
        print(
            "Enter skinfold measurements in mm in the following order: tricep, chest, subscapular, midaxillary, abdominal, suprailiac, thigh."
        )
        print(
            "Data should be 7 numbers, separated by commas, numbers can have fractional parts. Example: 10.5,5,12,11.7,25,20,33\n"
        )

        measurements_str = input("Enter your skinfold measurements here in mm:\n")

        skinfolds_measurements = measurements_str.split(",")

        if validate_skinfolds_measurements(skinfolds_measurements):
            print("Data is valid!")
            break
    return skinfolds_measurements


def validate_skinfolds_measurements(values):
    """
    Validates that there are exactly 7 numerical values and attempts to convert
    all string values into floats. Raises ValueError if strings cannot
    be converted into floats, or if there aren't exactly 7 values.
    """
    if len(values) != 7:
        print(
            f"Exactly 7 values of skinfold measurements required, you provided {len(values)}. Please try again.\n"
        )
        return False
    try:
        converted_skinfolds_measurements = [float(value) for value in values]
    except ValueError:
        print(
            "Invalid data: one or more skinfold measurements entered values are not a number. Please try again.\n"
        )
        return False

    # Check if any measurement value exceeds maximum possible skinfold size of 80 mm. Source: https://stackoverflow.com/questions/20211339/using-python-function-any-on-a-list-of-floats
    if any(value > 80 for value in converted_skinfolds_measurements):
        print("Invalid data: one or more skinfold measurements entered values exceeds 80 mm. Skinfold measurement cannot exceed 80 mm. Please retake your measurements and enter correct values.\n")
        return False

    return True


def store_data(
    date, user_name, user_gender, user_age, user_weight, skinfold_measurements
):
    """
    Store the validated data in the Google sheet.
    """
    print("Updating measurements worksheet...\n")
    measurements_sheet = SHEET.worksheet("measurements")
    data_row = [
        date,
        user_name,
        user_gender,
        user_age,
        user_weight,
    ] + skinfold_measurements
    measurements_sheet.append_row(data_row)
    print("The date in the measurements worksheet updated successfully\n")


def calculate_body_fat_percent(user_age, user_gender, skinfold_measurements):
    """
    Performs body fat percent calculations based on the user's gender, age, and sum of skinfold measurements
    Usuing Jackson/Pollock 7-Site Caliper Method formula.
    Source: https://tskvspartacus.nl/tools/7-point-fat-percentage-calculator.php#footnote-1
    """
    print("Calculating your body fat percent...\n")
    skinfolds_sum = sum([float(measurement) for measurement in skinfold_measurements])

    if user_gender == "M":
        body_fat_percent = (
            495
            / (
                1.112
                - (0.00043499 * skinfolds_sum)
                + (0.00000055 * skinfolds_sum**2)
                - (0.00028826 * user_age)
            )
            - 450
        )

    else:
        body_fat_percent = (
            495
            / (
                1.097
                - (0.00046971 * skinfolds_sum)
                + (0.00000056 * skinfolds_sum**2)
                - (0.00012828 * user_age)
            )
            - 450
        )

    return round(body_fat_percent, 2)


def calculate_body_fat_weight(user_weight, user_body_fat_percent):
    """
    Calculates the body fat weight based on the weight user ptovided and the calculated  body fat percent
    """
    print("Calculating your body fat weight...\n")
    body_fat_weight = (user_weight * user_body_fat_percent) / 100

    return round(body_fat_weight, 2)


def calculate_lean_body_weight(user_weight, user_body_fat_weight):
    """
    Calculates user's body lean mass based on the user's weight and body fat weight
    """
    print("Calculating your body lean mass...\n")
    lean_body_weight = user_weight - user_body_fat_weight

    return round(lean_body_weight, 2)


def display_recommendations(user_gender, user_body_fat_percent):
    """
    Checks user gender and the body fat percent calculated
    Provides explanation of the result and further recommendations based on the user's fitness levels of the body
    """

    if (user_gender == "M" and 2 <= user_body_fat_percent <= 5) or (
        user_gender == "F" and 10 <= user_body_fat_percent <= 13
    ):
        print(
            f"Your body fat percentage of {user_body_fat_percent}% indicates that you are in the Essential Fat category. Maintain your current level of physical activity and healthy eating habits. Consult with a healthcare provider if you're significantly below this range, as too little body fat can affect your health."
        )

    elif (user_gender == "M" and 5 < user_body_fat_percent <= 13) or (
        user_gender == "F" and 13 < user_body_fat_percent <= 20
    ):
        print(
            f"Your body fat percentage of {user_body_fat_percent}% indicates that you are in the Athletic Build category, with a lean body composition and a higher proportion of muscle mass. Continue your balanced diet and regular exercise regimen to maintain your athletic build, focusing on strength, flexibility, and endurance training for optimal performance."
        )

    elif (user_gender == "M" and 13 < user_body_fat_percent <= 17) or (
        user_gender == "F" and 20 < user_body_fat_percent <= 24
    ):
        print(
            f"Your body fat percentage of {user_body_fat_percent}% indicates that you are in the Fitness category. You're within a healthy and fit body fat percentage range, common for people who lead an active lifestyle. Keep up the good work with regular physical activity and a balanced diet, focusing on specific fitness goals based on personal preferences."
        )

    elif (user_gender == "M" and 17 < user_body_fat_percent <= 25) or (
        user_gender == "F" and 24 < user_body_fat_percent <= 31
    ):
        print(
            f"Your body fat percentage of {user_body_fat_percent}% indicates that you are in the Above but Acceptable category. Your body fat percentage is above the optimal range for fitness but still within an acceptable level. Consider increasing your physical activity level and monitoring your diet to improve your body composition, aiming for a mix of cardio, strength training, and flexibility exercises."
        )

    elif (user_gender == "M" and user_body_fat_percent > 25) or (
        user_gender == "F" and user_body_fat_percent > 31
    ):
        print(
            f"Your body fat percentage of {user_body_fat_percent}% indicates that you are in the Obese category. This means your body fat percentage falls within the obese range, which may increase your risk for health issues. It's advisable to seek guidance from a healthcare professional to develop a personalized plan for reducing body fat, including nutritional counseling, a structured exercise program, and lifestyle adjustments."
        )

    elif (user_gender == "M" and user_body_fat_percent < 2) or (
        user_gender == "F" and user_body_fat_percent < 10
    ):
        print(
            f"Your body fat percentage of {user_body_fat_percent}% is below the essential fat levels. This can pose serious health risks. Please consult with a healthcare provider."
        )


def main():
    """
    Run all program functions
    """

    date = get_measurements_date()
    user_name = get_user_name()
    user_gender = get_user_gender()
    user_age = get_user_age()
    user_weight = get_user_weight()
    skinfold_measurements = get_skinfold_measurements()
    user_inputs = store_data(
        date, user_name, user_gender, user_age, user_weight, skinfold_measurements
    )
    user_body_fat_percent = calculate_body_fat_percent(
        user_age, user_gender, skinfold_measurements
    )
    print(f"Your body fat percent is {user_body_fat_percent} %\n")
    user_body_fat_weight = calculate_body_fat_weight(user_weight, user_body_fat_percent)
    print(f"Your body fat weight is {user_body_fat_weight} kg\n")
    user_lean_body_weight = calculate_lean_body_weight(
        user_weight, user_body_fat_weight
    )
    print(f"Your lean body mass is {user_lean_body_weight} kg\n")
    recommendations = display_recommendations(user_gender, user_body_fat_percent)


print("Welcome to Body Fat Percent Calculator\n")
print("In order to use the Calculator, please use a skinfold caliper\n")
main()
