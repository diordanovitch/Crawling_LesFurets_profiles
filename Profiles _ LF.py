# Code to generate the set of 500 profiles for Les Furets crawling, set in june 2018.
# As there are many conditions to generate the set, the code will not work at each time, you have to repeat until it works.


import pandas as pd
import numpy as np
import random as rd
import csv 

from random import*
from datetime import datetime




class profil:
    def __init__(self,ID, age, nombre_pret, montant, type_emprunt, type_taux, taux, durée_emprunt, différé, 
                 debut_emprunt, sexe, situation_matrimoniale, code_postal, profession, type_contrat, 
                 duree_travail, deplacement_pro, manipulation_objet, fumeur,nombre_emprunteur, quelle_part,
                 objet,emprunt_vigueur,emprunt_signe,banque_preteuse):
        self.ID = ID
        self.nombre_emprunteur = nombre_emprunteur
        self.nombre_pret = nombre_pret
        self.montant = montant
        self.type_emprunt = type_emprunt
        self.type_taux = type_taux
        self.taux = taux
        self.durée_emprunt = durée_emprunt
        self.différé = différé
        self.debut_emprunt = debut_emprunt
        self.sexe = sexe
        self.age = age
        self.situation_matrimoniale = situation_matrimoniale
        self.code_postal = code_postal
        self.profession = profession
        self.type_contrat = type_contrat
        self.duree_travail = duree_travail
        self.deplacement_pro = deplacement_pro
        self.manipulation_objet = manipulation_objet
        self.fumeur = fumeur
        self.quelle_part = quelle_part
        self.objet = objet
        self.emprunt_vigueur = emprunt_vigueur
        self.emprunt_signe = emprunt_signe
        self.banque_preteuse = banque_preteuse



    def impr(self):
        print("Emprunteur unique : ",self.nombre_emprunteur)
        print("Nombre de prêt a assurer : ", self.nombre_pret)
        print("Montant du pret : ", self.montant)
        print("Type d'emprunt : ", self.type_emprunt)
        print("Type de taux : ", self.type_taux)
        print("Taux : " , self.taux, " : %")
        print("Durée de l'emprunt : ",self.durée_emprunt,"  : ans")
        print("Durée du différé : ",self.différé, "  : mois")
        print("Délai avant emprunt : ", self.debut_emprunt, " : mois")
        print("Sexe : " ,self.sexe)
        print("Age : ",self.age, " : ans")
        print("Statut : ", self.situation_matrimoniale)
        print("Code postal : " ,self.code_postal)
        print("Profession : " , self.profession)
        print("Type de contrat : " ,self.type_contrat)
        print("Durée de travail : ", self.duree_travail)
        print("Déplacement professionel : ", self.deplacement_pro)
        print("Manipulation d'objets lourds : ", self.manipulation_objet)
        print("Fumeur : ", self.fumeur)
        print("Pour quelle part du pret etre assuré : ", self.quelle_part)
        print("Quel est l'objet du prêt : ", self.objet)
        print("L'emprunt est-il déjà signé ? : ", self.emprunt_vigueur)
        print("L'emprunt est-il signé depuis plus d'un an ? : ", self.emprunt_signe)
        print("Quelle est la banque prêteuse ? : ", self.banque_preteuse)
    
    def imprl(self):
        print(self.ID,":",self.nombre_emprunteur,":", self.nombre_pret,":", self.montant,":", 
              self.type_emprunt,":", self.type_taux,":" , self.taux,":",self.durée_emprunt,":",
              self.différé,":", self.debut_emprunt,":",self.sexe,":",self.age,":",
              self.situation_matrimoniale,":",self.code_postal,":",self.profession,":",
              self.type_contrat,":",self.duree_travail,":",self.deplacement_pro,":",
              self.manipulation_objet,":",self.fumeur,":",self.quelle_part,":",self.objet,":",
              self.emprunt_vigueur,":",self.emprunt_signe,":",self.banque_preteuse)
        
    def listp(self):
        return(["FUR2018", self.ID, "FUR2018_"+str(self.ID), self.nombre_emprunteur, self.nombre_pret, self.montant, self.type_emprunt,
                self.type_taux, self.taux, self.durée_emprunt, self.différé, self.debut_emprunt, self.sexe, self.age,
                self.situation_matrimoniale, self.code_postal, self.profession, self.type_contrat, self.duree_travail,
                self.deplacement_pro,self.manipulation_objet,self.fumeur,self.quelle_part, "", self.objet, 
                self.emprunt_vigueur, self.emprunt_signe,self.banque_preteuse])






