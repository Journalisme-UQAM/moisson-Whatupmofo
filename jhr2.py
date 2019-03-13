#coding: utf-8

### Excellente 2e étape. Effort manifeste et soutenu.
### Ton script fonctionne très bien. J'ai pu le reproduire avec quelques adaptations.

import json
import csv
import re 
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.tokenize import MWETokenizer

artist_keys = ["Loud(Canada)","LaryKidd","LoudLaryAjust","Koriass","FouKi","AlaclairEnsemble","DeadObies","Kirouac","LaF(Montreal)","SansPression","RoiHeenok","Souldia","ObialeChef","Sarahmée","Marie-Gold(Canada)","ManuMilitari","O.G.B(Canada)","Rymz","LesAnticipateurs","LocoLocass","Taktika","IZZY-S","Dubmatique","Tizzo","Muzion","Rainmen","LaConstellation","AtachTatuq","Omnikrom","Telus","K6A","SirPathétik","K-maro","Connaisseur","Vendou","BrownFamily","Rowjay" ,"YesMccan","Lost[FR]","JayScøttXSmittyBacalley","STxLIAM","KenLo","EmanXVlooper","Enima","White-B","SebaetHorg","MaybeWatson","Anodajay","JoeRocca","BadNylon","OstiOne","M.B"]

