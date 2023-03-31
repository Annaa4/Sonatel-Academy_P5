const leftdiv = document.getElementById("left");
const rightdiv = document.getElementById("right");
const toRightButton = document.getElementById('toRight');
const toLeftButton = document.getElementById('toLeft');
const tableau=["Mon premier","Mon deuxième","Mon troisième","Mon quatrième"];
tableau.forEach(function(a){
    const p =document.createElement("p");
    p.textContent=a;
    leftdiv.appendChild(p);
    p.addEventListener("mouseover", function(){
        p.classList.add("hover");
    })
    p.addEventListener("mouseout", function(){
        p.classList.remove("hover");
    })
    
    p.addEventListener("click",function(){
        p.classList.add("selected");
    })
}); 

toRightButton.addEventListener("click", function(){
     const gauche=leftdiv.querySelector(".selected");
     if(gauche){
        rightdiv.appendChild(gauche);
     }
})
toLeftButton.addEventListener("click", function(){
    const droit=rightdiv.querySelector(".selected");
    if(droit){
       leftdiv.appendChild(droit);
    }
})