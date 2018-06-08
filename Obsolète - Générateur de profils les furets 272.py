from random import*
from datetime import datetime

def test (n):
    for j in range (0,len(n)):
        print (n[j])
        j=j+1
        
def NB ():
    NB=[]
    for i in range (0,272):
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

def genstrict (d,n):
    liste=[]
    for i in range (0,len(n)):
        while (n[i]!=0):
            liste.append(d[i])
            n[i]=n[i]-1
    return(liste)

XLDage=[18,	25,	30,	35,	40,	45,	50,	55,	60,	65,	70,	75];
XLNage=[6,	45,	68,	59,	41,	23,	12,	8,	5,	4,	1,	0];
age=genalea(XLDage,XLNage)
NBage=NB()

XLDDDP = [10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	20,	21,	22,	23,	24,	25,	26,	27,	28,	29,	30];
XLNDDP = [6,	1,	4,	1,	2,	31,	1,	3,	5,	2,	109,	0,	2,	2,	2,	91,	0,	0,	0,	0,	10]
DureeDuPret = genstrict(XLDDDP,XLNDDP)
NBDureeDuPret = NB()

XLDfumeur = ["oui","Non"]
XLNfumeur = [36,	236]
Fumeur = genstrict(XLDfumeur,XLNfumeur);
NBfumeur = NB()

XLDtypeDemprunt = ['Amortissable','In Fine'];
XLNtypeDemprunt = [257,	15]
TypeDemprunt = genstrict(XLDtypeDemprunt,XLNtypeDemprunt)
NBTypeDemprunt = NB()

XLDprofession = ["Agriculteur",	"Artisan",	"Chef d'entreprise",	"Commerçant" ,	"Enseignant",	"Etudiant",	
                 "Fonctionnaire",	"Salarié",	"Salarié cadre",	"Sans Profession",	"Recherche d'emploi",	
                 "Retraité",	"Ouvrier",	"Profession du spectacle",	"Profession Libérale",	
                 "Profession médicale",	"VRP"]
XLNprofession = [1,	5,	6,	5,	6,	1,	36,	80,	94,	2,	2,	15,	4,	1,	7,	7,	0]
Profession = genstrict(XLDprofession,XLNprofession)
NBProfession = NB()


XLDDP = ["Non","Moins de 15.000 km par an","Entre 15.000 et 20.000 km par an" ,"Plus de 20.000 km par an"]
XLNDP = [115,	123,	21,	13]
DeplacementProfessionel = genstrict(XLDDP,XLNDP)
NDDeplacementProfessionel = NB()

XLDManipulationObjetLourd = ["Oui","Non"];
XLNManipulationObjetLourd = [255,	17]
ManipulationObjetLourd = genstrict(XLDManipulationObjetLourd,XLNManipulationObjetLourd)
NBManipulationObjetLourd = NB()

XLDNombreDePretAAssurer = [1,2];
XLNNombreDePretAAssurer = [272,0] # Real values: [243,	29]
NombreDePretAAssurer = genstrict(XLDNombreDePretAAssurer,XLNNombreDePretAAssurer)
NBNombreDePretAAssurer = NB()


XLDMontant = [0,50000,100000,150000,200000,250000,300000,350000,400000,450000,500000,550000,600000]
XLNMontant = [8,	27,	62,	67,	47,	26,	14,	7,	4,	3,	2,	2,	3]
Montant = genalea(XLDMontant,XLNMontant)
NBMontant = NB()

XLDEmprunteurUnique = ["Oui","Non"];
XLNEmprunteurUnique = [272,0] # Real values :
EmprunteurUnique = genstrict(XLDEmprunteurUnique,XLNEmprunteurUnique)
NBEmprunteurUnique =NB()

