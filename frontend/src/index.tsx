import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Home from './pages/home/Home';
import How from './pages/how/How';
import Privacy from './pages/privacy/Privacy';
import Contact from './pages/contact/Contact';
import Suggestions from './pages/suggestions/Suggestions';
import Shared from './pages/shared/Shared';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';


export default function FestivalMatch() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />}></Route>
        <Route path="/how" element={<How />}></Route>
        <Route path="/privacy" element={<Privacy />}></Route>
        <Route path="/contact" element={<Contact />}></Route>
        <Route path="/suggestions" element={<Suggestions />}></Route>
        <Route path="shared" element={<Shared />}></Route>
      </Routes>
    </BrowserRouter>
  );
}

// @ts-ignore
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<FestivalMatch />);
