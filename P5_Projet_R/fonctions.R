verification_numero <- function(num){
    if (grepl("^[A-Z0-9]{7}+$", num)) {
      return(TRUE)
    } else {
      return(FALSE)
    }
  }

verification_nom <- function(nom){
  if(!grepl("^[[:alpha:]]",nom)){
    return(FALSE)
  }
  if (!grepl("^[[:alpha:]]{2,}$", nom)) {
    return(FALSE)
  }
  return(TRUE)
}

verification_prenom <- function(prenom){
  if(!grepl("^[[:alpha:]]",prenom)){
    return(FALSE)
  }
  if (!grepl("^[[:alpha:]]{3,}$", prenom)) {
    return(FALSE)
  }
  return(TRUE)
}
  
verification_classe <- function(classe) {
  #changement du format (nchar(classe),nchar(classe) permet de récuperer le dernier element)
  new_classe <- paste0(substring(classe,1,1), "iem", substring(classe,nchar(classe),nchar(classe)))
  if (substring(new_classe,1,1) %in% c("6","5","4","3") & substring(new_classe,nchar(new_classe),nchar(new_classe)) %in% c("A","B")){
    return(new_classe)
  }else{
    return(FALSE)
  }
}
Sys.setlocale("LC_TIME","fr_FR.UTF-8")
verification_date <- function(date){
  # Remplacer les caractères non numériques par des "/"
  date <- gsub("fev", "02", date)
  date <-gsub("février", "02", date)
  date <- gsub("mars","03", date)
  date <- gsub("decembre", "12", date)
  date_str <- gsub("[^0-9a-zA-Z]+", "/", date)
  t<-""
  format_date = c("%d/%m/%y","%d/%B/%Y","%d/%B/%y")
  # if (format(date) %in% format_date){
  for (i in format_date){
    new_date = as.Date(date_str,i)
  if (!is.na(new_date)){
      nouveau_date <- format(new_date, "%d/%m/%Y")
      return(nouveau_date)
  }}}
    
verification_date("28/Mars/1998")


