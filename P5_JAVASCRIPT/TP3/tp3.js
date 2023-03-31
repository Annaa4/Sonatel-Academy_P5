const vert = document.getElementById("green");
const rouge = document.getElementById("red");
const jaune = document.getElementById("yellow");
const bleu = document.getElementById("blue");
const notification = document.getElementById("notif");

vert.addEventListener("click", function(){
    const p = document.createElement("p");
    p.classList.add("pgreen");
    p.innerHTML="Bravo ! Vous avez réussi.";
    notification.appendChild(p);
    setTimeout(function(){
        notification.removeChild(p);
    },2000)
})
rouge.addEventListener("click",function(){
    const p = document.createElement("p");
    p.classList.add("pred");
    p.innerHTML="Dommage ! Vous avez échoué.";
    notification.appendChild(p);
    setTimeout(function(){
        notification.removeChild(p);
    },2000);
})
yellow.addEventListener("click",function(){
    const p = document.createElement("p");
    p.classList.add("pyellow");
    p.innerHTML="Attention ! Soyez vigilant.";
    notification.appendChild(p);
    setTimeout(function(){
        notification.removeChild(p);
    },2000);
})
blue.addEventListener("click",function(){
    const p = document.createElement("p");
    p.classList.add("pblue");
    p.innerHTML="Information ! Votre attention svp.";
    notification.appendChild(p);
    setTimeout(function(){
        notification.removeChild(p);
    },2000);
})