### J'essaie avec mes artistes
tounes = [
"lyrics_alfredozitarrosa_adagioenmipaís.json",
"lyrics_alfredozitarrosa_ajoséartigas.json",
"lyrics_alfredozitarrosa_cancióndeloshorneros.json",
"lyrics_alfredozitarrosa_candombedelolvidocandombre.json",
"lyrics_alfredozitarrosa_cantodenadie.json",
"lyrics_alfredozitarrosa_chamarritadelosmilicos.json",
"lyrics_alfredozitarrosa_chamarritadeunabailanta.json",
"lyrics_alfredozitarrosa_chotededontatú.json",
"lyrics_alfredozitarrosa_comounjazmíndelpaís.json",
"lyrics_alfredozitarrosa_coplasalcompadrejuanmiguel.json",
"lyrics_alfredozitarrosa_coplasdebaguala.json",
"lyrics_alfredozitarrosa_coplasdelcanto.json",
"lyrics_alfredozitarrosa_crecedesdeelpie.json",
"lyrics_alfredozitarrosa_cuecadelregreso.json",
"lyrics_alfredozitarrosa_decorralesatranqueras.json",
"lyrics_alfredozitarrosa_defensadelcantor.json",
"lyrics_alfredozitarrosa_defensadelgaucho.json",
"lyrics_alfredozitarrosa_delalucha.json",
"lyrics_alfredozitarrosa_denoolvidar.json",
"lyrics_alfredozitarrosa_diezdecimasdesaludoalpúblicoargentino.json",
"lyrics_alfredozitarrosa_doñasoledad.json",
"lyrics_alfredozitarrosa_doñasoledadcandombe.json",
"lyrics_alfredozitarrosa_duermenegrito.json",
"lyrics_alfredozitarrosa_dulcejuanita.json",
"lyrics_alfredozitarrosa_elcamba.json",
"lyrics_alfredozitarrosa_eldiccionario.json",
"lyrics_alfredozitarrosa_ellocoantonio.json",
"lyrics_alfredozitarrosa_elpericón.json",
"lyrics_alfredozitarrosa_elponcho.json",
"lyrics_alfredozitarrosa_elretobao.json",
"lyrics_alfredozitarrosa_elviolíndebecho.json",
"lyrics_alfredozitarrosa_enblancoynegro.json",
"lyrics_alfredozitarrosa_gatodelascuchillas.json",
"lyrics_alfredozitarrosa_guitarranegra.json",
"lyrics_alfredozitarrosa_guitarrero.json",
"lyrics_alfredozitarrosa_guitarreroviejo.json",
"lyrics_alfredozitarrosa_historiadejuanfiel.json",
"lyrics_alfredozitarrosa_historiadeunviejo.json",
"lyrics_alfredozitarrosa_hoydesdeaqui.json",
"lyrics_alfredozitarrosa_hoydesdeaquípoemas.json",
"lyrics_alfredozitarrosa_juancopete.json",
"lyrics_alfredozitarrosa_laamorosa.json",
"lyrics_alfredozitarrosa_lacanciónquiere.json",
"lyrics_alfredozitarrosa_lacanciónyelpoema.json",
"lyrics_alfredozitarrosa_lacoyunda.json",
"lyrics_alfredozitarrosa_lacuna.json",
"lyrics_alfredozitarrosa_laleyesteladearaña.json",
"lyrics_alfredozitarrosa_laniñahuichola.json",
"lyrics_alfredozitarrosa_larondacatonga.json",
"lyrics_alfredozitarrosa_lavueltadeobligado.json",
"lyrics_alfredozitarrosa_losboliches.json",
"lyrics_alfredozitarrosa_loshermanos.json",
"lyrics_alfredozitarrosa_malagueña.json",
"lyrics_alfredozitarrosa_maríadelasesquinas.json",
"lyrics_alfredozitarrosa_mariposanegra.json",
"lyrics_alfredozitarrosa_milicoepueblo.json",
"lyrics_alfredozitarrosa_milongadelalmai.json",
"lyrics_alfredozitarrosa_milongadelalmaii.json",
"lyrics_alfredozitarrosa_milongadelalmaiii.json",
"lyrics_alfredozitarrosa_milongadelalmaiv.json",
"lyrics_alfredozitarrosa_milongadelcordobés.json",
"lyrics_alfredozitarrosa_milongadelqueseausenta.json",
"lyrics_alfredozitarrosa_milongadeltartamudo.json",
"lyrics_alfredozitarrosa_milongadeojosdorados.json",
"lyrics_alfredozitarrosa_milongaendo.json",
"lyrics_alfredozitarrosa_milongaparaunaniña.json",
"lyrics_alfredozitarrosa_muchachacampesina.json",
"lyrics_alfredozitarrosa_negrachau.json",
"lyrics_alfredozitarrosa_nomeesperes.json",
"lyrics_alfredozitarrosa_nosepuede.json",
"lyrics_alfredozitarrosa_palqueseva.json",
"lyrics_alfredozitarrosa_paracarlamoriana.json",
"lyrics_alfredozitarrosa_polleraazuldelino.json",
"lyrics_alfredozitarrosa_porprudenciocorrea.json",
"lyrics_alfredozitarrosa_quédebohacer.json",
"lyrics_alfredozitarrosa_quépena.json",
"lyrics_alfredozitarrosa_quepenalitoraleña.json",
"lyrics_alfredozitarrosa_recordandote.json",
"lyrics_alfredozitarrosa_romanceparaunnegromilonguero.json",
"lyrics_alfredozitarrosa_señoritaerre.json",
"lyrics_alfredozitarrosa_sincaballoyenmontiel.json",
"lyrics_alfredozitarrosa_sitevas.json",
"lyrics_alfredozitarrosa_stefanie.json",
"lyrics_alfredozitarrosa_triunfoagrario.json",
"lyrics_alfredozitarrosa_zambaparavos.json",
"lyrics_alfredozitarrosa_zambaporvos.json",
"lyrics_carlosgardel_adiósmuchachos.json",
"lyrics_carlosgardel_almaenpena.json",
"lyrics_carlosgardel_almagro.json",
"lyrics_carlosgardel_almundolefaltauntornillo.json",
"lyrics_carlosgardel_alpiedelasantacruz.json",
"lyrics_carlosgardel_amoresdeestudiante.json",
"lyrics_carlosgardel_anclaoenparis.json",
"lyrics_carlosgardel_arrabalamargo.json",
"lyrics_carlosgardel_bandoneonarrabalero.json",
"lyrics_carlosgardel_barrioreo.json",
"lyrics_carlosgardel_buenosaires.json",
"lyrics_carlosgardel_caminito.json",
"lyrics_carlosgardel_chorra.json",
"lyrics_carlosgardel_confesion.json",
"lyrics_carlosgardel_cuestaabajo.json",
"lyrics_carlosgardel_eldiaquemequieras.json",
"lyrics_carlosgardel_estanochemeemborracho.json",
"lyrics_carlosgardel_estudiante.json",
"lyrics_carlosgardel_fayuto.json",
"lyrics_carlosgardel_gardeltangoporunacabeza.json",
"lyrics_carlosgardel_garufa.json",
"lyrics_carlosgardel_golondrinas.json",
"lyrics_carlosgardel_guitarraguitarramía.json",
"lyrics_carlosgardel_lacancióndebuenosaires.json",
"lyrics_carlosgardel_lacieguita.json",
"lyrics_carlosgardel_lacumparasita.json",
"lyrics_carlosgardel_lacumparsita.json",
"lyrics_carlosgardel_ladrillo.json",
"lyrics_carlosgardel_laúltimacopa.json",
"lyrics_carlosgardel_lavioleta.json",
"lyrics_carlosgardel_lejanatierramia.json",
"lyrics_carlosgardel_lohanvistoconotra.json",
"lyrics_carlosgardel_madrehayunasola.json",
"lyrics_carlosgardel_madreselva.json",
"lyrics_carlosgardel_malevaje.json",
"lyrics_carlosgardel_manoamano.json",
"lyrics_carlosgardel_manoamanowereeven.json",
"lyrics_carlosgardel_medapenaconfesarlo.json",
"lyrics_carlosgardel_medialuz.json",
"lyrics_carlosgardel_melodíadearrabal.json",
"lyrics_carlosgardel_mibuenosairesquerido.json",
"lyrics_carlosgardel_milongasentimental.json",
"lyrics_carlosgardel_minochetriste.json",
"lyrics_carlosgardel_muñecabrava.json",
"lyrics_carlosgardel_nochedereyes.json",
"lyrics_carlosgardel_padrenuestro.json",
"lyrics_carlosgardel_palomitablanca.json",
"lyrics_carlosgardel_pan.json",
"lyrics_carlosgardel_paseodejulio.json",
"lyrics_carlosgardel_pobregallobataraz.json",
"lyrics_carlosgardel_porunacabeza.json",
"lyrics_carlosgardel_porunacabezafromparfumdefemme.json",
"lyrics_carlosgardel_porunacabezaviolin.json",
"lyrics_carlosgardel_rencor.json",
"lyrics_carlosgardel_rosasdeotoño.json",
"lyrics_carlosgardel_rubiasdenewyork.json",
"lyrics_carlosgardel_secreto.json",
"lyrics_carlosgardel_sigaelcorso.json",
"lyrics_carlosgardel_silbando.json",
"lyrics_carlosgardel_silencio.json",
"lyrics_carlosgardel_sisoyasi.json",
"lyrics_carlosgardel_sisupieraslacumparsita.json",
"lyrics_carlosgardel_soledad.json",
"lyrics_carlosgardel_soltropical.json",
"lyrics_carlosgardel_sueñodejuventud.json",
"lyrics_carlosgardel_susojossecerraron.json",
"lyrics_carlosgardel_tangoargentino.json",
"lyrics_carlosgardel_tangoporunacabeza.json",
"lyrics_carlosgardel_tomoyobligo.json",
"lyrics_carlosgardel_tortazos.json",
"lyrics_carlosgardel_ventarrón.json",
"lyrics_carlosgardel_viejorincón.json",
"lyrics_carlosgardel_viejosmoking.json",
"lyrics_carlosgardel_volver.json",
"lyrics_carlosgardel_volvióunanoche.json",
"lyrics_carlosgardel_yirayira.json"
]

# y = str(artist_keys)
y = str(tounes)

# for y in artist_keys:
for y in tounes:
	# fichier = "rap_" + y + ".csv"
	fichier = "plata_" + y + ".csv"

	file_name = "Lyrics_" + y + ".json"
	file_name = y

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
			# infos.append(data["songs"][i]["artist"])
			infos.append(data["artist"]) ### Petite adaptation nécessaire pour les JSON que j'ai recueillis
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

		# print(data["songs"][i]["artist"])
		print(data["songs"][i]["title"]) ### Autre adaptation dûe aux JSON que j'ai obtenus dans la première étape
		print(len(count))

			#Pour l'instant, le script a encore quelques anomalies, mais j'y travaille très fort. 
			### Oui, ça paraît. Ne lâche pas!