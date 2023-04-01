const lengthInput = document.getElementById("length");
const uppercaseCheckbox = document.getElementById("uppercase");
const lowercaseCheckbox = document.getElementById("lowercase");
const numbersCheckbox = document.getElementById("numbers");
const specialCheckbox = document.getElementById("special");
const generateButton = document.getElementById("generate");
const passwordInput = document.getElementById("password");

function verification_case_cochee(){
    return uppercaseCheckbox.checked || lowercaseCheckbox.checked || numbersCheckbox.checked || specialCheckbox.checked;
}
function generer_password(){
        let characters = "";
        if (uppercaseCheckbox.checked) characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        if (lowercaseCheckbox.checked) characters += "abcdefghijklmnopqrstuvwxyz";
        if (numbersCheckbox.checked) characters += "0123456789";
        if (specialCheckbox.checked) characters += "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";
        let password = "";
        for (let i = 0; i < lengthInput.value; i++) {
            password += characters.charAt(Math.floor(Math.random() * characters.length));
        }
        return password;
}

    // Fonction qui met à jour l'état du bouton Générer mot de passe
    function updateGenerateButton() {
        generateButton.disabled = !verification_case_cochee();
    }

    // Événements liés aux critères
        uppercaseCheckbox.addEventListener("change", updateGenerateButton);
        lowercaseCheckbox.addEventListener("change", updateGenerateButton);
        numbersCheckbox.addEventListener("change", updateGenerateButton);
        specialCheckbox.addEventListener("change", updateGenerateButton);

        // Événement lié au bouton Générer mot de passe
        generateButton.addEventListener("click", function() {
        passwordInput.value = generer_password();
        });

        // Initialisation de l'état du bouton Générer mot de passe
    // updateGenerateButton();
