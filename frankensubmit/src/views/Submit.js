import React from "react";
import FrankenForm from "../components/FrankenForm.js";
import SubmitNavBar from "../components/SubmitNavBar.js";

import "../style/Submit.css"

export default function Submit() {



  return(
    <div >
      <div id="SubmitNavBar">
        <SubmitNavBar />
      </div>

      <div id="SubmitFrankenContainer">
        <FrankenForm />
      </div>

    </div>
  )
}
