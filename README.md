# Frankenswitch Submission Website



## 5-Hourly Breakdown (not doing it weekly, but it'll total to >30 hrs)

- Given 30 hrs and 6 weeks, we get around 5 hrs a week. This project will take way longer though.

| Weekly/five-hourly goal      | Requirement                                                  | Done |
| ---------------------------- | ------------------------------------------------------------ | ---- |
| Hour 0-5                     | Create frontend UI for the form. Components created and used together | y    |
| Hour 5-10                    | Add repository. Start learning how to create a database/use SQL. Create a small python database for blacklisted combinations. Further break down requirements as project gets approved. | y    |
| Hour 10-15                   | Database created and information can be retrieved from it. Python backend and API created. Frontend and backend can communicate with each other. Error messages correctly display when blacklisted combos given. | y    |
| Hour 15-20                   | User authentication using Google login added. Create routes for login and form submission. Backend should correctly submit combos to spreadsheet. Authenticated users should appear on the spreadsheet. | y    |
| Hour 20-25                   | XSS Vulnerabilities tested. SQL Injections Tested. Format String vulnerabilities tested. Report started. |      |
| Hour 25-30                   | Finish adding switches to database. Add bonus requirements like text feedback/additional notes. | y    |
| Hour 30-35                   | Finish report. Website hosted. Get feedback from the community. Write report on feedback. |      |
| Extra hours (5-10 hrs total) | General blog posts (4 hrs total) about progress. Planning out project. |      |



## TODOs

### Frontend

- Blacklisted combinations retrieved from backend
  - Backend receives the switch combination and checks whether it is blacklisted
  - If it is, fail it when it returns
  - Needs to give which switch parts are failed and why it failed

- User Authentication using Google Login
  - Login screen with URL attached to it
- Style frontend with cohesive scheme
- Errors Shown 
  - Invalid switch combination (blacklisted)
  - Combo added already



### Backend

- Send API to add to spreadsheet
- Authorised users have symbol next to name in spreadsheet
- Flask backend server created
  - backend can communicated to frontend



## Testing

- XSS Vulnerabilities
- SQL Injections
- Format String vulnerabilities
- Report on above 3 generated



## Website hosted

- Temporarily, I'll host it myself



## Non-priorities

- Add required modifications (crimping) to certain switch combinations if needed
- Allow authorised users to add to the blacklisted backend
- Allow users to add to the switch backend
- Make a way to add blacklisted combinations to backend by authorised users



| Grade | Requirement                                                  |
| ----- | ------------------------------------------------------------ |
| HD    | Website has cohesive colour scheme, font and fully styled  (CSS) user interfaces. Input forms have meaningful errors if they occur.  Different URLs for logging in and form submission. Login is optional and  allows users to enter data anonymously or as guests. Website is hosted and  feedback from community is gained with report made. |
| D     | Comprehensive Vulnerabilities test with report produced. XSS,  SQL injections, Format String vulnerabilities all thoroughly tested. |
| CR    | User authenticated with google sign in form.  Moderator/Verified user tag appears next to person's name in the google  sheet. |
| P     | Website with simple input form. Blacklist database, switch  database created. |


# Completed

- Python-based backend for managing the databases. `psycopg2` 
- Blacklisted switch combination database created
- Switch database created (or should I yank it from the spreadsheet?)