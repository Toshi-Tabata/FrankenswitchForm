# Progress made so far

20/02 5:30am - 10am

- Set up react project
- Created general file structure of the frontend 
  - Components/img/style/views
- Created dropdown menu component for selecting switch part (`Input.js`)
- Added images for each switch part
- FrankenForm.js created which uses the Input component to create each of the input forms for top housing/stem/spring/bottom housing
- Added Alert component that will allow any error messages to be displayed nicely
- Added styling (FrankenForm.css/Input.css) to add margins and make the text easier to read

- Decided on Dark grey text on white backgrounds for the general colour scheme
  - `rgb(52, 52, 52);`
  - default white for background



20/02 10:30am-1pm

- Added feedback messages for switch parts that haven't been selected
  - React-bootstrap typeahead has some UX issues with the search/dropdown menu in that you could type the full option but you can't tell if it's been selected or not
  - Used the Feedback component to alleviate some of this issue
  - Problem: feedback message is unstyled - text is huge

![image-20210220130318894](Progress made so far.assets/image-20210220130318894.png)

20/02 3:30pm - 6:30pm

- Added github repo https://github.com/Toshi-Tabata/FrankenswitchForm
- Broke down requirements further, still need to break each down
- Updated weekly breakdown

- Created python files for backend
- Attempted to create a database using `psycopg2` and postgres
- Learning about how to format the data (taking ages holy moly)
  - Thinking table for each switch part, with a table for the relations (invalid combinations) 
  - Invalid combinations table has 2 switch parts that make up an invalid combination
  - Switch parts can either be 
    - Top + Bottom
    - Stem + Top
    - Stem + Bottom
    - Bottom + stem is the same - how do i handle that?



21/02 2pm-5pm

- Created tables for 
  - top, bottom, stem, blacklisted combinations, manufacturers
- figured out how to connect between psycopg2's copy of the database and accessing it in `psql` directly
- Figured out a layout for the tables. For top/stem/bottom (edited 8:17pm to add manufacturer and variety columns):

| Name        | Manufacturer |
| ----------- | ------------ |
| "cherry mx" | "cherry"     |

- Blacklist contains at least two of top/bottom/stem, enforced by the constraints added

- Manufacturer for top/stem/bottom must be from the manufacturer table's name column



21/02 7pm - 12:30pm

- Setup credentials for google sheets' API
- Accessed switch database and parsed it for data
- Figured out how to get specific columns from the sheet, and created a module for getting this data
- Used the parsed data from the sheet to populate the tables
- Had to add the "manufacturer" and "variety" tables since the table was formatted in a way that wasn't giving enough clarification on what the "name" of the switch actually was

- Battled a ton of issues with string formatting and preventing SQL injections
  - turns out string formatting with constant strings is different from using a variable inside of a string format. You should pass in variables into `cursor.execute()` as a tuple in the second argument instead of using `psycopg2`'s string formats. 

- Due to the way switches get named, decided to just concatenate name and variety instead and get rid of the variety table

- Finally populated the switch table somewhat nicely. Most switches are present. there's some inconsistent formatting in the spreadsheet that is getting sorted so those switches are missing (e.g. razer switches don't have names)





![image-20210222225224206](Progress made so far.assets/image-20210222225224206.png)