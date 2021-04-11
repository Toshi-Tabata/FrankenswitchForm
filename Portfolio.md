# Portfolio (c) report

## Summary

- Different Mechanical keyboard switches can be combined to create different switches (called a "Frankenswitch")
- Users submit these combinations through a google form which gets put in this spreadsheet https://docs.google.com/spreadsheets/d/1gVWWT5wYcVID40-PsT-ShBgA2iDP41zocHeIH0XxVHg/edit?usp=sharing
- The problem is that Frankenswitches that do not work or random text can be input into the google form, cluttering the spreadsheet.
- I solved this by creating a website that filters user input by only allowing switches contained in the backend's SQL database to be input.
- The SQL database contains almost every existing switch.



## Project Scope

| Project Scope                                                | Deliverables                                                 |                                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Allow user to submit Frankenswitches to the spreadsheet      | Website contains inputs for the top housing, bottom housing, stem and spring | User can input what switch they desire for each part https://imgur.com/PE0Fieo |
| Prevent malformed inputs to the spreadsheet                  | Website will not allow user input to be submitted that is not part of a switch in the database | Frontend inputs prevent submissions of switches that don't exist in backend provided database. Backend will not add switch parts that do not exist in the backend. https://imgur.com/hdEyoi3 |
| Prevent SQL injections from being performed on the backend   | SQL injection attempts to functions containing user input and database accessing do not succeed | All SQL database accesses that contain user input are done through inbuilt query parameters that are made specifically to prevent SQL injections. See report. https://i.imgur.com/Qx10z1N.png, https://i.imgur.com/oYLIX1F.png, https://github.com/Toshi-Tabata/FrankenswitchForm/blob/main/security%20report.md |
| Prevent XSS attacks from occurring in the frontend           | Data given by the user cannot be used to automatically redirect a user to an external website | No user inputs are stored internally within the frontend. User input is used to search through react bootstrap typeahead. See report. https://github.com/Toshi-Tabata/FrankenswitchForm/blob/main/security%20report.md |
| Prevent duplicate Frankenswitch submissions                  | Frontend will reject a user submission if it had already been submitted in the past | User's selection is sent to the backend. The backend has a table containing all switch combinations that have been submitted and checks if the submitted combination exists in the database. https://i.imgur.com/vAvMiyZ.png, https://i.imgur.com/Un7BeSp.png |
| Prevent submissions of switch combinations that do not work  | Frontend will reject a user submission if it contains a combination that is known to fail | User's selection sent to backend and checked if it is contained in the blacklist table. https://i.imgur.com/Un7BeSp.png |
| Have user authentication to determine who is trusted/verified | Login Screen                                                 | Used Google's login authenticator to allow optional login which allows a verified tag to appear on the spreadsheet when adding. Also automatically adds username to credit creator of the Frankenswitch. https://imgur.com/eQMPER7, https://imgur.com/N5n3D1G, https://i.imgur.com/ZbBcoyp.png |
| String format vulnerability                                  | Website is not vulnerable to string format                   | See report. https://github.com/Toshi-Tabata/FrankenswitchForm/blob/main/security%20report.md |
| Host the website                                             | External users can access the website                        | Did not manage to host it due to 30 hr time constraint       |
| Implement it and replace the existing spreadsheet.           | External users can use the website to enter into the existing spreadsheet | Did not manage to host it due to 30 hr time constraint       |
| Get user feedback about it and make improvements.            | Real users of the spreadsheet give feedback on the website   | Did not manage to host it due to 30 hr time constraint and website would have needed to be hosted. |



## Reflection

Overall I did not expect to get the website deployed, as indicated by my initial notes in the README and that indeed was the case. 

The initial requirements I proposed were predicted to take around 28 hrs which seemed reasonable, but did not get approved until superfluous additional features were added, such as user authentication, multiple routes for login, submission, hosting and user feedback. In hindsight I should have pushed back and fought for why I thought the initial requirements were more than reasonable since the new proposal easily exceeded 40hrs of work.

I did try and readjust the requirements with justification but apparently that is impossible once it has been logged.



## Time Spent

- 39 hrs for just the project.
  - SQL database has a lot of constraints to prevent invalid inserts
  - I did a lot of research to find a reliable source of a list of switches (https://docs.google.com/spreadsheets/d/1TJAIiWmwYkhnI_w5xcOl_RRXZvgYcJoAfOxHFholcFE/edit)
  - Originally this spreadsheet was not formatted nicely so I contributed to reformatting it (I didn't add this to the time I spent to the project)
  - I parse the spreadsheet and populate my spreadsheet
  - I had 0 experience with SQL or psycopg2 so I had to learn all of this from scratch (did not add this time to time spent)
  - Frontend from scratch is inherently a large time sink
  - Learning how to properly use Google's login and authenticator took a bit of time to implement, especially with React
  - Needed to create an API/server to allow frontend to get information from backend
- Additional 5.5 hrs across the course from blogging and writing the report and creating the video.

- Additional 2hrs 15 mins on this. 6pm-8:25pm.

