import React, { useState, useEffect } from "react";
import axios from "axios";

const ManagerDashboard = () => {
  const [users, setUsers] = useState([]);
  const [courses, setCourses] = useState([]);
  const [selectedUser, setSelectedUser] = useState(null);
  const [selectedCourse, setSelectedCourse] = useState(null);

  useEffect(() => {
    axios.get("http://localhost:8000/api/manager-dashboard/")
      .then(res => {
        setUsers(res.data.users);
        setCourses(res.data.courses);
      })
      .catch(error => console.error("Error fetching manager data", error));
  }, []);

  return (
    <div style={{ display: "flex" }}>
      <div style={{ width: "30%", padding: "10px", background: "#f4f4f4" }}>
        <h3>Users</h3>
        {users.map(user => (
          <p key={user.id} onClick={() => setSelectedUser(user)}>{user.email}</p>
        ))}
        <h3>Courses</h3>
        {courses.map(course => (
          <p key={course.id} onClick={() => setSelectedCourse(course)}>{course.title}</p>
        ))}
      </div>

      <div style={{ flex: 1, padding: "20px" }}>
        {selectedUser && (
          <div>
            <h2>User: {selectedUser.email}</h2>
            <p>Name: {selectedUser.first_name} {selectedUser.last_name}</p>
            <p>Registered Courses: {selectedUser.courses?.map(c => c.title).join(", ") || "None"}</p>
          </div>
        )}
        {selectedCourse && (
          <div>
            <h2>Course: {selectedCourse.title}</h2>
            <p>Videos:</p>
            <ul>
              {selectedCourse.videos?.map(video => (
                <li key={video.id}>{video.title}</li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  );
};

export default ManagerDashboard;
