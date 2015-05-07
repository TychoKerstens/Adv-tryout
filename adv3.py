class Room1(object):
	
	directions = {
		'east': 'room2'
	}
	
	def enter(self):
		print "Hi."
		Player.visited_rooms.append(self)
		#Haven't foud a way to have this work yet:
		#Player.visited_room()
		
		
class Room2(object):
	
	directions = {
		'west': 'room1'
	}
	
	def enter(self):
		print "Hello."
		Player.visited_rooms.append(self)
		#Player.visited_room()
		
class Room(object):
	
	rooms = {
		'room1': Room1(),
		'room2': Room2()
	}
	
	def __init__(self, current_room, last_room):
		self.current_room = current_room
		self.last_room = last_room
	
	def start_end(self):
		while self.current_room != self.last_room:
			
			if self.current_room in Player.visited_rooms:
				print Prints.room_prints[0]
				print self.current_room.directions
				choice = raw_input("> ")
				if choice in self.current_room.directions:
					self.current_room = self.current_room.directions[choice]
					self.current_room = self.rooms[self.current_room]
				else:
					print Prints.room_prints[1]
			else:
				self.current_room.enter()

#For all the raw inputs, haven't made this working yet:
#class UserInterface(object):
	
	#def input(self):
		#raw_input("> ")

class Calcs(object):

	def player_hit(self):
		hit = Player.damage - Monster.armor
		return hit
		
	def monster_hit(self):
		hit = Monster.damage - Player.armor
		return hit
	
	def Monster_HP(self):
		Monster.hp -= player_hit
		
	def Player_HP(self):	
		Player.HP -= monster_hit
		
		
class Prints(object):
	
	general_prints = ["Okidoki.",
					  "You have been defeated"]
	
	room_prints = ["You have explored this room, lets move on.",
				   "You can't go here. Try again"]
	
	equip_prints = ["What item do you want to inspect?",
					"Do you want to equip this item?",
					"That item is not in your backpack."]
	
	combat_prints = ["You hit the monster for %d damage.",
	                 "Monster has %d HP left",
					 "The monster is defeated!",
					 "Monster strikes back dealing %d damage.",
					 "You have %d HP left."]
					
	def player_stat(self):
		if Player.HP >= 10:
			print "You survived. You have %d HP left." % self.HP
		elif Player.HP > 0:
			print "You have %d HP left, you survived but you are pretty wounded!" % self.HP
		elif Player.HP <= 0:
			print "You have died. Game over."
	

class Player(object):
	
	backpack = {}
	visited_rooms = []
	
	def __init__(self, HP, armor, damage):
		self.HP = HP
		self.armor = armor
		self.damage = damage
	
	#def visited_room(self):
		#visited_rooms.append(Room.current_room)
		
	def player_defeated(self):
		if self.HP <= 0:
			return True
		else:
			return False
			
			
class Monster(object):

	def __init__(self, HP, armor, damage):
		self.HP = HP
		self.armor = armor
		self.damage = damage
		
	def monster_defeated(self):
		if self.HP <= 0:
			return True
		else:
			return False



class Equipment(object):

	def __init__(self, key, descript, armor, damage):
		self.key = key
		self.descript = descript
		self.armor = armor
		self.damage = damage
		
		Player.backpack[self.key] = self.descript
		
	def see_backpack(self):
		print Prints.equip_prints[0]
		see = raw_input("> ")
		
		if see in Player.backpack:
			print Player.backpack[see]
			print Prints.equip_prints[1]
			equip = raw_input("> ")
			if equip == "yes":
				Player.damage = self.damage
				Player.armor = self.armor
			else:
				print Prints.general_prints[0]
				
		else:
			print Prints.equip_prints[2]
			self.see_backpack

		
def fighting(Monster, Player):
	while Monster.monster_defeated() == False and Player.player_defeated() == False:
		
		#I broke fighting, when called Calcs.player_hit() gives a TypeError:
		#"Unbound method player_hit() must be called with Calcs instance as first argument (got nothing instead)"
		#Same goes for Calcs.Monster_HP() and the rest.
		#I will try and find a way to make the formats go into the Calcs function
		print  Prints.combat_prints[0] % Calcs.player_hit()
		Calcs.Monster_HP()
		print  Prints.combat_prints[1] % Monster.HP
		raw_input("> ")
		
		if Monster.monster_defeated() == True:
			print Player.combat_prints[2]
			break
			
		print  Prints.combat_prints[3] % Calcs.monster_hit()
		Calcs.Player_HP()
		print  Prints.combat_prints[4] % Player.HP
		raw_input("> ")
		
		if Player.player_defeated() == True:
			print Prints.general_prints[1]
		#exit(0) for 
		

	
adventurer = Player(20, 1, 3)
orc = Monster(8, 1, 2)	
start = Room(Room1(), Room2())
start.start_end()

#while True:
	
	#print starting_room.description
	#choice = raw_input("> ")
	#choice = choice.lower()
	
	#if starting_room.has_exit_to(choice):
		#starting_room.moveto(choice)
	#else:
		#print "room does not exist."
		


