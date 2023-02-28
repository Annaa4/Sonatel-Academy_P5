import csv
import json
import fonctions
# from sys import exit
valideglo=[]
invalideglo=[]
invalide =[]
valide = []
csv_reader = csv.DictReader(open('donnees_projet_python.csv','r'))
#Convertir CSV en JSON
def csv_to_json():
    jsonArray=[]
    #convertir chaque ligne du fichier csv dans le dic Python
    for line in csv_reader:
    #ajouter chaque ligne dans le tableau
        jsonArray.append(line)
    #convertir python jsonArray en JSON String et écrire sur le fichier
    with open('project_data.json','w') as json_file:
        jsonstring = json.dumps(jsonArray)
        json_file.write(jsonstring)
    lire= open('project_data.json','r')
    data_lire = json.load(lire)

#Convertir CSV en XML
def csv_to_xml(line):
    return""" 
     <Eleve>
        <Numero> %s </Numero>
        <Nom> %s </Nom>
        <Prenom> %s </Prenom>
        <Date_de_naissance> %s </Date_de_naissance>
        <Classe> %s </Classe>
        <Note> %s </Note> 
                
    </Eleve>  """ %(line["Numero"],line["Nom"],line["Prénom"],line["Date de naissance"],line["Classe"],line["Note"])

with open('project_data.xml','w+') as xml_file:
    xml_file.write("<Eleves>")
    xml_file.write("\n".join([csv_to_xml(line) for line in csv_reader]))
    xml_file.write("\n")

#Lorsque l'utilisateur choisi de travailler avec JSON, le programme retourne les données valides sous format csv et invalides sous format xml
def choix_json(data_lire):
    valideglo=[]
    invalideglo=[]
    invalide =[]
    valide = []
    for row in data_lire:
        numero=fonctions.numero(row['Numero'])
        nom=fonctions.nom(row['Nom'])
        prenom=fonctions.prenom(row['Prénom'])
        date=fonctions.validdate(row['Date de naissance'])
        classe=fonctions.definirFormatClasse(row['Classe'])
        if classe == False:
            continue
        cl = fonctions.classeValide(classe)
        note=fonctions.note(row['Note']) 
    
        if (numero==True and nom==True and prenom==True and date==True and cl==True and note !=False):
            valide.append(row['Numero'])
            valide.append(row['Nom'])
            valide.append(row['Prénom'])
            valide.append(row['Date de naissance'])
            valide.append(classe)
            valide.append(note)
            valideglo.append(valide)
            valide =[]         
        else :
            invalide.append(row['Numero'])
            invalide.append(row['Nom'])
            invalide.append(row['Prénom'])
            invalide.append(row['Date de naissance'])
            invalide.append(classe)
            invalide.append(note)
            invalideglo.append(invalide)
            invalide=[]
    return valideglo,invalideglo
    # Mettre les donnees valides dans le fichier csv
def json_to_csv(valides_csv):
    header=['Numero','Nom','Prénom','Date de naissance','Classe','Note']
    with open('valides.csv','w') as csvf:
        # writer = csv.DictWriter(csvf,fieldnames=header)
        # writer.writeheader()
        # for line in valide:
        #  writer.writerows({"Numero":line[0],"Nom":line[1],"Prénom":line[2],"Date de naissance":line[3],"Classe":line[4],"Note":line[5]})
        csvstring=csv.writer(csvf, delimiter=",")
        csvstring.writerow(header)
        csvstring.writerows(valides_csv)


    #Mettre les donnees invalide dans le fichier xml 
    # with open('project.json') as json_file:
    #     d=json.load(json_file)
    #     import xml.etree.cElementTree as e
    #     root = e.Element("project")
    # for cle , valeur in d.items():
    #     elt = e.SubElement(root, cle)
