  // Déclaration de deux constantes qui recupére les classes crées dans le fichier html en utilisant document.getElementById
  const btn = document.getElementById("btn");
  const container = document.getElementById("container")
  
  // création di'une fonction javascript 
  function creerdiv(){
  
      // creation d'une section qui va contenir les icones edit et corbeille
      const section=document.createElement("section");
      // creation d'une classe section
      section.classList.add("section");
        // Ajout des icones au niveau de la section 
      const trash = document.createElement("trash");
      trash.classList.add("bx", "bxs-trash");
      section.appendChild(trash);
      const edit = document.createElement("edit");
      edit.classList.add("bx", "bxs-edit");
      section.appendChild(edit);

      const textarea=document.createElement("textarea");
      textarea.classList.add("textarea");
      //  Ajout du textarea au niveau de la section
      section.appendChild(textarea)
      // Ajout de la section dans un div général
      container.appendChild(section);
      // AJout d'un evenement pour la suppression
      trash.addEventListener("click", () => section.remove());
      // AJout d'un evenement pour l'activation/desactivation du textarea
      edit.addEventListener("click", () => {
      textarea.disabled= ! textarea.disabled;
    })
  }
// Activation du bouton +Add New
  btn.addEventListener("click", creerdiv);
  
  
  
  
  