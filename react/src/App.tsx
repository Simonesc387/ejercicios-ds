import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Estudiantes from './Estudiantes';
import Profesores from './Profesores';
import Cursos from './Cursos';
import './index.css';

export default function App() {
    return (
        <BrowserRouter>
            <nav>
                <Link to="/estudiantes">Estudiantes</Link> | {" "}
                <Link to="/profesores">Profesores</Link> | {" "}
                <Link to="/cursos">Cursos</Link>
            </nav>

            <Routes>
                <Route path="/estudiantes" element={<Estudiantes />} />
                <Route path="/profesores" element={<Profesores />} />
                <Route path="/cursos" element={<Cursos />} />
            </Routes>
        </BrowserRouter>
    );
}