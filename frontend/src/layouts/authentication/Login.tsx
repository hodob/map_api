import React, { useState } from 'react';
import { Container, Form, Button } from 'react-bootstrap';
import { useAuth } from '../../auth-context/auth.context';
import AuthApi from '../../api/AuthApi';
import { useNavigate } from "react-router-dom";

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const [error, setError] = useState("undefined");
  const navigate = useNavigate();
  const setUser  = useAuth().setUser;
  const user  = useAuth().user;
  console.log(user);


  const handleEmailChange = (event:React.ChangeEvent<HTMLInputElement>) => {
    setEmail(event.target.value);
  };

  const handlePasswordChange = (event:React.ChangeEvent<HTMLInputElement>) => {
    setPassword(event.target.value);
  };
  console.log(typeof user);
  console.log(typeof setUser);

  const login = async (event:React.MouseEvent<HTMLButtonElement>) => {
    if (event) {
      event.preventDefault();
    }

    if (user && user.token) {
      return navigate("/");
    }
    if (email === "") {
      return setError("You must enter your email.");
    }
    if (password === "") {
      return setError("You must enter your password");
    }
    try {
      let response = await AuthApi.Login({
        email,
        password,
      });
      if (response.data && response.data.success === false) {
        return setError(response.data.msg);
      }

      // console.log(response)
      // 
      return setProfile(response);
    } catch (err:any) {
      console.log(err);
    
      if (err.response) {
        return setError(err.response.data.msg);
      }
      return setError("There has been an error.");
    }
  };
  const setProfile = async (response:any) => {
    let user = { ...response.data.user };
    user.token = response.data.token;
    user = JSON.stringify(user);
    setUser(user);
    localStorage.setItem("user", user);
    return navigate("/");
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