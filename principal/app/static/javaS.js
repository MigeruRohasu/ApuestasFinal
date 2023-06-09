
function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

const formlogin = document.getElementById('formulariologin');

formlogin.addEventListener('botonlogin', (e) => {

  const username = document.querySelector('#username').value.trim();
  const password = document.querySelector('#password').value.trim();

  if (username === '') {
    alert('Please enter your username');
    return;
  }

  if (password === '') {
    alert('Please enter your password');
    return;
  }
  // Si los campos son válidos, enviar el formulario
  formlogin.submit();
});


const formBilletera = document.getElementById('formulariologin');

formBilletera.addEventListener('botonlogin', (e) => {

  const username = document.querySelector('#username').value.trim();
  const password = document.querySelector('#password').value.trim();

  if (username === '') {
    alert('Please enter your username');
    return;
  }

  if (password === '') {
    alert('Please enter your password');
    return;
  }
  // Si los campos son válidos, enviar el formulario
  formBilletera.submit();
});


// Obtener referencias a los elementos del DOM
const backBtn = document.getElementById('back-btn');

// Agregar un evento de clic al botón de back
backBtn.addEventListener('click', (event) => {
  event.preventDefault(); // Prevenir el comportamiento por defecto del botón
  window.location.href = 'home'; // Redirigir a la página de inicio
});

const crearBtn = document.getElementById('crear-btn');

// Agregar un evento de clic al botón de back
crearBtn.addEventListener('click', (event) => {
  event.preventDefault(); // Prevenir el comportamiento por defecto del botón
  window.location.href = 'crear_cuenta'; // Redirigir a la página de inicio
});
