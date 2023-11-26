//import { response } from "./general.js";

// validación de datos que se ingresan en los input
let element = document.querySelectorAll('input');

// let emailPattern = /^(([^<>()\[\]\.,;:\s@"]+(\.[^<>()\[\]\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
// let emailPattern = /^((?!\.)[\w\-_.]*[^.])(@\w+)(\.\w+(\.\w+)?[^.\W])$/

element.forEach(i => {
    i.addEventListener('blur', (e) => {
        
        if (e.target.validity.valueMissing) {
            console.log("entro por "+ e.target.name + " y vacio " + e.target.validity.valueMissing)
            e.target.setCustomValidity('Por favor complete el campo');
        }
        if (e.target.validity.patternMismatch) {
            console.log("entro por "+ e.target.name + " y pattern " + e.target.validity.patternMismatch)
            if (e.target.name == "name"){
                e.target.setCustomValidity('Por favor ingrese un nombre válido sin caracteres especiales');
            }
            if (e.target.name == "surname"){
                e.target.setCustomValidity('Por favor ingrese un apellido válido sin caracteres especiales');
            }
            if (e.target.name == "email"){
                e.target.setCustomValidity('Por favor ingrese un e-mail válido');
            }
        }
    })
    i.addEventListener('change', (e) => {
        e.target.setCustomValidity('');
    })
});
