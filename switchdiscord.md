# **Requirements**

## **Frontend**

- React-based frontend that has input forms for the switch name, top housing, stem, spring, bottom housing and username. (3-4hrs)

- Input forms searchable drop down menu. (10-20 mins)

- Inputs with blacklisted combinations will be denied submission (30 mins)

- Sends API request to google sheets to add to that spreadsheet (not ideal, but there's others working on a frontend for the spreadsheet so I'm just going to keep it the same for now)

- 1-2hr probably LMAO

- User authentication (1-2hr)

- Authorised users have symbol next to name in spreadsheet (1min)

 

## **Backend**

- Python-based backend for managing the databases. `psycopg2` probably since I want to overlap with COMP3311 since idk how to do this LOL (??? hrs)

- Needs to be tested against SQL based attacks (distinction, ??? hrs)
  - Report produced from the testing

- Receives request from frontend for blacklisted combos or list of switches (??? hrs)

 

## **Server?**

- Something needs to host the website, not really sure how to do this for long term use

- Need Static IP address, but can port forward the address for now? (??? hrs)



**<u>Things I Want to Implement</u>**

- React-based website that has input forms for the [switch name, top housing, stem, spring, bottom housing]
- Inputs have search and drop down
- Blacklist of switch combinations that do not work
- Form that lets user search for a specific switch type or type it in
- Sends API request to google sheets to add to that spreadsheet
- Gets a list of parts from a database
- Create the database
- Host the website - i have no clue how I'm going to do this
- 

| Grade | Requirement                                                  |
| ----- | ------------------------------------------------------------ |
| HD    | Website has cohesive colour scheme, font and fully styled  (CSS) user interfaces. Input forms have meaningful errors if they occur.  Different URLs for logging in and form submission. Login is optional and  allows users to enter data anonymously or as guests. Website is hosted and  feedback from community is gained with report made. |
| HD    | Comprehensive Vulnerabilities test with report produced. XSS,  SQL injections, Format String vulnerabilities all thoroughly tested. |
| D     | Database is integrated into the static website               |
| CR    | User authenticated with google sign in form.  Moderator/Verified user tag appears next to person's name in the google  sheet. |
| P     | Website with simple input form. Blacklist database, switch  database created. |

https://github.com/toperkin/staticFormEmails/blob/master/README.md

- can send requests to google forms