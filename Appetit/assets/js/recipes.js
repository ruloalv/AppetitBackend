const TOKEN = "nakzp5ez45x64zd4g9hseopk9picabjeonepyabf";
const URL = "https://sheetdb.io/api/v1/dqu2afl50gp3l";

const renderRecipes = (data) => {
    let breakfast = 0;
    let lunch = 0;
    let dessert = 0;
    
    let grupoBreakfast = document.createElement("section");
    grupoBreakfast.classList.add("contenedor_de_enlaces_01");
    let titulob = document.createElement("h2");
    titulob.innerText = "Breakfast";
    let linkb = document.createElement("a");
    linkb.href = "./breakfast.html";
    linkb.appendChild(titulob);
    let divb = document.createElement("div");
    divb.appendChild(linkb);
    divb.classList.add("enlaces_a_secciones");

    let grupoLunch = document.createElement("section");
    grupoLunch.classList.add("contenedor_de_enlaces_01");
    let titulol = document.createElement("h2");
    titulol.innerText = "Lunch";
    let linkl = document.createElement("a");
    linkl.href = "./lunch.html";
    linkl.appendChild(titulol);
    let divl = document.createElement("div");
    divl.appendChild(linkl);
    divl.classList.add("enlaces_a_secciones");

    let grupoDessert = document.createElement("section");
    grupoDessert.classList.add("contenedor_de_enlaces_01");
    let titulod = document.createElement("h2");
    titulod.innerText = "Dessert";
    let linkd = document.createElement("a");
    linkd.href = "./dessert.html";
    linkd.appendChild(titulod);
    let divd = document.createElement("div");
    divd.appendChild(linkd);
    divd.classList.add("enlaces_a_secciones");
    
    for (let i = 0; i < data.length; i++) {
        let receta = document.createElement("div");
        receta.classList.add("enlace_a_receta");
        let enlace = document.createElement("a");
        enlace.href = data[i].link;
        let imagen = document.createElement("img");
        imagen.classList.add("imagen_del_enlace");
        imagen.src = data[i].imgSmall;
        imagen.alt = data[i].name;
        let texto = document.createElement("p");
        texto.innerText = data[i].name;

        enlace.appendChild(imagen);
        enlace.appendChild(texto);
        receta.appendChild(enlace);

        if (data[i].type === "Breakfast" && breakfast<3){
            grupoBreakfast.appendChild(receta);
            breakfast += 1;
        }
        if (data[i].type === "Lunch" && lunch<3){
            grupoLunch.appendChild(receta);
            lunch += 1;
        }
        if (data[i].type === "Dessert" && dessert<3){
            grupoDessert.appendChild(receta);
            dessert += 1;
        }
        if (breakfast === lunch === dessert === 3){
            break; 
        }
    }
    let contenedor = document.getElementById("main");
    contenedor.appendChild(divb);
    contenedor.appendChild(grupoBreakfast);
    contenedor.appendChild(divl);
    contenedor.appendChild(grupoLunch);
    contenedor.appendChild(divd);
    contenedor.appendChild(grupoDessert);

    // console.log(contenedor);
}

fetch(URL, {
method: "GET",
headers: {Authorization: `Bearer ${TOKEN}`},
})
.then(res => res.json())
// .then(data => {console.log(data[1].imgSmall)})
.then(data => renderRecipes(data))
.catch((error) => {
    error;
    console.log(error)
})