def test (n):
    for j in range (0,len(n)):
        print (n[j])
        j=j+1
        
def NB ():
    NB=[]
    for i in range (0,500):
        NB.append(1)
    return(NB)

def genalea (d,n):
    liste=[]
    for i in range (0,len(n)):
        while (n[i]!=0):
            if i==len(n)-1:
                liste.append(d[i])
            else:
                liste.append(randint(d[i],d[i+1]-1))
            n[i]=n[i]-1
    return(liste)

def genalea_rate (d,n):
    liste=[]
    for i in range (0,len(n)):
        while (n[i]!=0):
            if i==len(n)-1:
                liste.append(d[i])
            else:
                liste.append( round ( rd.uniform(d[i],d[i+1]) ,2))
            n[i]=n[i]-1
    return(liste)



def genstrict (d,n):
    liste=[]
    for i in range (0,len(n)):
        while (n[i]!=0):
            liste.append(d[i])
            n[i]=n[i]-1
    return(liste)




CP_all = pd.read_csv('CP_all.csv')


XLDage=[18,	25,	30,	35,	40,	45,	50,	55,	60,	65,	70,	75,90];
XLNage=[10,	55,	90,	100,	85,	75,	45,	30,	5,	3,	1,	1,0];
age=genalea(XLDage,XLNage)
NBage=NB()

XLDDDP = [0,5,10,15,20,25,30,50];
XLNDDP = [10,35,80,115,125,125,10]
DureeDuPret = genalea(XLDDDP,XLNDDP)
NBDureeDuPret = NB()

XLDfumeur = ["Oui","Non"]
XLNfumeur = [55,	445]
Fumeur = genstrict(XLDfumeur,XLNfumeur);
NBfumeur = NB()

XLDtypeDemprunt = ['Amortissable','In Fine'];
XLNtypeDemprunt = [495,	5]
TypeDemprunt = genstrict(XLDtypeDemprunt,XLNtypeDemprunt)
NBTypeDemprunt = NB()

XLDprofession = ["Agriculteur",	"Artisan", "Au foyer", 	"Chef d'entreprise",	"Commerçant" ,	"Enseignant",	"Etudiant",	
                 "Fonctionnaire",	"Salarié",	"Salarié cadre",	"Sans Profession",	"Recherche d'emploi",	
                 "Retraité",	"Ouvrier",	"Profession du spectacle",	"Profession Libérale",	"VRP"]
XLNprofession = [5,	10,	5,	20,	5,	10,	5,	73,	189,	153,	0,	5,	5,	0,	0,	15,	0]
Profession = genstrict(XLDprofession,XLNprofession)
NBProfession = NB()


XLDDP = ["Moins de 15.000 km par an","Entre 15.000 et 30.000 km par an" ,"Plus de 30.000 km par an", ""]
XLNDP = [389,	76,	15, 20]
DeplacementProfessionel = genstrict(XLDDP,XLNDP)
NDDeplacementProfessionel = NB()

XLDManipulationObjetLourd = ["Oui","Non", ""];
XLNManipulationObjetLourd = [45,	435, 20]
ManipulationObjetLourd = genstrict(XLDManipulationObjetLourd,XLNManipulationObjetLourd)
NBManipulationObjetLourd = NB()

XLDNombreDePretAAssurer = [1,2];
XLNNombreDePretAAssurer = [500,0] # Real values: [410,	90]
NombreDePretAAssurer = genstrict(XLDNombreDePretAAssurer,XLNNombreDePretAAssurer)
NBNombreDePretAAssurer = NB()


XLDMontant = [1000,50000,100000,150000,200000,250000,300000,350000,400000,450000,500000,550000,600000]
XLNMontant = [30,	90,	130,	110,	65,	30,	20,	10,	5,	5,	1,	1,	3]
Montant = genalea(XLDMontant,XLNMontant)
NBMontant = NB()

XLDEmprunteurUnique = ["Oui","Non"];
XLNEmprunteurUnique = [500,0] # Real values : [175,	325]
EmprunteurUnique = genstrict(XLDEmprunteurUnique,XLNEmprunteurUnique)
NBEmprunteurUnique =NB()

XLDDifféréDamortissement = [1,6,12,18,24,36,48];
XLNDifféréDamortissement = [15,5,10,5,5,5]
XLDDifféréDamortissementStrict = [0]
XLNDifféréDamortissementStrict = [455]
DifféréDamortissement = genalea(XLDDifféréDamortissement,XLNDifféréDamortissement)
DifféréDamortissement.extend(genstrict(XLDDifféréDamortissementStrict,XLNDifféréDamortissementStrict))
NBDifféréDamortissmeent = NB()

