const boton = document.getElementById('btn');

function colorAleatorio() {
    const hexa = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += hexa[Math.floor(Math.random() * 16)];
    }
    return color;
}

boton.addEventListener('click', () => {
    const nuevoColor = colorAleatorio();
    document.body.style.backgroundColor = nuevoColor;
});