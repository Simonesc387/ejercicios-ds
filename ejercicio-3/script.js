const formulario = document.getElementById('formulario');
const nombre = document.getElementById('nombre');
const correo = document.getElementById('email');
const mensaje = document.getElementById('mensaje');

formulario.addEventListener('submit', (evento) => {
    evento.preventDefault(); 

    if (nombre.value === '' || correo.value === '') {
        mensaje.textContent = 'Error: Los campos no pueden estar vacios.';
        mensaje.className = 'error';
    } else {
        mensaje.textContent = 'Exito: Formulario enviado correctamente.';
        mensaje.className = 'exito';
    }
});