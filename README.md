# whats_my_commute
A Python project that uses Google's Distance Matrix API and email services provided by Python to send a commute time from one location to another by text message to a mobile number!

This project calls a function called get_commute() that utilizes the Google Distance Matrix API by performing a GET request to the API with the proper credentials and headers provided by their documentation that returns a distance and commute time. The script then creates an email that is sent to an email address that includes the target phone number and appends a carrier specific email domain. This domain turns the email into a SMS message that the target phone number will recieve. 

This application was created for my girlfriend who has a rather lengthy commute everyday. To run this project at the same time everyday before she leaves to work, I set up a Windows Task Scheduler task to automatically run it.

## Shoutouts
Shout out to Google for their Distance Matrix API as well as their wonderful documentation to make this possible.

Shout out to Cindy for the inspiration. :-)