XLDDifféréDamortissement = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24];
XLNDifféréDamortissement = [208,43,10,5,3,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
DifféréDamortissement = genstrict(XLDDifféréDamortissement,XLNDifféréDamortissement)
NBDifféréDamortissmeent = NB() #fausses valeurs

XLDDateDebutEmprunt = [0,90,180,270,365];
XLNDateDebutEmprunt = [208,40,10,8,6]
DateDebutEmprunt = genalea(XLDDateDebutEmprunt,XLNDateDebutEmprunt)
NBDateDebutDemprunt = NB() #FV

XLDTaux = [0,0.1,0.2,0.3,0.4,0.5,0.6,.7,0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3];
XLNTaux = [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	2,	2,	5,	11,	18,	27,	36,	38,	38,	33,	25,	18,	11,	5,	2,	1,	0,	0,	0,	0,	0]
Taux = genstrict(XLDTaux,XLNTaux)
NBTaux = NB()

XLDQuellePart = [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1];
XLNQuellePart = [240,10,5,4,3,2,2,2,2,2]
QuellePart = genstrict(XLDQuellePart,XLNQuellePart)
NBQuellePart = NB()##FV

XLDTypeDeTaux = ["Fixe","Variable"];
XLNTypeDeTaux = [208,64]
TypeDeTaux = genstrict(XLDTypeDeTaux,XLNTypeDeTaux)
NBTypeDeTaux = NB()##FV

XLDSexe = ["Homme","Femme"]
XLNSexe = [199,	73]
Sexe = genstrict(XLDSexe,XLNSexe)
NBSexe = NB()

XLDSatutMatrimoniale = ["Célibataire","Marié","Concubinage","Pacs","Divorcé","Instance de divorce",
                        "Union libre","Veuf","Vie maritale"];
XLNSatutMatrimoniale = [88,	80,	52,	40,	12,	0,	0,	0,	0]
SatutMatrimoniale = genstrict(XLDSatutMatrimoniale,XLNSatutMatrimoniale)
NBStatutMatrimoniale = NB()

XLDTypeDeContrat = ["CDI période d'essai terminée","Fonctionnaire ou assimilé","Education nationale","CDD",
                    "CDI période d'essai non terminée","Intérimaire","Intermittent du spectacle"];
XLNTypeDeContrat = [205,	38,	8,	1,	1,	0,	0]
XLDTypeDeContrat2 = ["CDI","CDD","Intérimaire","Saisonnier","TNS"];##compatible assurland
XLNTypeDeContrat2 = [243,5,1,1,22]
TypeDeContrat = genstrict(XLDTypeDeContrat2,XLNTypeDeContrat2)
NBTypeDeContrat = NB()

Département = ["Paris","Hauts-de-Seine","Rhône","Nord","Yvelines","Bouches du Rhône","Val-de-Marne",
               "Seine-St-Denis","Seine-et-Marne","Essonne","Val-d'Oise","Haute-Garonne","Gironde",
               "Loire-Atlantique","Haute-Savoie","Isère","Alpes-Maritimes","Hérault","Bas-Rhin",
               "Seine-Maritime","Pas-de-Calais","Var","Moselle","Oise","Ille-et-Vilaine","Ain","Haut-Rhin",
               "Loiret","Meurthe-et-Moselle","Pyrénées-Atlantiques","Puy-de-Dôme","Gard","Vaucluse",
               "Indre-et-Loire","Finistère","Savoie","Calvados","Eure","Drôme","Maine-et-Loire","Loire",
               "Marne","Côte d'Or","Morbihan","Somme","Doubs","Eure-et-Loir","Aisne","Charente Maritime",
               "Vienne","Saône-et-Loire","Pyrénées-Orientales","Vendée","Lot-et-Garonne","Landes","Sarthe",
               "Côtes d'Armor","Manche","Ardèche","Loir-et-Cher","Aude","Cher","Deux-Sèvres","Tarn",
               "Dordogne","Haute-Vienne","Yonne","Vosges","Tarn-et-Garonne","Ardennes","Jura","Allier",
               "Aube","Aveyron","Charente","Mayenne","Orne","Haute-Saône","Gers","Corrèze","Nièvre",
               "Hautes-Pyrénées","Alpes de Haute-Provence","Territoire-de-Belfort","Meuse","Haute-Loire",
               "Haute-Marne","Hautes-Alpes","Ariège","Indre","Lot","Cantal","Creuse","Lozère","Corse du Sud",
               "Haute-Corse"];
XLDNumeroDpt = [75,92,69,59,78,13,94,93,77,91,95,31,33,44,74,38,6,34,67,76,62,83,57,60,35,1,68,45,54,64,63,30,84,37,29,73,14,27,26,49,42,51,21,56,80,25,28,2,17,86,71,66,85,47,40,72,22,50,7,41,11,18,79,81,24,87,89,88,82,8,39,3,10,12,16,53,61,70,32,19,58,65,4,90,55,43,52,5,9,36,46,15,23,48,200,201]
XLNNumeroDpt = [26,	18,	13,	12,	11,	11,	10,	9,	8,	8,	8,	7,	7,	5,	5,	5,	5,	4,	4,	4,	4,	3,	3,	3,	3,	3,	3,	2,	2,	2,	2,	2,	2,	2,	2,	2,	2,	2,	2,	2,	2,	2,	2,	2,	2,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0]
NumeroDpt = genstrict(XLDNumeroDpt,XLNNumeroDpt)
NBDépartement = NB()

CD = []

def codePostal(n):
    c=randint(0,39200)
    while (((CD[c])//(1000))!=n):
        c=randint(0,39200)
    return (CD[c])


Région = ["Ile-de-France","Rhône-Alpes","Provence-Alpes-Côte d'Azur","Nord","Aquitaine","Midi-Pyrénées",
          "Pays-de-la-Loire","Languedoc","Centre","Bretagne","Alsace","Lorraine","Haute-Normandie",
          "Picardie","Bourgogne","Poitou-Charente","Basse-Normandie","Auvergne","Champagne",
          "Franche-Comté","Limousin","Corse"];
NBRégion = NB()

XLDDureeDeTravail = ["Temps plein","Temps partiel"];
XLNDureeDeTravail = [248,24]##FV
DureeDeTravail = genstrict(XLDDureeDeTravail,XLNDureeDeTravail)
NBDureeDeTravail = NB()

class profil:
    def __init__(self,ID, nombre_pret, montant, type_emprunt, type_taux, taux, durée_emprunt, différé, 
                 debut_emprunt, sexe, age, situation_matrimoniale, code_postal, profession, type_contrat, 
                 duree_travail, deplacement_pro, manipulation_objet, fumeur,nombre_emprunteur, quelle_part,
                 CA,CS,SM,P,TDC,DDT,DP,MOL,F,QP):
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
        self.coempSexe = CS
        self.coempAge = CA
        self.coempSM = SM
        self.coempP = P
        self.coempTDC = TDC
        self.coempDDT = DDT
        self.coempDP = DP
        self.coempMOL = MOL
        self.coempF = F
        self.coempQP = QP
        


    def impr(self):
        print("Emprunteur unique : ",self.nombre_emprunteur)
        print("Nombre de prêt a assurer : ", self.nombre_pret)
        print("Montant du pret : ", self.montant)
        print("Type d'emprunt : ", self.type_emprunt)
        print("Type de taux : ", self.type_taux)
        print("Taux : " , self.taux, " : %")
        print("Durée de l'emprunt : ",self.durée_emprunt,"  : ans")
        print("Durée du différé : ",self.différé, "  : mois")
        print("Début de l'emprunt : ", self.debut_emprunt, " : jours")
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
    
    def imprl(self):
        print(self.ID,":",self.nombre_emprunteur,":", self.nombre_pret,":", self.montant,":", 
              self.type_emprunt,":", self.type_taux,":" , self.taux,":",self.durée_emprunt,":",
              self.différé,":", self.debut_emprunt,":",self.sexe,":",self.age,":",
              self.situation_matrimoniale,":",self.code_postal,":",self.profession,":",
              self.type_contrat,":",self.duree_travail,":",self.deplacement_pro,":",
              self.manipulation_objet,":",self.fumeur,":",self.quelle_part,":",self.coempSexe,":",
              self.coempAge,":",self.coempSM,":",self.coempP,":",self.coempTDC,":",self.coempDDT,":",
              self.coempDP,":",self.coempMOL,":",self.coempF,":",self.coempQP)




NB =[NBage,NBNombreDePretAAssurer,NBMontant,NBTypeDemprunt,NBTypeDeTaux,NBTaux,NBDureeDuPret,
     NBDifféréDamortissmeent,NBDateDebutDemprunt,NBSexe,NBStatutMatrimoniale,NBDépartement,NBProfession,
     NBTypeDeContrat,NBDureeDeTravail,NDDeplacementProfessionel,NBManipulationObjetLourd,NBfumeur,
     NBEmprunteurUnique,NBQuellePart]

Crit =[age,NombreDePretAAssurer,Montant,TypeDemprunt,TypeDeTaux,Taux,DureeDuPret,DifféréDamortissement,
       DateDebutEmprunt,Sexe,SatutMatrimoniale,NumeroDpt,Profession,TypeDeContrat,DureeDeTravail,
       DeplacementProfessionel,ManipulationObjetLourd,Fumeur,EmprunteurUnique,QuellePart]

NB2 =[NBage,NBSexe,NBStatutMatrimoniale,NBProfession,NBTypeDeContrat,NBDureeDeTravail,
      NDDeplacementProfessionel,NBManipulationObjetLourd,NBfumeur]
Crit2 =[age,Sexe,SatutMatrimoniale,Profession,TypeDeContrat,DureeDeTravail,DeplacementProfessionel,
        ManipulationObjetLourd,Fumeur]

# Age,Sexe,SatutMatrimoniale,Profession,TypeDeContrat,DureeDeTravail,DeplacementProfessionel,ManipulationObjetLourd,Fumeur,QuellePart
liste_profil=[]
j=0
while j<272:
    i=0
    variables=[]
    for i in range(0,len(Crit)):
        k=randint(0,len(NB[i])-1)
        a=NB[i][k]
        while a==0:
            k=randint(0,len(NB[i])-1)
            a=NB[i][k]
        if i==11: # corresponde to NumeroDpt
            variables.append(codePostal(Crit[i][k]))
        elif i==18: #EmprunteurUnique
            if variables[0]<=30:
                variables.append("Oui")
            else:
                r=randint(0,100)
                if r<25:
                    variables.append("Oui")
                else:
                    variables.append("Non")
            if variables[18]=="Non":
                r2=randint(0,100)
                if r2<50:
                    variables.append(0.5)
                else:
                    variables.append(0.7)
                for t in range(0,len(Crit2)):
                    l=randint(0,len(NB2[t])-1)
                    aa=NB2[t][l]
                    while a==0:
                        l=randint(0,len(NB2[t])-1)
                        aa=NB2[t][l]
                    variables.append(Crit2[t][l])
                    NB2[t][l]=NB2[t][l]-1
                    t=t+1
                if r2<50:
                    variables.append(0.5)
                else:
                    variables.append(0.3)
            else:
                variables.append(1)
                for o in range(0,len(Crit2)+1):
                    variables.append(None)
        else:
            variables.append(Crit[i][k])
        NB[i][k]=NB[i][k]-1
        i=i+1
    liste_profil.append(profil(j+1,variables[0],variables[1],variables[2],variables[3],variables[4],
                               variables[5],variables[6],variables[7],variables[8],variables[9],
                               variables[10],variables[11],variables[12],variables[13],variables[14],
                               variables[15],variables[16],variables[17],variables[18],variables[19],
                               variables[20],variables[21],variables[22],variables[23],variables[24],
                               variables[25],variables[26],variables[27],variables[28],variables[29]))
    j=j+1

for m in range(0,len(liste_profil)):
    imprl(liste_profil[m])

##print(datetime.now().date().month)

