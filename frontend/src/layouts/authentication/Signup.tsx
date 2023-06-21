
import React, { useState, ChangeEvent, FormEvent, useReducer, useContext, Dispatch } from 'react';
import { Container, Form, Button, Collapse } from 'react-bootstrap';
import AuthApi from '../../api/AuthApi';
import { randomUUID } from 'crypto';
import { useNavigate } from "react-router-dom";



function Signup() {

  interface TermsAgreements {
    agreeTerms: boolean;
    agreePrivacyPolicy: boolean;
    agreeDataProcessing: boolean;
  }
  const navigate = useNavigate();
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [address, setAddress] = useState('');
  const [dob, setDob] = useState('');
  const [termsAgreements, setTermsAgreements] = useState<TermsAgreements>({
    agreeTerms: false,
    agreePrivacyPolicy: false,
    agreeDataProcessing: false,
  });
  const [showTerms1, setShowTerms1] = useState(false);
  const [showTerms2, setShowTerms2] = useState(false);
  const [showTerms3, setShowTerms3] = useState(false);

  function test(){
    setPassword("wjdh7578@")
    setName("지정호")
    setEmail("hodob76@gmail.com")
    setPhone("01030347578")
    setAddress("테스트 주소")
    setTermsAgreements({
      agreeTerms: true,
      agreePrivacyPolicy: true,
      agreeDataProcessing: true,
    })
  }



  const [error, setError] = useState("undefined");
  const handleSubmit = (e:  React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    // Handle form submission here
  };
  const handleAgreementChange = (e: ChangeEvent<HTMLInputElement>) => {
    const { name, checked } = e.target;
    setTermsAgreements((prevAgreements) => ({
      ...prevAgreements,
      [name]: checked,
    }));
  };

  const { agreeTerms, agreePrivacyPolicy, agreeDataProcessing } = termsAgreements;

  const toggleTerms1 = () => {
    setShowTerms1(!showTerms1);
  };
  const toggleTerms2 = () => {
    setShowTerms2(!showTerms2);
  };
  const toggleTerms3 = () => {
    setShowTerms3(!showTerms3);
  };

  const register = async (event: React.MouseEvent<HTMLButtonElement> ) => {
    if (event) {
      event.preventDefault();
    }
    // if (firstName === "") {
    //   return setError("You must enter your first name.");
    // }
    // if (email === "") {
    //   return setError("You must enter your email.");
    // }
    // if (password === "") {
    //   return setError("You must enter a password.");
    // }
    try {
      let response = await AuthApi.Register({
        password,
        name,
        email,
        phone,
        address,
        dob,
        agreeTerms,
        agreePrivacyPolicy,
        agreeDataProcessing,
      });
      if (response.data && response.data.success === false) {
        return setError(response.data.msg);
      }
      return navigate("/authentication/login")
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
      <h1>Member 회원가입</h1>
      <Form onSubmit={handleSubmit}>
      <Form.Group controlId="email">
          <Form.Label>Email address</Form.Label>
          <Form.Control
            type="email"
            placeholder="Enter Email"
            value={email}
            onChange={(e: any) => setEmail(e.target.value)}
          />
        </Form.Group>
        <Form.Group controlId="password">
          <Form.Label>Password</Form.Label>
          <Form.Control
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e: any) => setPassword(e.target.value)}
          />
        </Form.Group>

        <Form.Group controlId="confirmPassword">
          <Form.Label>Confirm Password</Form.Label>
          <Form.Control
            type="password"
            placeholder="Confirm Password"
            value={confirmPassword}
            onChange={(e: any) => setConfirmPassword(e.target.value)}
          />
        </Form.Group>

        <Form.Group controlId="name">
          <Form.Label>Name</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter Name"
            value={name}
            onChange={(e: any) => setName(e.target.value)}
          />
        </Form.Group>



        <Form.Group controlId="phone">
          <Form.Label>Mobile Phone</Form.Label>
          <Form.Control
            type="tel"
            placeholder="Enter Mobile Phone"
            value={phone}
            onChange={(e: any) => setPhone(e.target.value)}
          />
        </Form.Group>

        <Form.Group controlId="address">
          <Form.Label>Address</Form.Label>
          <Form.Control
            as="textarea"
            placeholder="Enter Address"
            value={address}
            onChange={(e: any) => setAddress(e.target.value)}
          />
        </Form.Group>

        <Form.Group controlId="dob">
          <Form.Label>Date of Birth</Form.Label>
          <Form.Control
            type="date"
            placeholder="Enter Date of Birth"
            value={dob}
            onChange={(e: any) => setDob(e.target.value)}
          />
        </Form.Group>

        <Form.Group controlId="agreeTerms">
          <Form.Check
            type="checkbox"
            label="이용약관동의 (필수)"
            name="agreeTerms"
            checked={agreeTerms}
            onChange={handleAgreementChange}
          />
        </Form.Group>
        <Button variant="link" onClick={toggleTerms1} className="mb-3">
          {showTerms1 ? '상세내용닫기' : '상세내용'}
        </Button>

        <Collapse in={showTerms1}>
          <div>
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ut lectus in purus scelerisque pharetra ut vel dolor.
              Nullam feugiat pharetra semper. Vivamus interdum consequat massa, eget mattis arcu feugiat eu. Suspendisse userid malesuada nunc.
              Integer vitae massa vel justo ullamcorper aliquet. Fusce placerat metus userid felis fermentum facilisis.
              Morbi a rhoncus odio. Suspendisse vitae sem et ex suscipit egestas. Praesent bibendum felis vitae ante malesuada, eget molestie orci rhoncus.
              Etiam tincidunt sem vel pharetra lacinia. Aenean dignissim tellus a lacus pulvinar, nec bibendum elit tempor.
            </p>
            <p>
              Donec in tristique metus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae;
              Sed vitae sagittis urna, userid sollicitudin sapien. Maecenas cursus scelerisque dui, vitae fermentum arcu finibus nec.
              Proin efficitur feugiat velit, sit amet elementum felis pellentesque eget. Aliquam volutpat lacus at dapibus iaculis.
              Integer userid lectus nisl. Fusce at volutpat orci, nec pulvinar sem. Nunc blandit vestibulum est at aliquam.
            </p>
          </div>
        </Collapse>

        <Form.Group controlId="agreePrivacyPolicy">
          <Form.Check
            type="checkbox"
            label="개인정보 수집 및 이용동의 (필수)"
            name="agreePrivacyPolicy"
            checked={agreePrivacyPolicy}
            onChange={handleAgreementChange}
          />
        </Form.Group>
        <Button variant="link" onClick={toggleTerms2} className="mb-3">
          {showTerms2 ? '상세내용닫기' : '상세내용'}
        </Button>

        <Collapse in={showTerms2}>
          <div>
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ut lectus in purus scelerisque pharetra ut vel dolor.
              Nullam feugiat pharetra semper. Vivamus interdum consequat massa, eget mattis arcu feugiat eu. Suspendisse userid malesuada nunc.
              Integer vitae massa vel justo ullamcorper aliquet. Fusce placerat metus userid felis fermentum facilisis.
              Morbi a rhoncus odio. Suspendisse vitae sem et ex suscipit egestas. Praesent bibendum felis vitae ante malesuada, eget molestie orci rhoncus.
              Etiam tincidunt sem vel pharetra lacinia. Aenean dignissim tellus a lacus pulvinar, nec bibendum elit tempor.
            </p>
            <p>
              Donec in tristique metus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae;
              Sed vitae sagittis urna, userid sollicitudin sapien. Maecenas cursus scelerisque dui, vitae fermentum arcu finibus nec.
              Proin efficitur feugiat velit, sit amet elementum felis pellentesque eget. Aliquam volutpat lacus at dapibus iaculis.
              Integer userid lectus nisl. Fusce at volutpat orci, nec pulvinar sem. Nunc blandit vestibulum est at aliquam.
            </p>
          </div>
        </Collapse>

        <Form.Group controlId="agreeDataProcessing">
          <Form.Check
            type="checkbox"
            label="개인정보 수집 및 이용동의 (선택)"
            name="agreeDataProcessing"
            checked={agreeDataProcessing}
            onChange={handleAgreementChange}
          />
        </Form.Group>
        <Button variant="link" onClick={toggleTerms3} className="mb-3">
          {showTerms3 ? '상세내용닫기' : '상세내용'}
        </Button>

        <Collapse in={showTerms3}>
          <div>
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ut lectus in purus scelerisque pharetra ut vel dolor.
              Nullam feugiat pharetra semper. Vivamus interdum consequat massa, eget mattis arcu feugiat eu. Suspendisse userid malesuada nunc.
              Integer vitae massa vel justo ullamcorper aliquet. Fusce placerat metus userid felis fermentum facilisis.
              Morbi a rhoncus odio. Suspendisse vitae sem et ex suscipit egestas. Praesent bibendum felis vitae ante malesuada, eget molestie orci rhoncus.
              Etiam tincidunt sem vel pharetra lacinia. Aenean dignissim tellus a lacus pulvinar, nec bibendum elit tempor.
            </p>
            <p>
              Donec in tristique metus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae;
              Sed vitae sagittis urna, userid sollicitudin sapien. Maecenas cursus scelerisque dui, vitae fermentum arcu finibus nec.
              Proin efficitur feugiat velit, sit amet elementum felis pellentesque eget. Aliquam volutpat lacus at dapibus iaculis.
              Integer userid lectus nisl. Fusce at volutpat orci, nec pulvinar sem. Nunc blandit vestibulum est at aliquam.
            </p>
          </div>
        </Collapse>

        <Form.Group controlId="termsAgreement">
          <Form.Check
            type="checkbox"
            label="전체동의"
            checked={agreeTerms && agreePrivacyPolicy && agreeDataProcessing}
            onChange={() => {
              if (agreeTerms || agreePrivacyPolicy || agreeDataProcessing) {
                setTermsAgreements((prevAgreements) => ({
                  ...prevAgreements,
                  agreeTerms: false,
                  agreePrivacyPolicy: false,
                  agreeDataProcessing: false,
                }))
              }
              else {
                setTermsAgreements((prevAgreements) => ({
                  ...prevAgreements,
                  agreeTerms: true,
                  agreePrivacyPolicy: true,
                  agreeDataProcessing: true,
                }))
              }
            }}
          />
        </Form.Group>
        <Button
          variant="primary"
          onClick={register}
          // disabled={!agreeTerms || !agreePrivacyPolicy || !agreeDataProcessing}
          disabled={!agreeTerms || !agreePrivacyPolicy}
          >
          Sign Up
        </Button>
        <Button
          variant="primary"
          onClick={test}
          >
          test
        </Button>
      </Form>
    </Container>
  )
};


export default Signup;