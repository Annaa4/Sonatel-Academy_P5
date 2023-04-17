const aside = document.getElementById("aside");
const section = document.getElementById("section");
const container = document.getElementById("container");
const enseignant=document.getElementById("enseignant");
const salle = document.getElementById("salle");
const classe = document.getElementById("classe");
const module = document.getElementById("module");
const toogle = document.querySelector("#checkbox");
const btn = document.querySelectorAll(".btn");
const select = document.getElementById("select");
const lundi = document.getElementById("el1");
const mardi = document.getElementById("el2");
const mercredi = document.getElementById("el3");
const jeudi = document.getElementById("el4");
const vendredi = document.getElementById("el5");
const samedi = document.getElementById("el6");

// creation d'une liste de dictionnaire pour les enseignants, classes, salles et modules 
const teacher=[
   { nom:'Enseignants', id:'0'},
   { nom:'Aly', id:'1'},
   { nom:'Baila', id:'2'},
   { nom:'Ndoye', id:'3'},
   { nom:'Mbaye', id:'4'},
   { nom:'Djily', id:'5'},
   { nom: 'Seckouba', id:'6'}
]
const classes=[
    { nom:'Classes', id:'10'},
    { nom:'L2 GLRS A', id:'11',eff:'30'},
    { nom:'L2 GLRS B', id:'12',eff:'25'},
    { nom:'L2 ETSE', id:'13',eff:'40'},
    { nom:'L1 A', id:'14',eff:'25'},
    { nom:'IAGE B', id:'15',eff:'45'},
    { nom:'L2 CDSD', id:'16',eff:'50'}
]
const salles=[
    { nom:'Salles',id:'20'},
    { nom:'101',id:'21',qte:'40'},
    { nom:'102',id:'22',qte:'45'},
    { nom:'103',id:'23',qte:'30'},
    { nom:'104',id:'24',qte:'50'},
    { nom:'201',id:'25',qte:'25'},
    { nom:'incub',id:'26',qte:'50'}
    
]
const modules=[
    { nom:'Modules', id:'30'},
    { nom:'ALGO', id:'31'},
    { nom:'PHP', id:'32'},
    { nom:'PYTHON', id:'33'},
    { nom:'LC', id:'34'},
    { nom:'JAVASCRIPT', id:'35'},
    { nom:'JAVA', id:'36'}
]

// fonction qui va permettre de changer les couleurs lorsqu'on clique sur le toogle
function change_toogle(){
    toogle.addEventListener("change",()=>{
        if(toogle.checked){
            section.style.backgroundColor="pink";
            container.style.backgroundColor="rgb(101, 97, 97)";
        }
        else{
            section.style.backgroundColor="black"
            container.style.backgroundColor="rgb(54, 54, 54)"
        }
    });
}
change_toogle()
// fonction qui va ajouter chaque liste dans le bloc select si on clique sur les != boutons
function liste(tab){
    select.innerHTML=""
    tab.forEach(element =>{
        const option = document.createElement("option")
        option.setAttribute("value",element.id)
        option.text=element.nom
        select.appendChild(option)
    })
}
// fonction de gestion des boutons
function buttonEven(){
    btn.forEach(element => {
    element.addEventListener("click",(event)=>{
        const identifiant= event.target.getAttribute("id")
        if (identifiant === "enseignant"){
            enseignant.style.backgroundColor='#229DEC';
            salle.style.backgroundColor='rgb(212, 202, 202)';
            module.style.backgroundColor='rgb(212, 202, 202)';
            classe.style.backgroundColor='rgb(212, 202, 202)'
            liste(teacher)
        }
        if (identifiant === "salle"){
            salle.style.backgroundColor='green';
            enseignant.style.backgroundColor='rgb(212, 202, 202)';
            classe.style.backgroundColor='rgb(212, 202, 202)';
            module.style.backgroundColor='rgb(212, 202, 202)';
            liste(salles)
        }
        if (identifiant === "classe"){
            classe.style.backgroundColor='orange';
            enseignant.style.backgroundColor='rgb(212, 202, 202)';
            salle.style.backgroundColor='rgb(212, 202, 202)';
            module.style.backgroundColor='rgb(212, 202, 202)';
            liste(classes)
        }
        if (identifiant === "module"){
            module.style.backgroundColor='red';
            enseignant.style.backgroundColor='rgb(212, 202, 202)';
            salle.style.backgroundColor='rgb(212, 202, 202)';
            classe.style.backgroundColor='rgb(212, 202, 202)';
            liste(modules)
        }    }) 
});
}
buttonEven()

 const jours =[lundi,mardi,mercredi,jeudi,vendredi,samedi]

 const planning=[
    { enseignant:'1',matiere:'33',salle:'25' ,classe:'16',heureDebut:'9',heureFin:'12' ,jour:'1'},
    { enseignant:'2',matiere:'32',salle:'22',classe:'12' ,heureDebut:'14',heureFin:'17',jour:'4'},
    { enseignant:'1',matiere:'35',salle:'22',classe:'12' ,heureDebut:'16',heureFin:'17',jour:'2'},
    { enseignant:'4',matiere:'31',salle:'26',classe:'11' ,heureDebut:'10',heureFin:'12',jour:'4'}
]

// function myFind(id){
//     let e=[]
//     planning.forEach(element => {
//         if(element.enseignant == id){
//             e= element
//             return true
//         }
//     });
//     return e
// }
// function myFilter(id){
//     let e=[]
//     i=0
//     planning.forEach(element => {
//         if(element.enseignant == id){
//             e[i]= element
//             i++
            
