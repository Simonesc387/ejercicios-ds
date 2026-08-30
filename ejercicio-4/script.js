const numero = document.getElementById('numero');
const btnMenos = document.getElementById('btn-menos');
const btnMas = document.getElementById('btn-mas');

let contador = 0;

btnMas.addEventListener('click', () => {
    contador++;
    numero.textContent = contador;
});

btnMenos.addEventListener('click', () => {
    contador--;
    numero.textContent = contador;
});