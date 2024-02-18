# Body Fat Percent Calculator

## Goal, target audience

### Project Links

Live Site

Repository

## How to use / User Experience
User Stories
First Time User / Returning User / Interested parties

## Structure 
Program Flowchart / Logic

## Data Storage / Model
User data and calculated results are stored in a Google Sheets. The document comprised of two separate worksheets: 'measurements' and 'results'. The data does not contain any sensitive information.

## Features
Colours
Colorama Python package that allows  to produce colored terminal text was used to add color to the text of the app and improve user experience. 

### Existing Features

### Future Features

## Data Model

## Python Packages Used

## Testing

### Testing behaviour
Action/Feature          | Expected behavior       | Status         |
|-------------------|-------------------------|----------------|
|Enter URL: <https://body-fat-percent-calculator-5ad0ac04aebf.herokuapp.com/> | Page loads with the terminal displaying the following message: 'Running startup command: python3 run.py. Welcome to Body Fat Percent Calculator. In order to use the Calculator, please use a skinfold caliper. Enter the date measurements were taken in the following format: DD/MM/YYYY:' | Pass |
|Testing date input field |
|Enter an invalid date format (e.g., “15-03-2024” or “03/15/2024”) | The program displays an error message: 'Incorrect date format. Try again.' The user is offered again to enter the date measurements were taken in the following format: DD/MM/YYYY.| Pass |
|Enter a date that is in the future (e.g., “20/05/2025”) | The program displays an error message: 'The date cannot be in the future. Please try again.' The user is offered again to enter the date measurements were taken in the following format: DD/MM/YYYY. | Pass |
|Enter a date that is in the distant past (e.g., “01/01/1800”) | The program displays an error message: 'The date is unrealistically old. Please enter a more recent date.' The user is offered again to enter the date measurements were taken in the following format: DD/MM/YYYY. | Pass |
|Enter text into the input field for the date | Error message is displayed: ‘Incorrect date format. Try again.’ The user is offered again to enter the date measurements were taken in the following format: DD/MM/YYYY. | Pass |
|Enter a space into the input field for the date | Error message is displayed: ‘Incorrect date format. Try again.’ The user is offered again to enter the date measurements were taken in the following format: DD/MM/YYYY. | Pass |
|Enter a date in a non-leap year (e.g., “29/02/2023”) | The program displays an error message: “Incorrect date format. Try again.” The user is offered again to enter the date measurements were taken in the following format: DD/MM/YYYY. | Pass |
|Enter a valid date in the format 'DD/MM/YYYY' | The date is accepted, the program displays a message 'Date is valid!' and proceeds. | Pass |
Enter a date in a leap year (e.g., “29/02/2020”) | The date is accepted, the program displays a message 'Date is valid!' and proceeds. | Pass |
|Testing name input field |
|Enter a name that contains no letters (e.g., digits or special characters only). | The program displays an error message: 'Invalid name. Ensure it contains only letters, hyphens, apostrophes, and spaces and consists of at least 2 characters'. The user if offered to enter name again. | Pass |
|Enter a name with fewer than 2 characters (e.g. 'A'). | The program displays the same error message “Invalid name. Ensure it contains only letters, hyphens, apostrophes, and spaces and consists of at least 2 characters”.  The user if offered to enter name again. | Pass |
|Enter a name containing unsupported characters, such as special symbols other than hyphens and apostrophes (e.g. 'Tom@Smith') | The program displays the same error message “Invalid name. Ensure it contains only letters, hyphens, apostrophes, and spaces and consists of at least 2 characters”.  The user if offered to enter name again. | Pass |
|Enter a name with a leading space (e.g. ' Jane') |  The program displays the same error message “Invalid name. Ensure it contains only letters, hyphens, apostrophes, and spaces and consists of at least 2 characters”.  The user if offered to enter name again. | Pass |
|Enter a space in the name input field |  The program displays the same error message “Invalid name. Ensure it contains only letters, hyphens, apostrophes, and spaces and consists of at least 2 characters”.  The user if offered to enter name again. | Pass |
|Enter a valid name containing only letters, hyphens, apostrophes, and spaces. | The name is accepted, the program displays a message 'Name is valid!' and proceeds. | Pass |
|Testing gender input field |
|Enter any input other than 'M' or 'F' (e.g., number, text, lower case 'm' or 'f') | The program displays an error message: “Invalid input.” The user is offered to enter their gender in the following format: M or F. | Pass |
|Enter space in the gender input field | The program displays an error message: “Invalid input.” The user is offered to enter their gender in the following format: M or F. | Pass |
|Enter 'M' | The gender is accepted, the program displays a message 'Gender is valid!' and proceeds. | Pass |
|Enter 'F' | The gender is accepted, the program displays a message 'Gender is valid!' and proceeds. | Pass |
|Testing age input field |
|Enter a negative age (e.g., '-10') | The program displays an error message: 'Please enter a valid age (between 18 and 130)'. The user is offered to enter age in numerical format (e.g. 30) | Pass |
|Enter zero as the age | The program displays an error message: 'Please enter a valid age (between 18 and 130)'. The user is offered to enter age in numerical format (e.g. 30) | Pass |
|Enter age below 18 (e.g. '15') | The program displays an error message: 'Please enter a valid age (between 18 and 130)'. The user is offered to enter age in numerical format (e.g. 30) | Pass |
|Enter age above 130 (e.g. 150) | The program displays an error message: 'Please enter a valid age (between 18 and 130)'. The user is offered to enter age in numerical format (e.g. 30) | Pass |
|Enter a non-numeric input (e.g., 'twenty') | The program displays an error message: 'Invalid input.' The user is offered to enter age in numerical format (e.g. 30) |
|Enter space to the age input field | The program displays an error message: 'Invalid input.' The user is offered to enter age in numerical format (e.g. 30) |
|Enter a valid age between 18 and 130 (e.g., '30'). | The age is accepted, the program displays a message 'Age is valid!' and proceeds. | Pass |
|Testing weight input field |
|Enter a negative weight (e.g., '-5') | The program displays an error message: 'Weight must be a positive number. Please enter a valid weight'. The user is offered to enter weight in kgs (e.g. 80.5). | Pass |
|Enter a non-numeric input (e.g., 'fifty') | The program displays an error message: 'Invalid input. Please enter a numeric value for weight.' The user is offered to enter weight in kgs (e.g. 80.5). | Pass |
|Enter a space into the weight input field | The program displays an error message: 'Invalid input. Please enter a numeric value for weight.' The user is offered to enter weight in kgs (e.g. 80.5). | Pass |
|Enter a valid weight greater than 10 (e.g., '80.5') | The weight is accepted, the program displays a message 'Weight is valid!'and proceeds | Pass |
|Testing procedure instructuins display |
|Enter any input other than 'Y' or 'N' (e.g., number, text, lower case 'y' or 'n') | The program displays an error message: 'Invalid input'. The user is asked if they would you like to view the information regarding the necessary equipment and procedures for conducting the measurements and offered to provide responcxe in the following format Y or N. | Pass |
|Enter 'Y' to view the instructions | The program displays the equipment and procedure instructions. | Pass |
|Enter 'N' to skip viewing the instructions | The program acknowledges the choice with the following message: 'No problem, we will skip to the next part' and proceeds. | Pass |
|Testing skinfold measurements instructuins display |
|Enter any input other than 'Y' or 'N' (e.g., number, text, lower case 'y' or 'n') | The program displays an error message: 'Invalid input'. The user is asked if they would you like to vreview the instructions for taking the required skinfold measurements and offered to provide responcxe in the following format Y or N. | Pass |
|Enter 'Y' to view the instructions | The program displays the equipment and procedure instructions. | Pass |
|Enter 'N' to skip viewing the instructions | The program acknowledges the choice with the following message: 'No problem, we will skip to the next part' and proceeds. | Pass |
|Testing skinfold measurements input field |
|Enter fewer or more than 7 values into the measurements input field(e.g., '10,15,12' or '11,20,12,10.7,9.5,20,18,35,45.5') | The program displays an error message: 'Exactly 7 values of skinfold measurements required, you provided X. Please try again.' The user is offered to attempt enterign skinfolds again. | Pass |
|Enter non-numeric values (e.g., 'hello,5,12,11.7,25,20,33') | The program displays an error message: 'Invalid data: one or more skinfold measurements entered are not numbers. Please try again'. | Pass |
|Enter measurements exceeding 80 mm (e.g., '90,70,85,95,100,80,75') | The program displays an error message: 'Invalid data: one or more measurements exceed 80 mm. Please retake your measurements and enter correct values'. | Pass |
|Enter valid skinfold measurements in the correct format (e.g., “10.5,5,12,11.7,25,20,33”) | The measurements are accepted, the program displays a message 'Data is valid!'and proceeds | Pass |


