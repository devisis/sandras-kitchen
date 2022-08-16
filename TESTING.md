# Testing

To return to readme documentation please click here [README.md](README.md)

## User Story Testing

### As a user I want to book multiple seats.

- A user has the option of entering a number themselves, or pressing the arrows situated to the right until they reach a number that suits them. As there are a limited amount of seats avaiable, if a user selects a number greater than this limit then an error is displayed.

![Booking Seats](documentation/features/reservation_form_filled.png)

### As a user I want to book a specific date.

- A user has the option of entering a date themselves, or selecting from the calender. As there are a limited amount of bookings avaiable, users are limited to one booking per day.
- Users are not allowed to book on the same day or a date that's in the past.

![Booking Date](documentation/features/reservation_form_filled.png)

### As a user I want to book a specific time.

- Users can enter a time themselves or select from the time input function.

![Booking Time](documentation/features/reservation_form_filled.png)

### As a user I want to see the restaurant menu.

- When a user clicks on the menu navigation option they are taken to the menu page.

![Menu](documentation/features/menu_page.png)

### As a user I want to edit my booking.

- A user has the option to edit their booking when they press the update button. Once they press submit if the form validates then it will update their initial booking.

![User Edit Bookings](documentation/features/update_reservation.png)

### As a user I want to delete my booking.

- When the user chooses to delete their booking they are sent to a delete confirmation page where it asks if they are sure they want to make this decision. If yes the reservation will be deleted.

![User Delete Bookings](documentation/features/delete_confirmation.png)

### As a user I want to register an account.

- After navigation to the registration page a user is able to enter their details and register for the site.

![Registration](documentation/features/registration_page.png)

### As a user I want to log into my an account.

- If the user enters the correct login details they will be granted access to the website

![Login](documentation/features/log_in.png)

### As an admin I want to delete accounts.

- As an admin I can select which accounts I would like to delete through the admin panel.

![Admin Delete Account](documentation/testing/delete_user_accounts.png)

### As an admin I want to edit a booking.

- As an admin I have access to all user bookings and have the option to update them.

![Admin Edit Booking](documentation/testing/manage_reservations_admin.png)

### As an admin I want to delete a booking.

- As an admin I have access to all user bookings and have the option to delete them.

![Admin Delete Booking](documentation/testing/manage_reservations_admin.png)


## Code Validation

### HTML

[Nu Html Checker](https://validator.w3.org/)
[rocketvalidator](https://rocketvalidator.com/)

Upon initial testing of my html I had a few issues with nesting and my head element being in the wrong place. I have fixed these issues to the best of my knowledge. 

![After fixes](documentation/testing/html_validation.png)
![Initial testing](documentation/testing/initial_html_testing.png)

### CSS 

[Jigsaw](https://jigsaw.w3.org/)

I copied and pasted my css into the input section and checked my css. Everything seems to be in order with nothing wrong.

![Jigaw validation](documentation/testing/jigsaw_validation.png)

## Browser Complatability
chrome ff edge ss

## Browser Responsiveness
- I used chrome developer settings to test the responsiveness of the site on 3 devices with varying sizes. Iphone 5, the Iphone12 and the Ipad Air.

### Iphone 5SE

![Iphone 5SE](documentation/testing/iphone_5se.png)

### Iphone 12

![Iphone 12](documentation/testing/iphone_12.png)

### Ipad Air

![Ipad Air](documentation/testing/ipad_air.png)

## Bug
ss
### Fixed Bug

### Unfixed Bug