XLDDelaiDebutEmprunt = [1,6,12,18,24];
XLNDelaiDebutEmprunt = [234,33,1,0]
XLDDelaiDebutEmpruntStrict = [0]
XLNDelaiDebutEmpruntStrict = [232]
DelaiDebutEmprunt = genalea(XLDDelaiDebutEmprunt,XLNDelaiDebutEmprunt)
DelaiDebutEmprunt.extend(genstrict(XLDDelaiDebutEmpruntStrict, XLNDelaiDebutEmpruntStrict))
NBDelaiDebutEmprunt = NB() 

XLDTaux = [0,1,1.2,1.4,1.6,1.8,2,2.5,3,4,10];
XLNTaux = [25,	35,	65,	85,	80,	70,	70,	35,	25,	10,0]
Taux = genalea_rate(XLDTaux,XLNTaux)
NBTaux = NB()

XLDQuellePart = [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1];
XLNQuellePart = [500,0,0,0,0,0,0,0,0,0] # Real values : [355,	0,10,15,10,105,0,0,0,0]
QuellePart = genstrict(XLDQuellePart,XLNQuellePart)
NBQuellePart = NB()

XLDTypeDeTaux = ["Fixe","Variable"];
XLNTypeDeTaux = [485,15]
TypeDeTaux = genstrict(XLDTypeDeTaux,XLNTypeDeTaux)
NBTypeDeTaux = NB()

XLDSexe = ["Homme","Femme"]
XLNSexe = [300,	200]
Sexe = genstrict(XLDSexe,XLNSexe)
NBSexe = NB()

XLDSatutMatrimoniale = ["Célibataire","Marié","Concubinage","Pacs","Séparé", "Divorcé", "Veuf"];
XLNSatutMatrimoniale = [106,	220,	90,	62,	3,	18,	1]
SatutMatrimoniale = genstrict(XLDSatutMatrimoniale,XLNSatutMatrimoniale)
NBStatutMatrimoniale = NB()

XLDTypeDeContrat = ["CDI","CDD","Intérimaire","Saisonnier","TNS", ""];
XLNTypeDeContrat = [420,	35,	10,	5,	10, 20]
TypeDeContrat = genstrict(XLDTypeDeContrat,XLNTypeDeContrat)
NBTypeDeContrat = NB()


XLDDureeDeTravail = ["Temps plein","Temps partiel", ""];
XLNDureeDeTravail = [450,30,20]
DureeDeTravail = genstrict(XLDDureeDeTravail,XLNDureeDeTravail)
NBDureeDeTravail = NB()



XLDRegion = ["Ile_de_France","Rhone_Alpes","PACA","Nord_pas_de_Calais","Aquitaine","Midi_Pyrenees",
          "Pays_de_la_Loire","Languedoc","Centre","Bretagne","Alsace","Lorraine","Normandie",
          "Picardie","Bourgogne","Poitou_Charente","Auvergne","Champagne",
          "Franche_Comte","Limousin","Corse"];
XLNRegion = [110,55,50,35,30,25,25,25,20,15,10,15,15,15,10,10,10,10,10,5,0]
Region = genstrict(XLDRegion,XLNRegion)
NBRegion = NB()


XLDObjet = ["Résidence principale", "Résidence secondaire", "Investissement locatif", "Autres"]
XLNObjet = [394,17,65,24]
Objet = genstrict(XLDObjet,XLNObjet)
NBObjet = NB()


XLDEmpruntEnVigueur = ["Prêt signé", "Prêt à signer"] 
XLNEmpruntEnVigueur = [330,170]
EmpruntEnVigueur = genstrict(XLDEmpruntEnVigueur,XLNEmpruntEnVigueur)
NBEmpruntEnVigueur = NB()


XLDEmpruntSigneDepuis1an = ["Oui", "Non", ""]
XLNEmpruntSigneDepuis1an = [240,90, 170]
EmpruntSigneDepuis1an = genstrict(XLDEmpruntSigneDepuis1an,XLNEmpruntSigneDepuis1an)
NBEmpruntSigneDepuis1an = NB()



XLDBanquePreteuse = ["Je ne sais pas", "AXA banque", "Banque populaire", "Banque postale", "Barclays", "BNP Paribas", 
                     "Boursorama", "Caisse d'Epargne", "CIC", "Credit Agricole", "Credit du Nord", "Credit Foncier de France", 
                     "Credit Immobilier de France", "Credit mutuel", "HSBC", "ING Direct", "LCL", "Société Générale", "Autre"]
