import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

function Video_test() {
  const [videos, setVideos] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/videomaterials/')
      .then(response => response.json())
      .then(data => {
        setVideos(data);
      })
      .catch(error => {
        console.error('Ошибка при получении данных:', error);
      });
  }, []);

  return (
    <div>
      <h1>Teachers</h1>
      <ul>
        {videos.map(video => (
          <li key={video.id}> {video.video_name}
              {video.video_file && (
                <video width="320" height="240" controls>
                    <source src={video.video_file} type="video/mp4" />
                    Ваш браузер не поддерживает воспроизведение видео.
                </video>
            )}

          </li>

        ))}
      </ul>
    </div>
  );
}

export default Video_test;
