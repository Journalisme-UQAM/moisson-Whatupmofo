#coding: utf-8


import json
import csv
import re 
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.tokenize import MWETokenizer


artist_keys = ["Loud(Canada)","LaryKidd","LoudLaryAjust","Koriass","FouKi","AlaclairEnsemble","DeadObies","Kirouac","LaF(Montreal)","SansPression","RoiHeenok","Souldia","ObialeChef","Sarahmée","Marie-Gold(Canada)","ManuMilitari","O.G.B(Canada)","Rymz","LesAnticipateurs","LocoLocass","Taktika","IZZY-S","Dubmatique","Tizzo","Muzion","Rainmen","LaConstellation","AtachTatuq","Omnikrom","Telus","K6A","SirPathétik","K-maro","Connaisseur","Vendou","BrownFamily","Rowjay" ,"YesMccan","Lost[FR]","JayScøttXSmittyBacalley","STxLIAM","KenLo","EmanXVlooper","Enima","White-B","SebaetHorg","MaybeWatson","Anodajay","JoeRocca","BadNylon","OstiOne","M.B"]

y = str(artist_keys)


for y in artist_keys:
	fichier = "rap_" + y + ".csv"

	file_name = "Lyrics_" + y + ".json"

	json_data=open(file_name).read()

	data = json.loads(json_data)

	for i in range(0,len(data["songs"])): #Prend toutes les chansons qui se trouvent dans le JSON.


		lyrics = str(data["songs"][i]["lyrics"].lower().replace("["," ").replace("1er"," ").replace("]"," ").replace("couplet"," ").replace(","," ").replace("!"," ").replace("?"," ").replace("("," ").replace(")"," ").replace("2e"," ").replace("refrain"," ").replace("hook"," ").replace("pre-hook"," ").replace("..."," ").replace("'","_").replace("’","_").replace("2ième"," ").replace("verse"," ").replace("outro"," ").replace("«"," ").replace("»"," ").replace("3e"," ").replace("3ième"," ").replace("pre-refrain"," ").replace("-"," ").replace("‘"," ").replace(":"," "))
		#Retourne les paroles en textes et nettoie les caractères qui ne sont pas des mots.
		token = nltk.word_tokenize(lyrics)
		#Sépare individuellement les mots tout en conservant les "'" pour le cas de don't, that's, etc. 
		count = {}
		#Crée un dictionnaire dans le but de compter les mots.

		for word in token:
			infos = []
			infos.append(data["songs"][i]["artist"]) 
			infos.append(data["songs"][i]["title"]) 
			infos.append(data["songs"][i]["album"]) 
			infos.append(data["songs"][i]["year"])
			infos.append(word.replace("_","'"))
			#Ainsi chaque mot sera accompagné de l'artiste, de l'album, de la chanson et de l'année (si cette dernière est disponible).

			if word in count:
				count[word] += 1
			else:
				count[word] = 1
			#Le script qui compte les mots, s'il se trouve déjà dans le dictionnaire, ça valeur augmente de 1, sinon la clé s'ajoute. Ainsi, si on compte la quantité de clés, on obtient la quantité de mots différents utilisés par un artiste donné.
			
			infos.append(len(count.keys()))

			f2 = open(fichier, "a")
			z = csv.writer(f2)
			z.writerow(infos)

		print(data["songs"][i]["artist"])
		print(len(count))

			#Pour l'instant, le script a encore quelques anomalies, mais j'y travaille très fort. 

	






		
		



		
	













			








