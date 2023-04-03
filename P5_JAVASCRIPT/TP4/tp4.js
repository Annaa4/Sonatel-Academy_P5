const lengthInput = document.getElementById("length");
const uppercase = document.getElementById("uppercase");
const lowercase = document.getElementById("lowercase");
const nombres = document.getElementById("numbers");
const special = document.getElementById("special");
const generateButton = document.getElementById("generate");
const passwordInput = document.getElementById("password");

const majuscules = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
const miniscules = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
const numbers = "0,1,2,3,4,5,6,7,8,9"
const speciaux= "%,*,;,/,§,!,?,\,µ,[,],/,#,~,&"

function generate_password(){
    let password ="";
    let a ="";
    if(uppercase.checked){
        a+=majuscules
    }
    if(lowercase.checked){
        a+=miniscules
    }
    if(nombres.checked){
        a+=numbers
    }
    if(special.checked){
        a+=speciaux
    }
    for (let i=0;i < lengthInput.value;i++){
        var c = Math.floor(Math.random()*a.length)
        password+=a[c]
    }
   passwordInput.value=password
}
function bouton(){
    if (uppercase.checked || lowercase.checked || nombres.checked || special.checked){
        generateButton.disabled = false
    }
    else{
        generateButton.disabled = true
    }
}
uppercase.addEventListener("change", bouton);
lowercase.addEventListener("change", bouton);
nombres.addEventListener("change", bouton);
special.addEventListener("change", bouton);
 
generateButton.addEventListener("click",generate_password)