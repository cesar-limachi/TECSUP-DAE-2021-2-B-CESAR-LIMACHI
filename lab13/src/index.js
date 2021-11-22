import 'bootstrap/dist/css/bootstrap.min.css';
import {Nav, Navbar, Container} from 'react-bootstrap';
import React from 'react'
import ReactDOM from 'react-dom'
import { Route, Link, BrowserRouter,Routes} from 'react-router-dom'
import App from './App'
import Users from './users'
import Contact from './contact'
import Notfound  from './notfound'



const routing = (
    <div>
      <BrowserRouter>
        
        
        <Navbar bg="dark" variant="dark">
            <Container>
                <Navbar.Brand> Navbar</Navbar.Brand>
                <Nav className="me-auto">
                    <Link to="/" className="nav-link">Home</Link>
                    <Link to="/usuarios" className="nav-link">Users</Link>
                    <Link to="/contacto" className="nav-link">Contact</Link>
                </Nav>
            </Container>
        </Navbar>




        <Routes>
          <Route exact path="/" element={<App />} />
          <Route path="/usuarios/:id" element={<Users />} />
          <Route path="/contacto" element={<Contact />} />
          <Route path="*" element = {<Notfound />} />
        </Routes>
      </BrowserRouter>
    </div>
  )
  
    
  ReactDOM.render(
    routing,
    document.getElementById('root')
  );
  

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals

