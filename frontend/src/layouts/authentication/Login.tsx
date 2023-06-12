import React, { useState } from 'react';
import { Container, Form, Button } from 'react-bootstrap';

import AuthApi from '../../api/AuthApi';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const [error, setError] = useState("undefined");

  const handleEmailChange = (event:React.ChangeEvent<HTMLInputElement>) => {
    setEmail(event.target.value);
  };

  const handlePasswordChange = (event:React.ChangeEvent<HTMLInputElement>) => {
    setPassword(event.target.value);
  };


  const login = async (event:React.MouseEvent<HTMLButtonElement>) => {
    if (event) {
      event.preventDefault();
    }

    // if (user && user.token) {
    //   return history.push("/dashboard");
    // }
    // if (email === "") {
    //   return setError("You must enter your email.");
    // }
    // if (password === "") {
    //   return setError("You must enter your password");
    // }
    // setButtonText("Signing in");
    try {
      let response = await AuthApi.Login({
        email,
        password,
      });
      if (response.data && response.data.success === false) {
        return setError(response.data.msg);
      }
    //   return setProfile(response);
    } catch (err:any) {
      console.log(err);
    
      if (err.response) {
        return setError(err.response.data.msg);
      }
      return setError("There has been an error.");
    }
  };




  return (
    <Container>
      <h1>Login</h1>
      <h1>{error}</h1>
      <Form>
        <Form.Group controlId="formEmail">
          <Form.Label>Email address</Form.Label>
          <Form.Control
            type="email"
            placeholder="Enter email"
            value={email}
            onChange={handleEmailChange}
          />
        </Form.Group>
        <Form.Group controlId="formPassword">
          <Form.Label>Password</Form.Label>
          <Form.Control
            type="password"
            placeholder="Password"
            value={password}
            onChange={handlePasswordChange}
          />
        </Form.Group>
        <Button 
        variant="primary" 
        type="submit" 
        onClick={login}
        >
          Submit
        </Button>
      </Form>
    </Container>
  );
};

export default Login;