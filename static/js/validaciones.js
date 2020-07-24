"use strict";

var boton = document.querySelector("#boton");
boton.addEventListener("click", () => {
  console.log("HolaMundo");
});
boton.disabled = true;

// CEDULA
var cedula = document.querySelector("#cedula");
var error_cedula = document.querySelector("#error_cedula");
var mensaje_error_cedula = document.querySelector("#mensaje_error_cedula");
error_cedula.parentElement.style.display = "none";

// CONTRASEÑA
var password = document.querySelector("#password");
var error_password = document.querySelector("#error_password");
var mensaje_error_password = document.querySelector("#mensaje_error_password");
error_password.parentElement.style.display = "none";

// USUARIO NO ENCONTRADO
var usuario_no_econtrado = document.querySelector("#usuario_no_encontrado");
usuario_no_econtrado.parentElement.style.display = "none";

// booleanos
var mostrar = true;
var mostrar_1 = true;

cedula.addEventListener("blur", () => {
  let name = cedula.value;
  let mensaje = "";
  mostrar = false;

  if (isNaN(name)) {
    mensaje = "La cédula debe ser un número";
    mostrar = true;
  } else {
    mostrar = false;
  }
  if (!mostrar) {
    if (name.length > 10 || name.length < 10) {
      mensaje = "El cédula debe tener 10 números";
      mostrar = true;
    } else {
      mostrar = false;
    }
  }

  if (mostrar) {
    mensaje_error_cedula.innerHTML = mensaje;
    error_cedula.parentElement.style.display = "";
    boton.disabled = true;
  } else {
    error_cedula.parentElement.style.display = "none";
    if (mostrar_1 == false && mostrar == false) {
      boton.disabled = false;
    }
  }
});

password.addEventListener("blur", () => {
  let contrasenia = password.value;
  let mensaje = "";
  mostrar_1 = false;

  if (contrasenia === "") {
    mensaje = "El campo contraseña está vació";
    mostrar_1 = true;
  } else {
    mostrar_1 = false;
  }
  if (mostrar_1) {
    mensaje_error_password.innerHTML = mensaje;
    error_password.parentElement.style.display = "";
    boton.disabled = true;
  } else {
    error_password.parentElement.style.display = "none";
    if (mostrar_1 == false && mostrar == false) {
      boton.disabled = false;
    }
  }
});

function usuario_no_econtrado_mostrar(mensaje) {
  if (mensaje === "Con_error") {
    usuario_no_econtrado.parentElement.style.display = "";
  }
}
