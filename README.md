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


