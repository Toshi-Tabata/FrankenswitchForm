import React from 'react';
import GoogleLogin from 'react-google-login';
import Token from '../token.json';
import { useHistory } from 'react-router-dom';

export default function Login() {
  const history = useHistory()
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
    <GoogleLogin
      clientId={Token.client_id}
      buttonText="Login"
      onSuccess={responseGoogle}
      onFailure={responseGoogle}
      isSignedIn={true}
      cookiePolicy={'single_host_origin'}
    />
  )
}
