# coding: utf-8

### Bon premier script. Le moissonnage se fait souvent en plusieurs étapes. C'en est une bonne première.

import lyricsgenius
#Il faut d'abord faire un pip install lyricsgenius dans le teminal

from apiJHR import t ### J'ai pris soin de confiner mon access token, info sensible, dans un fichier à part

### Pour faire un test, j'ai pris une autre liste
artist_keys = ["Loud(Canada)","Lary Kidd","LourLaryAjust","Koriass","FouKi","Alaclair Ensemble","Dead Obies","Kirouac" ,"LaF (Montreal)","Sans Pression","Roi Heenok","Souldia","Obia le Chef","Sarahmée","Marie Gold (Canada)","Manu Militari","O.G.B (Canada)","Rymz","Les Anticipateurs","Loco Locass","Taktika","IZZY-S","Dubmatique","Tizzo","Muzion","Rainmen","La Constellation","Atach Tatuq","Omnikrom","Telus","K6A","Sir Pathétik","K-maro","Connaisseur","Vendou","Brown Family" ,"Rowjay" ,"Yes Mccan","Lost [FR]","Jay Scøtt","ST x LIAM","KenLo","Eman X Vlooper","Enima","White-B","Seba et Horg","Maybe Watson","Anodajay","Joe Rocca","Bad Nylon","Osti One","M.B"]

artistes = [
	"Alfredo Zitarrosa",
	"Carlos Gardel"
]

for artiste in artistes:

	genius = lyricsgenius.Genius(t) #Ici on doit mettre son client acces token entre les " " ### J'ai inclus le mien
	artist = genius.search_artist(artiste, sort="title") #Cherche chaque artiste dans la liste plus haut et les classe par ordre alphabétique de titre 
	genius.skip_non_songs == False # Retire tous les éléments qui ne sont pas considérés comme une chanson
	genius.excluded_terms == ["(Remix)", "(Live)"] #Enlève les enregistrements live et les remix, on aurait aussi pu, avec cette commande, retirer les freestyles, mais nous avons décider, d'un commun accord de les garder. 
	artist.save_lyrics() #Sauvegarde l'ensemble des morceaux d'un artiste disponible sur Genius dans un fichier JSON 

### En l'essayant de mon côté, ça me donne un fichier JSON par chanson, cependant...