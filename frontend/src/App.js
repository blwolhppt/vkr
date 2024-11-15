import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Teachers from './Teachers';
import TeacherElement from './TeacherElement';
import Video_test from './Video_test';
import Courses from './Courses';


function App() {
  return (
    <Router>
      <div>
        {/*<nav>*/}
        {/*  <ul>*/}
        {/*    <li>*/}
        {/*      <Link to="/teachers">Teachers</Link>*/}
        {/*    </li>*/}
        {/*  </ul>*/}
        {/*</nav>*/}

        <Routes>
          <Route path="/teachers" element={<Teachers />} />
          <Route path="/teachers/:id" element={<TeacherElement />} />
          <Route path="/courses" element={<Courses />} />
          <Route path="/video_test" element={<Video_test />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
