import React, { useState, useEffect } from 'react';

function Teachers() {
  const [teachers, setTeachers] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/teachers/')
      .then(response => response.json())
      .then(data => {
        setTeachers(data);
      })
      .catch(error => {
        console.error('Ошибка при получении данных:', error);
      });
  }, []);

  return (
    <div>
      <h1>Teachers</h1>
      <ul>
        {teachers.map(teacher => (
          <li key={teacher.id}>{teacher.last_name} {teacher.first_name} {teacher.second_name} {teacher.photo && (
                <img src={teacher.photo} alt={`${teacher.first_name} ${teacher.last_name}`} style={{ maxWidth: '300px' }} />
            )}</li>

        ))}
      </ul>
    </div>
  );
}
export default Teachers;
