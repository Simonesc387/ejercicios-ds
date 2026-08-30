const inputTarea = document.getElementById('input-tarea');
const btnAgregar = document.getElementById('btn-agregar');
const listaTareas = document.getElementById('lista-tareas');

btnAgregar.addEventListener('click', () => {
    const nuevaTarea = document.createElement('li');
    nuevaTarea.textContent = inputTarea.value;

    nuevaTarea.addEventListener('click', () => {
        nuevaTarea.remove();
    });

    listaTareas.appendChild(nuevaTarea);
    inputTarea.value = '';
});