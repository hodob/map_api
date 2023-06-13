import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
// import NavDropdown from 'react-bootstrap/NavDropdown';

function NavbarLayout() {
  return (
    <Navbar bg="light" expand="lg">
      <Container>
        <Navbar.Brand href="/">(주)다츠</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="/authentication/signup">회원가입</Nav.Link>
            <Nav.Link href="/authentication/login">로그인</Nav.Link>
            <Nav.Link href="/authentication/logout">로그아웃</Nav.Link>

            {/* <NavDropdown title="Dropdownㅇㅇㅇ" id="basic-nav-dropdown">
              <NavDropdown.Item href="#action/3.1">Actioㅇㅇn</NavDropdown.Item>
              <NavDropdown.Item href="#action/3.2">
                Another actㅇㅇion
              </NavDropdown.Item>
              <NavDropdown.Item href="#action/3.3">Sometㅇㅇhing</NavDropdown.Item>
              <NavDropdown.Divider />
              <NavDropdown.Item href="#action/3.4">
                Separated ㅇㅇlink
              </NavDropdown.Item>
            </NavDropdown> */}

          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavbarLayout;