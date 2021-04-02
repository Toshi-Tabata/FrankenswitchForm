# XSS Attacks

- Went through entire frontend and collated all places where user may input data
  - Login Screen - 2 buttons
    - One directly logs in and no user data is passed
    - Other redirects to google's API so I don't have control over that
      - The information from google's API is only used as-is as text to insert into google sheets via their API
      - All the possible vulnerabilities with login and its data is offloaded to google's services rather than my own (i.e. google's login API and google sheets' API)
        - The possible problem here is that I am storing the name of the logged in user which is the one place where the user could input something malicious as their google account name that I have not predefined.
        - I think it is reasonably safe to assume that the names given from Google's API is safe to be passed back into google's own API again.
  - 4 identical user inputs for searching for a switch
    -  The actual input given by the user isn't used, it's only used to search for a pre-defined input
      - the user input never gets explicitly stored in the frontend and therefore never gets sent to the backend
      - The data is used to access the table of switches which is already publicly available in the frontend. 
      - The database tables are all inaccessible from the front end since no additional data is sent from the frontend to the backend outside of the GET request itself.
      - There are two endpoints in the backend that could be attacked, one of which (the table retrieval for switches) does not accept any user input
      - The other endpoint accepts input from a POST request which could be vulnerable to SQL injections (discussed in the next section)
      - 
