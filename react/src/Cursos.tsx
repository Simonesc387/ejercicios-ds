import { useState, useEffect } from 'react';

interface Curso {
    id: number;
    nombre: string;
}

export default function Cursos() {
    const [datos, setDatos] = useState<Curso[]>([]);

    useEffect(() => {
        fetch('http://localhost:8000/cursos')
            .then(res => res.json())
            .then(data => setDatos(data));
    }, []);

    return (
        <ul>
            {datos.map(c => <li key={c.id}>{c.nombre}</li>)}
        </ul>
    );
}