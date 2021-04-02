import React from "react";
import { BrowserRouter, Switch, Route } from 'react-router-dom';

import FrankenForm from "./components/FrankenForm.js";
import SubmitSuccess from "./views/SubmitSuccess.js";

import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import Login from "./views/Login.js";
import Submit from "./views/Submit.js";


function App() {
  return (
    <BrowserRouter id="appContainer">
      <Switch>
        <Route path="/(|login)">
        {/*  TODO: create login screen */}
          <Login />
        </Route>

        <Route path="/submit">
          <Submit className="App">

          </Submit>

        </Route>

        <Route path="/success">
          <SubmitSuccess />
        </Route>
        <Route path="">
          <div> 404 not found </div>
        </Route>

      </Switch>


    </BrowserRouter>



  );
}

export default App;
