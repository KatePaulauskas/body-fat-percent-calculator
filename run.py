import gspread
from google.oauth2.service_account import Credentials
import datetime
import re
from colorama import init, Fore, Back, Style

# Initialize Colorama
init()

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
    Runs a while loop to collect a valid date from the user via the terminal
    until the data is valid.
    """
    while True:
        date_measurements_taken = input(Style.BRIGHT +
            Fore.CYAN +
            "Enter the date measurements were taken in the following format: "
            "DD/MM/YYYY:\n"
        )

        if validate_date(date_measurements_taken):
            print(Fore.GREEN + "Date is valid!\n")
            break

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
        min_realistic_date = datetime.datetime.strptime(
            "01/01/1900", date_format)
        if entered_date > current_date:
            print(Fore.RED
                  + "The date cannot be in the future. "
                  "Please try again.\n")
            return False
        elif entered_date < min_realistic_date:
            print(Fore.RED
                  + "The date is unrealistically old. "
                  "Please enter a more recent date.\n")
            return False

        return True

    except ValueError:
        print(Fore.RED + "Incorrect date format. Try again.\n")
        return False


def get_user_name():
    """
    Request the user to input their name.
    Runs a while loop to collect a valid name from the user via the terminal
    until the name is valid.
    """
    while True:
        user_name = input(Fore.CYAN + "Enter your name here:\n")

        if validate_user_name(user_name):
            print(Fore.GREEN + "Name is valid!\n")
            break

    return user_name


def validate_user_name(name):
    """
    Validates user name entry contains only letters, hyphens, apostrophes,
    and spaces. Raises error message if the name was not entered in the
    required format.
    Sources:
    https://stackoverflow.com/questions/28495822/
    best-way-to-validate-a-name-in-python, 
    https://docs.python.org/3/howto/regex.html
    """
    pattern = r"^[a-zA-Z][a-zA-Z' -]+$"
    if re.match(pattern, name):
        return True
    else:
        print(Fore.RED + "Invalid name. Ensure it contains only letters, "
              "hyphens, apostrophes, and spaces and consists of at least "
              "2 characters.\n")
        return False


def get_user_gender():
    """
    Request the user to input their gender. Runs a while loop to collect
    a valid gender from the user via the terminal until the gender is valid.
    """
    while True:
        user_gender = input(
            Fore.CYAN
            + "Enter your gender in the following format: M or F:\n").upper()

        if user_gender == "M" or user_gender == "F":
            print(Fore.GREEN + "Gender is valid!\n")
            return user_gender
        else:
            print(Fore.RED + "Invalid input.\n")
            return get_user_gender()


def get_user_age():
    """
    Requests the user to input their age and validates it. Ensures that
    the input is a positive number. Runs a while loop to collect a valid
    age from the user via the terminal until the age is valid.
    """
    while True:
        user_age = input(Fore.CYAN
                         + "Enter your age in numerical "
                         "format (e.g. 30):\n")

        try:
            age = int(user_age)
            if 18 < age <= 130:
                print(Fore.GREEN + "Age is valid!\n")
                return age
            else:
                print(Fore.RED
                      + "Please enter a valid "
                      "age (between 18 and 130).\n")
        except ValueError:
            print(Fore.RED + "Invalid input.\n")


def get_user_weight():
    """
    Requests the user to input their weight and validates it. Ensures
    that the input is a positive number, which can be a float. Runs a
    while loop to collect a valid weight from the user via the terminal
    until the weight is valid.
    """
    while True:
        user_weight = input(Fore.CYAN
                            + "Enter your weight in "
                            "kgs (e.g. 80.5):\n")

        try:
            weight = float(user_weight)
            if weight > 10:
                print(Fore.GREEN + "Weight is valid!\n")
                return weight
            elif weight < 0:
                print(Fore.RED
                      + "Weight must be a positive number. "
                      "Please enter a valid weight.\n")    
            else:
                print(Fore.RED
                      + "Weight is unrealistically low. "
                      "Please enter a valid weight.\n")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a numeric value for "
                  "weight.\n")


def offer_procedure_instructions():
    """
    Offers instructions on how the measurements should be taken.
    """
    while True:
        print(Fore.YELLOW + "Would you like to view the information "
              "regarding the necessary equipment and procedures for "
              "conducting the measurements?\n")
        procedure_and_equipment = input(
            Fore.CYAN + "Enter your response here: Y or N.\n"
        ).upper()

        if procedure_and_equipment == "Y":
            print(Fore.MAGENTA + "Equipment: Skinfold caliper.\n"
                  "Procedure:\n")
            print("Measurements are taken on the right side of body. "
                  "Caliper needs to be perpendicular to the site "
                  "analysed. The participant must relax the muscle "
                  "group that is being assessed. When skin fold is "
                  "pinched, the practitioner should be taking reading "
                  "at the middle of the pinched skin, not apex or base. "
                  "Wait 1 to 2 seconds after releasing caliber, record "
                  "closest 0.5mm. Retake each site in order to obtain "
                  "accurate readings.\n")
            break
        elif procedure_and_equipment == "N":
            print(Fore.CYAN + "No problem, we will skip to the next part.\n")
            break
        else:
            print(Fore.RED + "Invalid input.\n")


def offer_measurements_instructions():
    """
    Offers instructions for taking the required skinfold measurements.
    """
    while True:
        print(Fore.YELLOW + "Would you like to review the instructions for "
              "taking the required skinfold measurements?\n")
        instructions = input(Fore.CYAN
            + "Enter your response here: Y or N.\n").upper()

        if instructions == "Y":
            print(Fore.MAGENTA + "Instructions:\n")
            print("Tricep: vertical fold at the midpoint of the posterior "
                  "side of tricep between shoulder and elbow with arm "
                  "relaxed at the side.\n"
                  "Chest: diagonal fold half the distance between anterior "
                  "axillary line and the nipple.\n"
                  "Subscapular: diagonal fold 2cm from inferior angle of "
                  "the scapula.\n"
                  "Midaxillary: at midaxillary line horizontal to xiphoid "
                  "process of the sternum.\n"
                  "Suprailiac: diagonal fold parallel and superior to the "
                  "iliac crest.\n"
                  "Abdominal: vertical fold 2cm to the right of the navel.\n"
                  "Thigh: midpoint of the anterior side of the upper leg "
                  "between the patella and top of thigh.\n")
            break
        elif instructions == "N":
            print(Fore.CYAN + "No problem, we will skip to the next part.\n")
            break
        else:
            print(Fore.RED + "Invalid input.\n")


def get_skinfold_measurements():
    """
    Requests the user to input the skinfold measurements in the form
    of a string of 7 numbers separated by commas.
    """
    while True:
        print(
            Fore.YELLOW +
            "Enter skinfold measurements in the following order: "
            "tricep, chest, subscapular, midaxillary, abdominal, "
            "suprailiac, thigh.\n"
            "Data should be 7 numbers, separated by spaces, "
            "numbers can have fractional parts. "
            "Example: 10.5 5 12 11.7 25 20 33\n"
        )

        measurements_str = input(Fore.CYAN
                                 + "Enter your skinfold measurements "
                                 "here in mm:\n")
        ##Replace comas with spaces, if entered by mistake and split the string                          
        skinfolds_measurements = measurements_str.replace(",", " ").split()

        if validate_skinfolds_measurements(skinfolds_measurements):
            print(Fore.GREEN + "Data is valid!\n")
            break
    return skinfolds_measurements


def validate_skinfolds_measurements(values):
    """
    Validates that there are exactly 7 numerical values and attempts to convert
    all string values into floats. It ensures each value is either an integer or a float.
    Checks for entries that are spaces and dots without numbers.
    """
    # Pattern to identify entries that are purely non-numeric (e.g., empty, just dots or commas)
    #Source: https://www.geeksforgeeks.org/write-regular-expressions/
    #https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Cheatsheet
    non_numeric_pattern = r"^\s*[\.,]*\s*$"

    # Ensure each entry is not just dots or empty spaces
    if any(re.match(non_numeric_pattern, value) for value in values):
        print(Fore.RED + "Invalid input. Each measurement must be a numerical value, "
        "entries containing only spaces or dots are not accepted.\n")
        return False

    # Filter out any entries that are just spaces or empty
    numeric_values = [value for value in values if value.strip()]

    # Attempt to convert each value to float and check for non-numeric values
    try:
        converted_skinfolds_measurements = [float(value) for value in numeric_values]
    except ValueError:
        print(
            Fore.RED +
            "Enter numeric value. Please ensure all entries are numbers.\n"
        )
        return False
    # Ensure none of the measurements exceeds 80 mm
    # Source: https://www.geeksforgeeks.org/python-any-function/
    if any(value > 80 for value in converted_skinfolds_measurements):
        print(
            Fore.RED +
            "Invalid data: one or more measurements exceed 80 mm. "
            "Please retake your measurements and enter correct values.\n"
        )
        return False
    #Prevent user from entering negative numbers
    if any(value < 0 for value in converted_skinfolds_measurements):
        print(
            Fore.RED +
            "Invalid data: measurements cannot be negative. "
            "Please enter positive values only.\n"
        )
        return False    

    # Check if we still have exactly 7 values
    if len(numeric_values) != 7:
        print(
            Fore.RED +
            "Exactly 7 values of skinfold measurements required, you provided "
            f"{len(numeric_values)}. Please try again.\n"
        )
        return False    

    return True

def store_data(date,
               user_name,
               user_gender,
               user_age,
               user_weight,
               skinfold_measurements):
    """
    Stores the validated data in the Google sheet 'measurements'.
    """
    print(Fore.YELLOW + "Updating measurements worksheet...\n")
    measurements_sheet = SHEET.worksheet("measurements")
    data_row = [
        date, user_name, user_gender, user_age, user_weight
    ] + skinfold_measurements
    measurements_sheet.append_row(data_row)
    print(Fore.GREEN
          + "Data in the measurements worksheet updated successfully.\n")


def calculate_body_fat_percent(user_age, user_gender, skinfold_measurements):
    """
    Calculates body fat percent using Jackson/Pollock 7-Site Caliper Method.
    Source: https://tskvspartacus.nl/tools/7-point-fat-percentage-calculator.php
    """
    print(Fore.CYAN + "Calculating your body fat percent...\n")
    skinfolds_sum = sum(
        [float(measurement) for measurement in skinfold_measurements])

    if user_gender == "M":
        body_fat_percent = 495 / (1.112 - (0.00043499 * skinfolds_sum) +
                                  (0.00000055 * skinfolds_sum ** 2) -
                                  (0.00028826 * user_age)) - 450
    else:
        body_fat_percent = 495 / (1.097 - (0.00046971 * skinfolds_sum) +
                                  (0.00000056 * skinfolds_sum ** 2) -
                                  (0.00012828 * user_age)) - 450

    return round(body_fat_percent, 2)


def calculate_body_fat_weight(user_weight, user_body_fat_percent):
    """
    Calculates the body fat weight based on the provided weight and
    calculated body fat percent.
    """
    print(Fore.CYAN + "Calculating your body fat weight...\n")
    body_fat_weight = (user_weight * user_body_fat_percent) / 100
    return round(body_fat_weight, 2)


def calculate_lean_body_weight(user_weight, user_body_fat_weight):
    """
    Calculates the user's lean body mass based on their weight
    and body fat weight.
    """
    print(Fore.CYAN + "Calculating your lean body mass...\n")
    lean_body_weight = user_weight - user_body_fat_weight
    return round(lean_body_weight, 2)


def store_results(user_body_fat_percent,
                  user_body_fat_weight,
                  user_lean_body_weight):
    """
    Stores calculated results for the user's body fat percent, body fat weight,
    and lean body mass in the Google sheet 'results'.
    """
    print(Fore.YELLOW + "Updating results worksheet...\n")
    results_sheet = SHEET.worksheet("results")
    data_row = [user_body_fat_percent,
                user_body_fat_weight,
                user_lean_body_weight]
    results_sheet.append_row(data_row)
    print(Fore.GREEN + "Data in the results worksheet updated successfully.\n")


def display_recommendations(user_gender, user_body_fat_percent):
    """
    Checks user gender and the body fat percent calculated
    Provides explanation of the result and further recommendations based on the
    user's fitness levels of the body
    """
    print(Fore.YELLOW + "Summary and Recommendations:\n")

    if (user_gender == "M" and 2 <= user_body_fat_percent <= 5) or (
         user_gender == "F" and 10 <= user_body_fat_percent <= 13):
        print(Fore.CYAN
              + f"Your body fat percentage of {user_body_fat_percent}% "
              "indicates that you are in the Essential Fat category. "
              "Maintain your current level of physical activity and healthy "
              "eating habits. Consult with a healthcare provider if you're "
              "significantly below this range, as too little body fat "
              "can affect your health.\n")

    elif (user_gender == "M" and 5 < user_body_fat_percent <= 13) or (
          user_gender == "F" and 13 < user_body_fat_percent <= 20):
        print(Fore.CYAN
              + f"Your body fat percentage of {user_body_fat_percent}% "
              "indicates that you are in the Athletic Build category, with "
              "a lean body composition and a higher proportion of muscle "
              "mass. Continue your balanced diet and regular exercise "
              "regimen to maintain your athletic build, focusing on "
              "strength, flexibility, and endurance training for "
              "optimal performance.\n")

    elif (user_gender == "M" and 13 < user_body_fat_percent <= 17) or (
          user_gender == "F" and 20 < user_body_fat_percent <= 24):
        print(Fore.CYAN
              + f"Your body fat percentage of {user_body_fat_percent}% "
              "indicates that you are in the Fitness category. "
              "You're within a healthy and fit body fat percentage range, "
              "common for people who lead an active lifestyle. Keep up the "
              "good work with regular physical activity and a balanced diet, "
              "focusing on specific fitness goals based on "
              "personal preferences.\n")

    elif (user_gender == "M" and 17 < user_body_fat_percent <= 25) or (
          user_gender == "F" and 24 < user_body_fat_percent <= 31):
        print(Fore.CYAN
              + f"Your body fat percentage of {user_body_fat_percent}% "
              "indicates that you are in the Above but Acceptable "
              "category. Your body fat percentage is above the optimal "
              "range for fitness but still within an acceptable level. "
              "Consider increasing your physical activity level and "
              "monitoring your diet to improve your body composition, "
              "aiming for a mix of cardio, strength training, and "
              "flexibility exercises.\n")

    elif (user_gender == "M" and user_body_fat_percent > 25) or (
          user_gender == "F" and user_body_fat_percent > 31):
        print(Fore.CYAN
              + f"Your body fat percentage of {user_body_fat_percent}% "
              "indicates that you are in the Obese category. This means "
              "your body fat percentage falls within the obese range, "
              "which may increase your risk for health issues. "
              "It's advisable to seek guidance from a healthcare "
              "professional to develop a personalized plan for reducing "
              "body fat, including nutritional counseling, a structured "
              "exercise program, and lifestyle adjustments.\n")

    elif (user_gender == "M" and user_body_fat_percent < 2) or (
          user_gender == "F" and user_body_fat_percent < 10):
        print(Fore.RED
              + f"Your body fat percentage of {user_body_fat_percent}% "
              "is below the essential fat levels. This can pose serious "
              "health risks. Please consult with a healthcare provider.\n")


def run_again():
    """
    Asks the user if they want to run the program again or end it.
    """
    while True:
        run_again_input = input(
            Fore.CYAN
            + "Would you like to run the program again? "
            "Enter Y or N:\n").upper()

        if run_again_input == "Y":
            return True

        elif run_again_input == "N":
            return False

        else:
            print(Fore.RED + "Invalid input. Please enter Y or N.\n")


def main():
    """
    Run all program functions
    """
    while True:

        print(Style.BRIGHT +
              Fore.YELLOW + "Welcome to Body Fat Percent Calculator\n")
        print("In order to use the Calculator, please use "
              "a skinfold caliper\n")

        date = get_measurements_date()
        user_name = get_user_name()
        user_gender = get_user_gender()
        user_age = get_user_age()
        user_weight = get_user_weight()
        procedure_instructions = offer_procedure_instructions()
        measurements_instructions = offer_measurements_instructions()
        skinfold_measurements = get_skinfold_measurements()
        user_inputs = store_data(
            date,
            user_name,
            user_gender,
            user_age,
            user_weight,
            skinfold_measurements)
        user_body_fat_percent = calculate_body_fat_percent(
            user_age, user_gender, skinfold_measurements)
        print(Fore.MAGENTA
              + f"Your body fat percent is {user_body_fat_percent} %\n")
        user_body_fat_weight = calculate_body_fat_weight(
            user_weight, user_body_fat_percent)
        print(Fore.MAGENTA
              + f"Your body fat weight is {user_body_fat_weight} kg\n")
        user_lean_body_weight = calculate_lean_body_weight(
            user_weight, user_body_fat_weight)
        print(Fore.MAGENTA
              + f"Your lean body mass is {user_lean_body_weight} kg\n")
        user_results = store_results(
            user_body_fat_percent, user_body_fat_weight, user_lean_body_weight)
        recommendations = display_recommendations(
            user_gender, user_body_fat_percent)
        run_program_again = run_again()

        """
        'if cond == False' replaced with 'if not cond'
        Source:
        https://stackoverflow.com/questions/54474042/
        how-to-fix-the-flake-8-error-e712-comparison-
        to-false-should-be-if-cond-is-fal
        """
        if not run_program_again:
            break
    print(Fore.YELLOW
        + "The program has ended. Thank you for using the Body Fat Percent "
        "Calculator.")


main()