### Validator Testing
To align with web standards and ensure accessability compliance Python code was tested through [PEP8 Python Validator](https://pep8ci.herokuapp.com). Five errors were identified, as described below.

**1. E501: Line Too Long (93 > 79 characters)**
- Description: This error occurs when a line exceeds the recommended maximum length of 79 characters.
- Resolution: Lines with such error were broken into multiple lines using parentheses as per instructions from [ Stack Overflow](https://stackoverflow.com/questions/53158284/python-giving-a-e501-line-too-long-error?noredirect=1).

**2. E128: Continuation Line Under-Indented for Visual Indent**
- Description: This error occurs when a continuation line (following an opening parenthesis) is not indented correctly.
- Resolution: It was ensured that continuation lines with such error are indented to the same level as the opening parenthesis as per instructions from [Stack Overflow](https://stackoverflow.com/questions/15435811/what-is-pep8s-e128-continuation-line-under-indented-for-visual-indent).

**3. W291: Trailing Whitespace**
- Description: This warning indicates that there are extra spaces or tabs at the end of a line.
- Resolution: All the trailing whitespaces were removed from the end of each line with such an error as per instruction form [Stack Overflow](https://stackoverflow.com/questions/21410075/what-is-trailing-whitespace-and-how-can-i-handle-this).

**4. E127: Continuation Line Over-Indented for Visual Indent**
- Description: This error occurs when a continuation line is indented farther than it should be for a visual indent.
- Resolution: The indentations of the continuation lines were adjusted to align with the opening delimiter of the construct they belong to as per instruction from [Stack Overflow](https://stackoverflow.com/questions/21947121/pep8-continuation-line-over-indented-for-visual-indent).

**5. E712: Comparison to False Should Be ‘if cond is False’**
- Description: This error occurs when comparing a value to False using the == operator.
- Resolution: 'if not cond:' was used instead of 'if cond == False:' as per instructions from [Stack Overflow](https://stackoverflow.com/questions/54474042/how-to-fix-the-flake-8-error-e712-comparison-to-false-should-be-if-cond-is-fal).


### Bugs

#### Solvd Bugs

After adding Colorama module Python package to the code to be able to change twxt color and improve user experience, the project was successfully running locally in Gitpod. However after the deployment the following error was identified: 'ModuleNotFoundError'.

```Traceback (most recent call last):
  File "/app/run.py", line 5, in <module>
    from colorama import init, Fore, Back, Style
ModuleNotFoundError: No module named 'colorama'
```

**Solution**
1. Colorama was reinstalled using command:

   ```pip3 install colorama```

2. Requirements file was updated by adding ```colorama==0.4.6``` to requirements.txt file.

### Remaining Bugs
No bugs remaining

### Validator Testing

## Deployment

The calculator app is hosted on Heroku, a container-based cloud platform designed for app development, deployment, and management. It was deploied followign the steps below.

Deployment Steps:

1. Log into Heroku Account

2. Create a New App:
   - Click on 'Create new app', enter a name for the app and select a region, then click 'Create app'.

3. Access Settings:
   - Go to the 'Settings' tab of the created app.

4. Configure Environment Variables:
   - Navigate to the 'Config Vars' section to set up environment variables:
     - Click 'Reveal Config Vars'.
     - Add key-value pair to allow connection to API and access the spreadsheet
         - For the KEY, enter `CREDS` in all capital letters.
         - Go to Gitpod workspace, open the `creds.json` file, and copy its content.
         - Paste this content into the 'VALUE' field next to the `CREDS` key on Heroku. Click 'Add'.
     - Add another key-value pair to improve compatibility with Python libraries:
       - KEY: `PORT`
       - VALUE: `8000`

5. Add Buildpacks:
   - Under the 'Settings' tab, locate the 'Buildpacks' section.
   - Click 'Add Buildpack', select 'python', and then 'Save changes'.
   - Repeat the process to add 'nodejs' as another buildpack, ensuring they are in the order: Python followed by NodeJS.

6. Set Up Deployment from GitHub:
   - Switch to the 'Deploy' tab.
   - Choose 'GitHub' as the deployment method and connect to GitHub account.
   - In the search bar, type the repository name `body-fat-percent-calculator` and click 'Search' to find it on GitHub.
   - Click 'Connect' to link the Heroku app to the GitHub repository.

7. Deployment
   - Click on 'Enable Automatic Deploys'
   - Make sure the main branch is selected, then click 'Deploy Branch'
   - Await the build process. Once complete, a message is displayed 'your app was successfully deployed'.

8. View Deployed App:
   - Click on the 'View' button to see the deployed project. 


## Credits


