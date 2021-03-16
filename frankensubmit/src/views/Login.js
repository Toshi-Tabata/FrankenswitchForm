import React from 'react';
import GoogleLogin from 'react-google-login';
import Token from '../token.json';
import { useHistory } from 'react-router-dom';
import "../style/Login.css";
import Button from "react-bootstrap/Button";

export default function Login() {
  const history = useHistory()

  function signIn() {
    history.push("/submit");
  }

  const responseGoogle = (response) => {
    console.log(response);

    if (!response.error) {
      console.log(response.Is.sd)
      history.push("/submit", {google: response})

    } else {
      console.log(response.error);
    }
  }

  return(
    <div id="loginContainer">
      <h1 id="loginTitle"> Frankenswitch Submissions </h1>
      <div id="loginButtons">
        <GoogleLogin
          clientId={Token.client_id}
          buttonText="Login"
          onSuccess={responseGoogle}
          onFailure={responseGoogle}
          isSignedIn={true}
          cookiePolicy={'single_host_origin'}
          render={renderProps => (
            <Button variant="dark" onClick={renderProps.onClick} className="loginButtons">
              Sign In With Google
            </Button>
          )}
        />
        <Button variant="dark" onClick={signIn} className="loginButtons"> or continue as guest </Button>
      </div>

    </div>

  )
}
