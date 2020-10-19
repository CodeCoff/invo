import React from "react";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";

import Button from "react-bootstrap/Button";

function Navigation() {
  return (
    <div>
      <Navbar bg="light" variant="light" expand="lg">
        <Navbar.Brand href="#home">Invo</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="mr-auto" style={{ color: "red" }}>
            <Nav.Link href="#link">Product</Nav.Link>
            <Nav.Link href="#home">Features</Nav.Link>
            <Nav.Link href="#link">Pricing</Nav.Link>
          </Nav>
        </Navbar.Collapse>
        <Button variant="primary">Log In</Button>&nbsp;&nbsp;
        <Button variant="danger">Sign Up</Button>{" "}
      </Navbar>
    </div>
  );
}

export default Navigation;
