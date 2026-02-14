import { useEffect, useState } from "react";
import { api } from "../api/api";

export default function Students() {
  const [students, setStudents] = useState([]);

  useEffect(() => {
    api.get("/students").then(res => {
      setStudents(res.data);
    });
  }, []);

  return (
    <div>
      <h1>Students</h1>
      {students.map(s => (
        <div key={s.id}>
          {s.name} - {s.department}
        </div>
      ))}
    </div>
  );
}
