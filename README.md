# Sandra's Kitchen

## Introduction

Sandra's Kitchen is a restaurant booking website aimed at providing a secure place for customers to make and manage bookings.

# UX

## Strategy 

I used an agile methodology when planning the project via the use of projects and issues. The latter used to create user stories which formed the main guide when building the project.

## External User Goal

The customer wants to book a table at a restaurant.

## User Stories

- As a user I want to book multiple seats.
- As a user I want to book a specific date.
- As a user I want to book a specific time.
- As a user I want to see the restaurant menu.
- As a user I want to see the restaurant opening times.
- As a user I want to edit my booking.
- As a user I want to delete my booking.
- As a user I want to register an account.
- As a user I want to log into my an account.
- As an admin I want to delete accounts.
- As an admin I want to edit a booking.
- As an admin I want to delete a booking.


## Site Owner Goal

- Provide attractive site for customer booking.

## Wireframes 

#### Menu

![Menu Desktop View](documentation/wireframes/menu-desk.png)
![Menu Mobile View](documentation/wireframes/menu-mob.png)

#### Registration

![Registration Desktop View](documentation/wireframes/registration-desk.png)
![Registration Mobile View](documentation/wireframes/registration-mob.png)

#### Login

![Login Desktop View](documentation/wireframes/login-desk.png)
![Login Mobile View](documentation/wireframes/login-mob.png)

#### Booking

![Booking Desktop View](documentation/wireframes/reservation-desk.png)
![Booking Mobile View](documentation/wireframes/reservation-mob.png)

## Features

### Login Page
![Login Page]()

### Registration Page
![Registration Page]()

### Gallery of Menu
![Gallery of Menu]()

### Menu Page with title and details
![Menu Page]()

### Booking page
![Booking Page]()

## Technologies Used

- Git used for version control.
- [GitHub]() was used for securely storing code.
- [Gitpod](https://gitpod.io/) is the cloud based IDE.
- Python3 is used for the main code logic.
- [Django](https://www.djangoproject.com/) was used as the framework
- PostgreSQL
- 
- [Heroku](https://heroku.com/) was used for live deployment.
- [ShareX](https://getsharex.com/) for capturing screenshots.

## Testing

To view all testing documentation please refer to [TESTING.md](TESTING.md)

### Deployment

The site was deployed using [Heroku](https://heroku.com/). The app can be found using this link - [Mama's Kitchen](https://sandras-kitchen.herokuapp.com/).

The steps are as follows:

- Log-in or Sign-up to Heroku.
- From the Dashboard click "New" then "Create New App".
- Enter a project name (unique), select a region then press "Create app".
- This will create an app and open the deploy tab. From here select the "Settings" tab.
- Set your Environment Variables by navigating to Reveal Config Vars.
Scroll up and head to the "Deploy" section to choose deployment method. Select "GitHub" and in the "connect to GitHub" section link your GitHub account.
- Scroll down to the manual deploy option and select "Deploy Branch".
- The app will now be built. Once completed a 'Your App Was Successfully Deployed' message and a link will appear.

### Local Deployment

To make a local copy of this project, you can clone it by typing the following in your IDE terminal:

- `git clone https://github.com/devisis/sandras-kitchen.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/devisis/sandras-kitchen)

Once your project is ready for coding, you must download the required dependencies from the requirements.txt file. You can type:

- `pip3 install -r requirements.txt`

Please note, for this particular project, there aren't any required dependencies, however, the file is still necessary in order to get the application running on Heroku.
Additionally, Heroku will require a `Procfile`, so you can type:

- `echo web: node index.js > Procfile`

### Acknowledgements

- Thank you to my mentor for help and support.
