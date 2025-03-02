import React, { useState } from "react";
import axios from "axios";

const Signin = () => {
    const [formData, setFormData] = useState({
        email: "",
        password: "",
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const res = await axios.post("http://127.0.0.1:8000/users/signin/", formData);
            alert("Logged in successfully!");
            localStorage.setItem("token", res.data.access); // Store token
        } catch (error) {
            alert(error.response.data.error || "Login failed.");
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="email" name="email" placeholder="Email" onChange={handleChange} required />
            <input type="password" name="password" placeholder="Password" onChange={handleChange} required />
            <button type="submit">Sign In</button>
        </form>
    );
};

export default Signin;
