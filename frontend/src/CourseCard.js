// CourseCard.js
import React from 'react';
import './courseCard.css';

const CourseCard = ({ name, level, duration, price }) => {
    return (
        <div className="course-card">
            <h3>{name}</h3>
            <div className="course-info">
                <p>for: <span>{level}</span></p>
                <p>duration: <span>{duration}</span></p>
                <p>price: <span>{price}</span></p>
            </div>
            <div className="decorative-elements">
                <div className="circle pink"></div>
                <div className="circle green"></div>
                <div className="circle blue"></div>
                <button className="add-button">+</button>
            </div>
        </div>
    );
};

export default CourseCard;
