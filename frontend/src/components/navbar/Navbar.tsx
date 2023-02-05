import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { Link } from 'react-router-dom';
import LogoText from './LogoText';
import './Navbar.css';

function FestivalmatchNavbar() {
  return (
    <Navbar className='mainnav' expand="lg" variant="dark">
          <Navbar.Brand as={Link} to="/">
              <LogoText />
          </Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
              <Nav.Link className="mainnav-link" as={Link} to="/">Home</Nav.Link>
              <Nav.Link className="mainnav-link" as={Link} to="/how">How it works</Nav.Link>
              <Nav.Link className="mainnav-link" as={Link} to="/contact">Contact</Nav.Link>
          </Navbar.Collapse>
    </Navbar>
  );
}

export default FestivalmatchNavbar;