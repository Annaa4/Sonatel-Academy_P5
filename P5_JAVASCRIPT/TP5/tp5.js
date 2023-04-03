const general = document.getElementById("general");
const rejouer = document.getElementById("replay")
var questions=[
    {
        Question : "Quel est le meilleur language de programmation en 2022 ?",
        a: "Java",
        b: "C",
        c: "Python",
        d: "JavaScript",
        correct: "d"
    },
    {
        Question : "Quelle option n'est pas un langage de programmation ?",
        a: "Java",
        b: "Catcode",
        c: "Python",
        d: "JavaScript",
        correct: "b"
    },
    {
        Question : "Quel est le nom du système d'exploitation mis au point par Google ?",
        a: "Chrome",
        b: "Chrome OS",
        c: "Chrobuntu",
        correct: "b"
    },
    {
        Question : "Linux, ou GNU/Linux, est un système d'exploitation compatible POSIX. Linux est basé sur le noyau Unix. Mais en quelle année a-t-il été créé ?", 
        a: "1991",
        b: "1995",
        c: "1990",
        correct: "a"
    },
    {
        Question: "Quel est le langage de programmation le plus utilisé pour les applications mobiles ?",
        a: "Java",
        b: "C",
        c: "Swift",
        d: "Kotlin",
        correct: "c"
  },]
  var currentQuestion = 0;
  var score = 0;
  
  function loadQuestion() {
    rejouer.style.display='none'
      var q = questions[currentQuestion];
      document.getElementById("questions").textContent = q.Question;
      document.getElementById("a").textContent = q.a;
      document.getElementById("b").textContent = q.b;
      document.getElementById("c").textContent = q.c;
      document.getElementById("d").textContent = q.d;
  }
  
  function checkAnswer() {
      var answer = document.querySelector("input[name='answer']:checked").value;
      if (answer === questions[currentQuestion].correct) {
          score++;
      }
  }
  
  function showNextQuestion() {
      checkAnswer();
      currentQuestion++;
      if (currentQuestion < questions.length) {
          loadQuestion();
      } else {
          var quiz = document.getElementById("quiz");
          quiz.innerHTML = "<h2>Vous avez trouvé : " + score + " / " + questions.length + " questions </h2>";
          rejouer.style.display='block'
      }
  }
  
  loadQuestion();
  
  document.getElementById("suivant").addEventListener("click", showNextQuestion);