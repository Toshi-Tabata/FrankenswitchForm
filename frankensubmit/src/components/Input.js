import React, {useState} from 'react';
import 'react-bootstrap-typeahead/css/Typeahead.css';
import Form from 'react-bootstrap/Form'
import { Typeahead } from 'react-bootstrap-typeahead';
import "../style/Input.css";
import stem from "../img/stem.svg";
import top from "../img/topHousing.svg";
import bottom from "../img/bottomHousing.svg";
import spring from "../img/spring.svg";

async function getDataFromBackend(type) {

  // switch (type) {
  //   case "Switch":
  //     return ["gateron", "jwk", "cherry"];
  //
  //   case "Spring":
  //     return ["Any", "68g", "100g", "78g"];
  //
  //   default:
  //     return [""];
  // }
}

function getPart(part) {
  let altText = "";
  let img = null;
  switch (part) {
    case "Stem":
      altText = "mx switch stem";
      img = stem;
      break;

    case "Top Housing":
      altText = "mx switch top housing";
      img = top;
      break;

    case "Bottom Housing":
      altText = "mx switch bottom housing";
      img = bottom;
      break;

    case "Spring":
      altText = "mx switch bottom housing";
      img = spring;
      break;

    default:
      return null
  }

  return (
    <div className={"InputImgContainer"}>
      <img className={"InputImg"} src={img} alt={altText} />
    </div>
  )

}

export default function Input(props) {

  function handleChange(choice) {
    let oldChoice = {...props.input}
    oldChoice[props.name]["part"] = choice;
    props.setInput(oldChoice);
  }

  return (
    <div className={"Input"}>
      <Form.Label id={"InputFormLabel"}>
        {props.name}
      </Form.Label>
      <div>
        {getPart(props.name)}
      </div>
      <Typeahead
        filterBy={["manufacturer", "name"]}
        className={props.input[props.name]["part"].length === 0 ? "is-invalid" : ""}
        inputProps={
          {
            required: true,
            shouldSelectHint: (shouldSelect, e) => {
              return e.keyCode === 13 || shouldSelect;
            }
          }
        }
        id="basic-typeahead-single"
        labelKey={option => `${option.manufacturer} ${option.name}`}
        onChange={(choice) => {handleChange(choice)}}
        placeholder={"Choose a " + props.type}
        options={props.data}
        isInvalid={props.input[props.name]["part"].length === 0}
        renderMenuItemChildren={(option) => (
          <div>
            {option.name}
            <div>
              <small>Manufacturer: {option.manufacturer}</small>
            </div>
          </div>
        )}
      />
      {props.children}
    </div>
  );
}
