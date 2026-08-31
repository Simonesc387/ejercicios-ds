import { useState, useEffect } from 'react';

interface Estudiante {
    id: number;
    nombre: string;
}

export default function Estudiantes() {
    const [datos, setDatos] = useState<Estudiante[]>([]);

    useEffect(() => {
        fetch('http://localhost:8000/estudiantes')
            .then(res => res.json())
            .then(data => setDatos(data));
    }, []);

    return (
        <ul>
            {datos.map(e => <li key={e.id}>{e.nombre}</li>)}
        </ul>
    );
}