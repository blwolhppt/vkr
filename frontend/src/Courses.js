// // import React, { useState, useEffect } from 'react';

// // function Courses() {
// //   const [courses, setCourses] = useState([]);

// //   useEffect(() => {
// //     fetch('http://127.0.0.1:8000/api/courses/')
// //       .then(response => response.json())
// //       .then(data => {
// //         setCourses(data);
// //       })
// //       .catch(error => {
// //         console.error('Ошибка при получении данных:', error);
// //       });
// //   }, []);

// //   return (
// //     <div>
// //       <h1>Cources</h1>
// //       <ul>
// //         {courses.map(course => (
// //           <li key={course.id}>{course.course_name} {course.duration} месяцев {course.price} рублей
// //           {course.description} {course.for_who} {course.categories}
          
// //           </li>

// //         ))}
// //       </ul>
// //     </div>
// //   );
// // }
// // export default Courses;

// // Courses.js
// import React from 'react';
// import './courses.css';
// import CourseCard from './CourseCard';

// const coursesData = [
//     { id: 1, name: 'C++', level: 'beginners', duration: '4 years', price: 'free' },
//     { id: 2, name: 'Python', level: 'experience', duration: '3 months', price: '500$' },
//     { id: 3, name: 'Biology for young', level: 'experience', duration: '3 months', price: '500$' },
// ];

// const Courses = () => {
//     return (
//         <div className="courses-container">
//             <div className="search-section">
//                 <h2>It is never too late to learn.</h2>
//                 <input type="text" placeholder="Something with IT and Biology, including IT-development" />
//             </div>
//             <div className="category-buttons">
//                 <button>Biology</button>
//                 <button>IT</button>
//                 <button>Marketing</button>
//                 <button>Literature</button>
//                 <button>Languages</button>
//                 <button>Design</button>
//             </div>
//             <div className="courses-list">
//                 {coursesData.map((course) => (
//                     <div key={course.id} className="course-card">
//                         <h3>{course.name}</h3>
//                         <p>for: <span>{course.level}</span></p>
//                         <p>duration: <span>{course.duration}</span></p>
//                         <p>price: <span>{course.price}</span></p>
//                         <button className="add-button">+</button>
//                     </div>
//                 ))}
//             </div>
//         </div>
//     );
// };

// export default Courses;

import React from "react";
import "./courses.css"; // Import a CSS file for detailed styling if needed

const courses = [
  { title: "C++", for: "beginners", duration: "4 years", price: "free" },
  { title: "Python", for: "experience", duration: "3 months", price: "500$" },
  { title: "Biology for young", for: "experience", duration: "3 months", price: "500$" },
];

const Courses = () => {
  return (
    <div className="courses-container">
      <header className="header">
        <h1>Educational Hub</h1>
        <p>It is never too late to learn.</p>
      </header>
      <div className="search-bar">
        <input type="text" placeholder="What do you want to find?" />
      </div>
      <div className="categories">
        {["Biology", "IT", "Marketing", "Literature", "Languages", "Design"].map((category) => (
          <button key={category} className="category-button">
            {category}
          </button>
        ))}
      </div>
      <div className="course-cards">
        {courses.map((course, index) => (
          <div key={index} className="course-card">
            <h2>{course.title}</h2>
            <p><strong>For:</strong> {course.for}</p>
            <p><strong>Duration:</strong> {course.duration}</p>
            <p><strong>Price:</strong> {course.price}</p>
            <div className="controls">
              <div className="triangle-button" />
              <div className="circle-button" />
              <div className="plus-button">+</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Courses;
