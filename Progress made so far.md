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


20/02 3:30pm
- Added github repo https://github.com/Toshi-Tabata/FrankenswitchForm
- Broke down requirements further, still need to break each down

