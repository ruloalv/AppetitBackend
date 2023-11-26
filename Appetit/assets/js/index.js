document.getElementById("btn_menu").addEventListener("click", function(){
	var lista = document.getElementById("lista_menu");
	if(lista.classList.contains('oculto')){
		lista.classList.remove('oculto');
		lista.classList.add('visible');
	}else{
		lista.classList.add('oculto');
		lista.classList.remove('visible');
	}
})
