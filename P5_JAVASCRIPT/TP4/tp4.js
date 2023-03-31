      const uppercaseLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
      const lowercaseLetters = 'abcdefghijklmnopqrstuvwxyz';
      const numbers = '0123456789';
      const specialCharacters = '!@#$%^&*()_+~`|}{[]\:;?><,./-=';

      function generatePassword() {
        let password = '';
        const length = document.getElementById('length').value;
        const uppercaseChecked = document.getElementById('uppercase').checked;
        const lowercaseChecked = document.getElementById('lowercase').checked;
        const numbersChecked = document.getElementById('numbers').checked;
        const specialChecked = document.getElementById('special').checked;

        const possibleChars = (uppercaseChecked ? uppercaseLetters : '') +
                              (lowercaseChecked ? lowercaseLetters : '') +
                              (numbersChecked ? numbers : '') +
                              (specialChecked ? specialCharacters : '');

        if (possibleChars === '') {
          alert('Veuillez cocher au moins un critère pour générer un mot de passe.');
          return;
        }

        for (let i = 0; i < length; i++) {
          password += possibleChars.charAt(Math.floor(Math.random() * possibleChars.length));
        }

        document.getElementById('password').value = password;
      }

      document.getElementById('generate').addEventListener('click', generatePassword);

      document.getElementById('password').addEventListener('mouseover', function() {
        const tooltip = document.getElementById('tooltip');
        tooltip.style.display = 'inline-block';
        tooltip.style.top = (this.offsetTop - 25) + 'px';
        tooltip.style.left = (this.offsetLeft + this.offsetWidth / 2 - tooltip.offsetWidth / 2) + 'px';

        const range = document.createRange();
        range.selectNodeContents(this);
        const selection = window.getSelection();
        selection.removeAllRanges();
        selection.addRange(range);
      });

      document.getElementById('password').addEventListener('mouseout', function() {
        const tooltip = document.getElementById('tooltip');
        tooltip.style.display = 'none';

        const selection = window.getSelection();
        selection
      }



