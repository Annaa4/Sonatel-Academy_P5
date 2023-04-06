const APIURL = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=04c35731a5ee918f014970082a0088b1&page=1";
const IMGPATH = "https://image.tmdb.org/t/p/w1280";
const SEARCHAPI ="https://api.themoviedb.org/3/search/movie?&api_key=04c35731a5ee918f014970082a0088b1&query=";
const movie_container = document.getElementById("movie_container");
const searchInput = document.getElementById("search"); 

function affimovie(){
    fetch(APIURL)
    .then(reponse => reponse.json())
    .then(data =>{
        data.results.forEach(movie => {
            const movielemnt=document.createElement("div");
            movielemnt.classList.add("movie");

            const movieAffiche = document.createElement("img");
            movieAffiche.classList.add("image");

            movieAffiche.src = IMGPATH + movie.poster_path;
            movieAffiche.alt = movie.title;

            const movieInfo = document.createElement("div");
            movieInfo.classList.add("movie_info");

            const movieTitle = document.createElement("h3");
            movieTitle.classList.add("movie_title");
            movieTitle.textContent = movie.title
            
            const movieRating = document.createElement("p");
            movieRating.classList.add("movie_rating");
            movieRating.textContent = movie.vote_average;

            const movieDescription = document.createElement("div");
            movieDescription.classList.add("movie_description");
            movieDescription.textContent = movie.overview;
            movieDescription.style.display="none"
        
            movieInfo.appendChild(movieTitle);
            movieInfo.appendChild(movieRating);
            movielemnt.appendChild(movieAffiche);
            movielemnt.appendChild(movieInfo);
            movielemnt.appendChild(movieDescription);
            movie_container.appendChild(movielemnt);
            movielemnt.addEventListener("mouseover",() => {
                movieDescription.style.display="block";
                movieDescription.style.opacity = "1"
                movieInfo.style.display = "none";
                movieAffiche.style.opacity = "0.3"
            })
            movielemnt.addEventListener("mouseout",() => {
                movieDescription.style.display="none";
                movieAffiche.style.opacity = "2";
                movieInfo.style.display = "flex";
            })  

        });
    })
}

affimovie();
// Recherche par autocompletion 
function searchMovie(toSearch){
    fetch(APIURL)
    .then(reponse => reponse.json())
    .then(data =>{
        movie_container.innerHTML=''
        data.results.forEach(movie => {
            
            if (movie.title.toLowerCase().includes(toSearch)){
            const movielemnt=document.createElement("div");
            movielemnt.classList.add("movie");

            const movieAffiche = document.createElement("img");
            movieAffiche.classList.add("image");

            movieAffiche.src = IMGPATH + movie.poster_path;
            movieAffiche.alt = movie.title;

            const movieInfo = document.createElement("div");
            movieInfo.classList.add("movie_info");

            const movieTitle = document.createElement("h3");
            movieTitle.classList.add("movie_title");
            movieTitle.textContent = movie.title
            
            const movieRating = document.createElement("p");
            movieRating.classList.add("movie_rating");
            movieRating.textContent = movie.vote_average;

            const movieDescription = document.createElement("div");
            movieDescription.classList.add("movie_description");
            movieDescription.textContent = movie.overview;
            movieDescription.style.display="none"
        
            movieInfo.appendChild(movieTitle);
            movieInfo.appendChild(movieRating);
            movielemnt.appendChild(movieAffiche);
            movielemnt.appendChild(movieDescription);
            movielemnt.appendChild(movieInfo);
           
            movie_container.appendChild(movielemnt);
            movielemnt.addEventListener("mouseover",() => {
                movieDescription.style.display="block";
                movieDescription.style.opacity = "1"
                movieInfo.style.display = "none";
                movieAffiche.style.opacity = "0.3"
            })
            movielemnt.addEventListener("mouseout",() => {
                movieDescription.style.display="none";
                movieAffiche.style.opacity = "2";
                movieInfo.style.display = "flex";
            }) 
        } 

        });
    })
}
searchInput.addEventListener("input",() =>{
    const rechercher = searchInput.value.toLowerCase();
    searchMovie(rechercher)
})