XLNBanquePreteuse = [41,3,38,31,1,26,8,59,22,117,5,18,2,44,3,2,26,30,24]
BanquePreteuse = genstrict(XLDBanquePreteuse,XLNBanquePreteuse)
NBBanquePreteuse = NB()






NB =[NBage,NBNombreDePretAAssurer,NBMontant,NBTypeDemprunt,NBTypeDeTaux,NBTaux,NBDureeDuPret,
     NBDifféréDamortissmeent,NBDelaiDebutEmprunt,NBSexe,NBStatutMatrimoniale,NBRegion,NBQuellePart,
     NBfumeur,NBEmprunteurUnique,NBProfession, NBManipulationObjetLourd, NBTypeDeContrat, NBDureeDeTravail, 
     NDDeplacementProfessionel,NBObjet,NBEmpruntEnVigueur, NBEmpruntSigneDepuis1an, NBBanquePreteuse]

Crit =[age,NombreDePretAAssurer,Montant,TypeDemprunt,TypeDeTaux,Taux,DureeDuPret,DifféréDamortissement,
       DelaiDebutEmprunt,Sexe,SatutMatrimoniale,Region,QuellePart,Fumeur,EmprunteurUnique, Profession, ManipulationObjetLourd,
       TypeDeContrat,DureeDeTravail, DeplacementProfessionel,Objet, EmpruntEnVigueur, EmpruntSigneDepuis1an, BanquePreteuse]







