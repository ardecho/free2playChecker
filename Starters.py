#!/usr/bin/env python
from RiotAPI import RiotAPI
import RiotConsts as Consts

CHNAME = Consts.CHNAME
#sn = raw_input("Write ur summoner name\n")
#sn = 'plxardecho'
#platform = raw_input("eune, euw\n")
count = 0
champion_list = []
l=[]
champsID = []


def summonerNameStart():				#pobiera dane na temat summonera po jego nazwie
	sn = raw_input("Write ur summoner name\n")
	api = RiotAPI('RGAPI-6f7cd083-fda1-4ff4-8b0e-3427f51df8f4')
	r = api.get_summoner_by_name(sn)
	summID = r[sn]['id']
	print r[sn]['id']
	print r[sn]['name']
	print r[sn]['summonerLevel']
	return summID
	


def championListStart(champion_list):
	api = RiotAPI('RGAPI-6f7cd083-fda1-4ff4-8b0e-3427f51df8f4')
	ch = api.get_champions()							 # wykozystywane do pobrania listy champow z champion
	count = 0
	while True:
		champion_list.append({"CHAMPION ID: ": ch["champions"][count]["id"], "FREE TO PLAY? : ": ch["champions"][count]["freeToPlay"]}) #1 
		count += 1
		if count == 133:
			#print champion_list
			#print ch
			return champion_list
			break
	
def championByIDStart(champ_ID,l):								#pobiera dane o championie z api po ID i zwraca liste z nazwa/nazwami
	api = RiotAPI('RGAPI-6f7cd083-fda1-4ff4-8b0e-3427f51df8f4')
	chid = api.get_champion_by_id(champ_ID)
	#l.append(chid["name"])
	print chid
	#print chid["name"]
	#print chid["title"]
	#return l



#-----------------------------------------Data Processing metods-----------------------------------------------







def F2PchampionPool(champion_list): 							# zwraca liste free to play champow i inicjujac championByIDStart wyszukuje ich dane z api
	"""Zadziala tylko jesli wykonane championListStart()""" 
	free_to_play_champs = []
	IDchampsList = []
	for x in champion_list:
		if x["FREE TO PLAY? : "] == True:
			free_to_play_champs.append(x)
	for x in free_to_play_champs:
		IDchampsList.append(x["CHAMPION ID: "])
	for x in IDchampsList:
		championByIDStart(x,l)	

def IDchampionPool(champion_list,champsID):						#zwraca liste ID champow i inicjujac championByIDStart wyszukuje ich dane z api
	"""Zadziala tylko jesli wykonane championListStart()"""
	for x in champion_list:
		champsID.append(x["CHAMPION ID: "])
	return champsID
	#for x in champsID:
	#	championByIDStart(x,l)


def F2PIDchampionPool(champion_list,champsID):						#zwraca liste ID dla free championow
	"""Zadziala tylko jesli wykonane championListStart()"""
	free_to_play_champs = []
	for x in champion_list:
		if x["FREE TO PLAY? : "] == True:
			free_to_play_champs.append(x)
	for x in free_to_play_champs:
		champsID.append(x["CHAMPION ID: "])
	return champsID

def SearchChampByID(CHNAME,champsID,l): 		# zwraca liste champow za pomoca ID champa
	"""Zadziala jesli wykonano F2PIDchampionPool"""
	for x in champsID:
		for key, value in CHNAME.items():
			if x==key:
				l.append(CHNAME[key])
	return l
	
	
def SearchChampByIDinChampionList(CHNAME,champsID,l): 		# zwraca liste champow za pomoca ID champa
	"""Zadziala jesli wykonano F2PIDchampionPool"""
	for x in champsID:
		for key, value in CHNAME.items():
			if x==key:
				l.append(x[key])
	print l
	return l
	

def SearchChampByIDx(CHNAME,champsID,l): 		# zwraca liste champow za pomoca ID champa
	"""Zadziala jesli wykonano F2PIDchampionPool"""
	for x in champsID:
		for key, value in CHNAME.items():
			if x==key:
				l.append(x)
				l.append(CHNAME[key])

	print champsID
	print l
	return l
