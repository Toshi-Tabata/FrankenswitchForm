import React from 'react';
import Input from "./Input.js";
import "../style/FrankenForm.css";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import Alert from "react-bootstrap/Alert";

const choiceError = "Please Choose a Switch from the dropdown";

export default function FrankenForm() {
  const [parts, setParts] = React.useState({
    "Top Housing": {part: [], error: "a"},
    Stem: {part: [], error: "b"},
    Spring: {part: [], error: "c"},
    "Bottom Housing": {part: [], error: "d"},
  });
  const [invalid, setInvalid] = React.useState(false);

  function validateFranken() {
    // TODO: set API request to backend which will verify that the combo works/doesn't work
    // TODO: how do I verify? When we find one that needs a specific mod (crimping), need to add it to the spreadsheet
    //  Database should contain all 4 but some can be null which we ignore
    // TODO: show the error at the top of the screen, listing all the problematic parts
    setInvalid(false);
    let prevParts = {...parts}

    // TODO: delete this, just for testing
    if (prevParts["Top Housing"].part && prevParts["Top Housing"].part[0] === "cherry") {
      // TODO: this is how we would blacklist and bring up errors with switch combinations.
      prevParts["Top Housing"].part = []
      prevParts["Top Housing"].error = "Testing!@!"
      setInvalid(true);
    }

    setParts(prevParts);
  }

  function getErrorMessage() {
    return parts["Top Housing"].error;
  }

  function handleSubmit(e) {
    e.preventDefault();
    e.stopPropagation();

    validateFranken();

    console.log(parts);
  }

  return (
    <div className={"FrankenForm"}>
      <h1 className={"FFTitle"}> Frankenswitch Submission! </h1>
      <div className={"FFContainer"}>
        {invalid ? <Alert variant={"danger"}> {getErrorMessage()} </Alert> : ""}


        <Form onSubmit={(e) => {handleSubmit(e)}}>
          <Form.Group>

            <Input className={"FFInput"} name={"Top Housing"} type={"Switch"} setInput={setParts} input={parts}>
              <Form.Control.Feedback type={"invalid"}>{choiceError}</Form.Control.Feedback>
            </Input>

            <Input className={"FFInput"} name={"Stem"} type={"Switch"} setInput={setParts} input={parts}>
              <Form.Control.Feedback type={"invalid"}>{choiceError}</Form.Control.Feedback>
            </Input>
            <Input className={"FFInput"} name={"Spring"} type={"Spring"} setInput={setParts} input={parts}>
              <Form.Control.Feedback type={"invalid"}>{choiceError}</Form.Control.Feedback>
            </Input>
            <Input className={"FFInput"} name={"Bottom Housing"} type={"Switch"} setInput={setParts} input={parts}>
              <Form.Control.Feedback type={"invalid"}>{choiceError}</Form.Control.Feedback>
            </Input>
            <Button variant="dark" type="submit">
              Submit
            </Button>
          </Form.Group>
        </Form>
      </div>

    </div>
  )
}