liste_profil=[]
j=0
e=0
while j<500:
    i=0
    variables=[]
    
    for i in range(0,len(Crit)):
        k=randint(0,len(NB[i])-1)
        a=NB[i][k]
        
        while a==0: # dans ce cas ça veut dire qu'on a déjà ajouté cette version du critère
            k=randint(0,len(NB[i])-1)
            a=NB[i][k]
        
        if i==11: # on tire un code postal aléatoirement de la région
            r = Crit[i][k]
            cp = int ( CP_all[CP_all['REGION'] == r] ['Code_postal'].sample(n=1) )
            cp = str(cp).zfill(5)
            variables.append(cp)
        

            
            
        elif i==6: # durée en fonction de montant : -de 15 ans pour -de 50.000
            if variables[2] < 50000:
                while Crit[i][k]>15 or a==0:
                    k=randint(0,len(NB[i])-1)
                    a=NB[i][k]
                variables.append(Crit[i][k])

            else:        
                variables.append(Crit[i][k])
                
        
        elif i==22: # emprunt signé depuis.. seulement si emprunt en vigueur
            if variables[21] == "Prêt à signer":
                while Crit[i][k]!="" or a==0:
                    k=randint(0,len(NB[i])-1)
                    a=NB[i][k]
                variables.append(Crit[i][k])
                
            elif variables[21] == "Prêt signé":
                while Crit[i][k]=="" or a==0:
                    k=randint(0,len(NB[i])-1)
                    a=NB[i][k]
                variables.append(Crit[i][k])

            else:        
                variables.append(Crit[i][k])
                
       
    
        elif i==15: # si +65 ans alors retraité, et inversement
            if variables[0] >= 65:
                while Crit[i][k]!="Retraité" or a==0:
                    k=randint(0,len(NB[i])-1)
                    a=NB[i][k]
                variables.append(Crit[i][k])
    
            else:
                while Crit[i][k]=="Retraité" or a==0:
                    k=randint(0,len(NB[i])-1)
                    a=NB[i][k]
                variables.append(Crit[i][k])
    
    
    
        elif i==17: # si pas de profession alors pas de contrat, si salarié/cadre alors pas de TNS, si cadre alors pas de TNS/saisonnier
            if variables[15] == "Recherche d'emploi" or variables[15] =="Au foyer" or variables[15] =="Etudiant" or variables[15] =="Retraité":
                while Crit[i][k]!="" or a==0:
                    k=randint(0,len(NB[i])-1)
                    a=NB[i][k]
                variables.append(Crit[i][k])
            
            elif variables[15] == "Salarié" or variables[15] =="Salarié cadre":
                while Crit[i][k]=="TNS" or Crit[i][k]=="" or a==0:
                    k=randint(0,len(NB[i])-1)
                    a=NB[i][k]
                variables.append(Crit[i][k])
              
            
            elif variables[15] =="Salarié cadre":
                while Crit[i][k]=="Saisonnier" or Crit[i][k]=="" or a==0:
                    k=randint(0,len(NB[i])-1)
                    a=NB[i][k]
                variables.append(Crit[i][k])
            
            

            else:
                while Crit[i][k]=="" or a==0:
                    k=randint(0,len(NB[i])-1)
                    a=NB[i][k]
                variables.append(Crit[i][k])
        
        
        elif i==18: # si pas de profession alors pas de tps travail
            if variables[15] == "Recherche d'emploi" or variables[15] =="Au foyer" or variables[15] =="Etudiant" or variables[15] =="Retraité":
                while Crit[i][k]!="" or a==0:
                    k=randint(0,len(NB[i])-1)
                    a=NB[i][k]
                variables.append(Crit[i][k])

            else:        
                while Crit[i][k]=="" or a==0:
                    k=randint(0,len(NB[i])-1)
                    a=NB[i][k]
                variables.append(Crit[i][k])
                
                
        elif i==19: # si pas de profession alors pas de deplacements pro
            if variables[15] == "Recherche d'emploi" or variables[15] =="Au foyer" or variables[15] =="Etudiant" or variables[15] =="Retraité":
                while Crit[i][k]!="" or a==0:
                    k=randint(0,len(NB[i])-1)
                    a=NB[i][k]
                variables.append(Crit[i][k])

            else:        
                while Crit[i][k]=="" or a==0:
                    k=randint(0,len(NB[i])-1)
                    a=NB[i][k]
                variables.append(Crit[i][k])
                
                
                
        elif i==16: # si pas de profession alors pas d'outillage, et outillage réservé en priorité à certaines professions    
            if variables[15] == "Recherche d'emploi" or variables[15] =="Au foyer" or variables[15] =="Etudiant" or variables[15] =="Retraité":
                while Crit[i][k]!="" or a==0:
                    k=randint(0,len(NB[i])-1)
                    a=NB[i][k]
                variables.append(Crit[i][k])

            elif variables[15] == "Salarié cadre":
                while Crit[i][k]=="Oui" or Crit[i][k]=="" or a==0:
                    k=randint(0,len(NB[i])-1)
                    a=NB[i][k]
                variables.append(Crit[i][k])
        
            elif variables[15] == "Agriculteur" or variables[15] == "Artisan" or variables[15] == "Chef d'entreprise" or variables[15] == "Commerçant":
                while (Crit[i][k]!="Oui" or a==0) and e<500:
                    k=randint(0,len(NB[i])-1)
                    a=NB[i][k]
                    e=e+1
                if Crit[i][k]!="": 
                    variables.append(Crit[i][k])
                else:
                    while Crit[i][k]=="" or a==0:
                        k=randint(0,len(NB[i])-1)
                        a=NB[i][k]
                    variables.append(Crit[i][k])
        
            
            
            else:        
                while Crit[i][k]=="" or a==0:
                    k=randint(0,len(NB[i])-1)
                    a=NB[i][k]
                variables.append(Crit[i][k])
        
             
            
            
            
        else:        
            variables.append(Crit[i][k])
                
            
            
            
        NB[i][k]=NB[i][k]-1 # 1 version du critère ajoutée, donc on passe son index à 0
        i=i+1
    liste_profil.append(profil(j+1,variables[0],variables[1],variables[2],variables[3],variables[4],
                               variables[5],variables[6],variables[7],variables[8],variables[9],
                               variables[10],variables[11],variables[15],variables[17],variables[18],
                               variables[19],variables[16],variables[13],variables[14],variables[12],
                               variables[20],variables[21],variables[22],variables[23]))
    j=j+1





with open("Profiles_LF.csv", "a", newline="") as file :
    Profiles_LF = csv.writer(file)
    Profiles_LF.writerow(["level","id", "profil_id", "applicantcount", "loannb", "firstloan_amount", 
              "firstloan_type", "firstloan_type_tax" , "firstloan_rate","firstloan_duration_years",
              "firstloan_differ", "contract_start_days","primary_applicant_sex","primary_applicant_age",
              "primary_applicant_marital_status","post_code","primary_applicant_occupation_code",
              "primary_applicant_contract","primary_applicant_working_time","primary_applicant_travel",
              "primary_applicant_risk","primary_applicant_smoke","primary_applicant_share","contract_start_date","object",
              "loan_effective","loan_one_year","lending_bank"])    


for p in range(0,len(liste_profil)):
    profil.imprl(liste_profil[p])
    with open("Profiles_LF.csv", "a", newline="") as file :
        Profiles_LF = csv.writer(file)
        Profiles_LF.writerow(profil.listp(liste_profil[p]))