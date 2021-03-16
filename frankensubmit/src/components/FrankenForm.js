import React from 'react';
import Input from "./Input.js";
import "../style/FrankenForm.css";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import Alert from "react-bootstrap/Alert";
import { useHistory, useLocation } from 'react-router-dom';
const choiceError = "Please Choose a Switch from the dropdown";

async function getSwitches() {
    const url = `http://localhost:1337`;


    const options = {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    };

    let res = await fetch(url + "/switches", options);
    return res.json();
}

async function submitCombo(top, stem, bottom, info) {
  const url = `http://localhost:1337`;

  const options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(
      {
        top,
        stem,
        bottom,
        info,
      })
  };

  let res = await fetch(url + "/submit", options);
  return res.json();

}



export default function FrankenForm() {
  // TODO: error key is unused for now, idea was to state which parts were problematic
  //  but that is a little out of the scope of what I can do right now
  const [parts, setParts] = React.useState({
    "Top Housing": {part: [], error: ""},
    Stem: {part: [], error: ""},
    Spring: {part: [], error: ""},
    "Bottom Housing": {part: [], error: ""},
  });
  const [invalid, setInvalid] = React.useState("");
  const [switchData, setSwitchData] = React.useState([""]);
  const history = useHistory();
  const location = useLocation();

  React.useEffect(() => {

    // Get the list of switches from the backend
    async function updateOptions() {
      const res = await getSwitches();
      // TODO: handle any errors that occur here
      setSwitchData(res);

    }

    updateOptions()

  }, []);


  async function handleSubmit(e) {
    e.preventDefault();
    e.stopPropagation();
    setInvalid("");
    let info = {
      google: location.state ? location.state.google : null,
    }
    let success = await submitCombo(parts["Top Housing"], parts["Stem"], parts["Bottom Housing"], info)

    // TODO: better error handler, allow other error types to be displayed like warnings
    //  Backend should return a dict with key=type of error, value = warning?
    if (success.error) {
      setInvalid(success.error);
    } else {
      // TODO: handle success
      console.log("Switch submitted!")
      history.push("/success");
    }
  }

  return (
    <div className={"FrankenForm"}>
      <h1 className={"FFTitle"}> Frankenswitch Submission! </h1>
      <div className={"FFContainer"}>
        <div>
          {invalid ? <Alert variant={"danger"}> {invalid} </Alert> : ""}
        </div>

        <Form onSubmit={(e) => {handleSubmit(e)}}>
          <Form.Group>
            <Input className={"FFInput"} name={"Top Housing"} type={"Switch"} setInput={setParts} input={parts} data={switchData}>
              <Form.Control.Feedback type={"invalid"}>
                <div className="FrankenFormError">
                  {choiceError}
                </div>
              </Form.Control.Feedback>
            </Input>

            <Input className={"FFInput"} name={"Stem"} type={"Switch"} setInput={setParts} input={parts} data={switchData}>
              <Form.Control.Feedback type={"invalid"} className="FrankenFormError">
                <div className="FrankenFormError">
                  {choiceError}
                </div>
              </Form.Control.Feedback>
            </Input>

            <Input className={"FFInput"} name={"Spring"} type={"Spring"} setInput={setParts} input={parts} data={switchData}>
              <Form.Control.Feedback type={"invalid"}>
                <div className="FrankenFormError">
                  {choiceError}
                </div>
              </Form.Control.Feedback>
            </Input>

            <Input className={"FFInput"} name={"Bottom Housing"} type={"Switch"} setInput={setParts} input={parts} data={switchData}>
              <Form.Control.Feedback type={"invalid"}>
                <div className="FrankenFormError">
                  {choiceError}
                </div>
              </Form.Control.Feedback>
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
