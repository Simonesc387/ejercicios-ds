import { useState, useEffect } from 'react';

interface Profesor {
    id: number;
    nombre: string;
}

export default function Profesores() {
    const [datos, setDatos] = useState<Profesor[]>([]);

    useEffect(() => {
        fetch('http://localhost:8000/profesores')
            .then(res => res.json())
            .then(data => setDatos(data));
    }, []);

    return (
        <ul>
            {datos.map(p => <li key={p.id}>{p.nombre}</li>)}
        </ul>
    );
}