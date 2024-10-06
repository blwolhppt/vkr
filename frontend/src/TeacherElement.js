import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

function TeacherElement() {
  const { id } = useParams();
  const [teacher, setTeacher] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/api/teachers/${id}/`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        setTeacher(data);
        setLoading(false);
      })
      .catch(error => {
        setError('Ошибка при получении данных');
        setLoading(false);
      });
  }, [id]);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div>
      <h1>{teacher.first_name}</h1>
      {teacher.photo && (
                <img src={teacher.photo} alt={`${teacher.first_name} ${teacher.last_name}`} style={{ maxWidth: '300px' }} />
            )}
    </div>
  );
}

export default TeacherElement;
