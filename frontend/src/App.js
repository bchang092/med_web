import React, { useState, useEffect } from 'react';
import axios from 'axios';

function VolunteerPage() {
    const [reviews, setReviews] = useState([]);
    const [formData, setFormData] = useState({
        Review_Content: '',
        Department: '',
        Rating: ''
    });

    // Fetch reviews on load
    useEffect(() => {
        axios.get('http://127.0.0.1:8000/reviews/volunteer_page/')  // Backend API URL
            .then(response => setReviews(response.data))
            .catch(error => console.error(error));
    }, []);

    // Handle form input changes
    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    // Handle form submission
    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('/api/reviews/', formData, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${localStorage.getItem('token')}` // Replace with your auth token
            }
        })
        .then(response => {
            setReviews([response.data, ...reviews]); // Add new review to the list
            setFormData({ Review_Content: '', Department: '', Rating: '' }); // Clear form
        })
        .catch(error => console.error(error));
    };

    return (
        <div>
            <h1>Volunteer Reviews</h1>
            <form onSubmit={handleSubmit}>
                <textarea name="Review_Content" value={formData.Review_Content} onChange={handleChange} required />
                <input type="text" name="Department" value={formData.Department} onChange={handleChange} required />
                <input type="number" name="Rating" value={formData.Rating} onChange={handleChange} required />
                <button type="submit">Submit</button>
            </form>
            <h2>Submitted Reviews:</h2>
            <ul>
                {reviews.map((review) => (
                    <li key={review.id}>
                        {review.Review_Content} - {review.Rating}/10 ({review.Sentiment})
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default VolunteerPage;