//         }
//     });
//     return e
// }
function planningEnseignants(idProf){
    const planningEnseign = planning.filter(nomProf => nomProf.enseignant === idProf)
    console.log(planningEnseign);
    planningEnseign.forEach(element => {
        const Module = modules.find(nomModule => nomModule.id === element.matiere).nom;
        const Classe = classes.find(nomClasse => nomClasse.id === element.classe).nom;
        const Salle = salles.find(nomSalle => nomSalle.id === element.salle).nom;
        const heureDebut = element.heureDebut;
        const heureFin = element.heureFin;
        const jour = element.jour;
        const duree = heureFin - heureDebut;
       
        jours.forEach(eljour =>{
            if(eljour === jours[jour - 1]){
            
                let H = document.createElement("div")
                H.innerHTML="";
                H.innerHTML += `<p>${Classe}<br>${Module}<br>${Salle}</p>`;
                // H.innerHTML += `<p></p>`;
                // H.innerHTML += `<p></p>`;
                eljour.appendChild(H)
                H.style.marginLeft=`${(heureDebut - 8)*10.5}%`
                H.style.width=`${(duree)*11.5}%`
                H.style.height = "80px"
                H.style.backgroundColor='red' 
                H.style.borderRadius='10px'
                H.style.display  = "flex"
                H.style.justifyContent = "center"
                H.style.textAlign="center"
        
        }
        })
    });

}


// Planning classes
function planningClasses(idClasse){
    const planningClasse = planning.filter(nomClasse => nomClasse.classe === idClasse)
    planningClasse.forEach(element => {
        const Module = modules.find(nomModule => nomModule.id === element.matiere).nom;
        const Enseignant = teacher.find(nomEnseign => nomEnseign.id === element.enseignant).nom;
        const Salle = salles.find(nomSalle => nomSalle.id === element.salle).nom;
        const heureDebut = element.heureDebut;
        const heureFin = element.heureFin;
        const jour = element.jour;
        const duree = heureFin - heureDebut;
       
        jours.forEach(eljour =>{
            if(eljour === jours[jour - 1]){
            
                let H = document.createElement("div")
                H.innerHTML="";
                H.innerHTML += `<p>${Enseignant}<br>${Module}<br>${Salle}</p>`;
                eljour.appendChild(H)
                H.style.marginLeft=`${(heureDebut - 8)*10.5}%`
                H.style.width=`${(duree)*11.5}%`
                H.style.height = "80px"
                H.style.backgroundColor='green' 
                H.style.borderRadius='10px'
                H.style.display  = "flex"
                H.style.justifyContent = "center"
                H.style.textAlign="center"
        
        }
        })
    });

}

select.addEventListener("change",(event)=>{
    const valeur = event.target.value
    jours.forEach(eljour =>{
        eljour.innerHTML = ""
    })
    if(classes.find(nomvaleur => nomvaleur.id === valeur)){
    planningClasses(valeur)
    const nomvaleur = classes.find(nomvaleur => nomvaleur.id === valeur).nom;
    document.getElementById("titreplanning").textContent='Planning :' + ' ' + nomvaleur
       afficheFormulaire()
    }
    if (teacher.find(nomvaleur => nomvaleur.id === valeur)){
        planningEnseignants(valeur)
        const nomvaleur = teacher.find(nomvaleur => nomvaleur.id === valeur).nom;
        document.getElementById("titreplanning").textContent='Planning :' + ' ' + nomvaleur
        afficheFormulaire()
    }
    if (salles.find(nomvaleur => nomvaleur.id === valeur)){
        planningEnseignants(valeur)
        const nomvaleur = teacher.find(nomvaleur => nomvaleur.id === valeur).nom;
        document.getElementById("titreplanning").textContent='Planning :' + ' ' + nomvaleur
        afficheFormulaire()
    }
    if (modules.find(nomvaleur => nomvaleur.id === valeur)){
        planningEnseignants(valeur)
        const nomvaleur = teacher.find(nomvaleur => nomvaleur.id === valeur).nom;
        document.getElementById("titreplanning").textContent='Planning :' + ' ' + nomvaleur
        afficheFormulaire()
    }
})

// Evenement liés au formulaire

const formulaire = document.getElementById("formulaire")
const btnAnnuler = document.getElementById("annuler")
const btnLundi = document.getElementById("lundi");
const btnMardi = document.getElementById("mardi")
const btnMercredi = document.getElementById("mercredi")
const btnJeudi = document.getElementById("jeudi")
const btnVendredi = document.getElementById("vendredi")
const btnSamedi = document.getElementById("samedi")
function afficheFormulaire(){ 
    btnLundi.addEventListener("click",()=>{
         formulaire.style.display="block"
    })
    btnMardi.addEventListener("click",()=>{
        formulaire.style.display="block"
   })
    btnMercredi.addEventListener("click",()=>{
    formulaire.style.display="block"
   })
    btnJeudi.addEventListener("click",()=>{
        formulaire.style.display="block"
   })
    btnVendredi.addEventListener("click",()=>{
        formulaire.style.display="block"
   })
    btnSamedi.addEventListener("click",()=>{
        formulaire.style.display="block"
})
    btnAnnuler.addEventListener("click",()=>{
        formulaire.style.display="none"
    })
    
}
