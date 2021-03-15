import React from "react";
import { BrowserRouter, Switch, Route } from 'react-router-dom';

import FrankenForm from "./components/FrankenForm.js";
import SubmitSuccess from "./views/SubmitSuccess.js";

import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import Login from "./views/Login.js";


function App() {
  return (
    <BrowserRouter id="appContainer">
      <Switch>
        <Route path="/login">
        {/*  TODO: create login screen */}
          <Login />
        </Route>

        <Route path="/submit">
          <div className="App">
            <FrankenForm />
          </div>
        </Route>

        <Route path="/success">
          <SubmitSuccess />
        </Route>

      </Switch>


    </BrowserRouter>



  );
}

export default App;
