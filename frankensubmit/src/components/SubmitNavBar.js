import React from "react";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import "../style/SubmitNavBar.css";
import { GoogleLogout } from 'react-google-login';
import { useLocation, useHistory } from 'react-router-dom';
import Button from "react-bootstrap/Button";
import Token from "../token.json";



export default function SubmitNavBar() {
  // TODO: pass in props for user's token
  // then use <GoogleLogout with clientId .>

  const location = useLocation();
  const history = useHistory();
  const [logoutButton, setLogoutButton] = React.useState("")



  React.useEffect(() => {
    function goToLogin() {
      history.push("/login")
    }


    let logoutElement;
    if (location.state !== null) {
      logoutElement = (
        <GoogleLogout
          clientId={Token.client_id}
          onLogoutSuccess={goToLogin}
          render={renderProps => (
            <Button onClick={renderProps.onClick}>
              Sign Out
            </Button>
          )}
        >
        </GoogleLogout>
      );

    } else {
      logoutElement = <Nav.Link id="SubmitNavBarAnon" onClick={goToLogin}> Sign In </Nav.Link>
    }


    setLogoutButton(logoutElement)
  }, [history, location.state])




  return(
    <div id="SubmitNavBarContainer">
      <Navbar bg="dark" variant="dark">
        <Navbar.Brand >Submission</Navbar.Brand>
        <Nav className="mr-auto">
          <Nav.Link href="https://docs.google.com/spreadsheets/d/1pBggUHTHfCo-mQ4604Jeh0BoPqovvDLwEamYH-keqQ8/edit#gid=0">
            Spreadsheet
          </Nav.Link>


        </Nav>
        <Nav>
            {/*TODO: only show the logout screen if location.state. Use useEffect)*/}
          {logoutButton}


        </Nav>
      </Navbar>
    </div>
  )
}
