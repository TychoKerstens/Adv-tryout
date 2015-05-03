class Room1(object):
	
	directions = {
		'east': 'room2'
	}
	
	def enter(self):
		print "Hi."
	
class Room2(object):
	
	def enter(self):
		print "Hello."
		
		
class Room(object):
	
	rooms = {
		'room1': Room1(),
		'room2': Room2()
	}
	
	def __init__(self, room_name):
		self.room_name = room_name
	
	def start_end(self):
		current_room = Room1()
		last_room = self.room_name.next_room('room2')
			
		while current_room != last_room:
			current_room.enter()
			print current_room.directions
			choice = raw_input("> ")
			current_room = current_room.directions[choice]
			current_room = self.rooms[current_room]
			
			
class Player(object):

    def __init__(self, HP, armor, damage):
		self.HP = HP
		self.armor = armor
		self.damage = damage
		
    def player_stat(self):
		if self.HP >= 10:
			print "You survived. You have %d HP left." % self.HP
		elif self.HP > 0:
			print "You have %d HP left, you survived but you are pretty wounded!" % self.HP
		elif self.HP <= 0:
			print "You have died. Game over."
		
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

	def see_backpack(self):
		print Backpack
		print "What item do you want to inspect?"
		see = raw_input("> ")
		
		if see in Backpack:
			print Backpack[see]
			print "Do you want to equip this item?"
			equip = raw_input("> ")
			if equip == "Yes":
				Player.damage = self.damage
				Player.armor = self.armor
			else:
				print "Okidoki."
				
		else:
			print "That item is not in your backpack."
			self.see_backpack

		
def fighting(Monster, Player):
	while Monster.monster_defeated() == False and Player.player_defeated() == False:
		
		player_hit = Player.damage - Monster.armor
		monster_hit = Monster.damage - Player.armor
		print "You hit the monster for %d damage." % player_hit
		Monster.HP -= player_hit
		print "Monster has %d HP left" % Monster.HP
		raw_input("> ")
		
		if Monster.monster_defeated() == True:
			print "The monster is defeated!"
			break
			
		print "Monster strikes back dealing %d damage." % monster_hit
		Player.HP -= monster_hit
		print "You have %d HP left." % Player.HP
		raw_input("> ")
		
		if Player.player_defeated() == True:
			print "You have been defeated"
		#exit(0) for 
		

class UserInterface(object):
	pass 
	
	
class Maps(object):
	
	rooms = {
		'room1': Room1(),
	    'room2': Room2()
	}
	
	def __init__(self, first_room):
		self.first_room = first_room
		
	def next_room(self, room_name):
		room = Maps.rooms.get(room_name)
		return room
	
	def first_room(self):
		return self.next_room(self.first_room)
		
Backpack = {}
#Backpack[Equipment.key] = Equipment.descript				
			
#fire_axe = Equipment('fire_axe', 
					#'This fine work of magical crafting from dwarven origins smells and looks like molten magma',
                    #0, 6)
#fire_axe.see_backpack()

begin = Maps('room1')
start = Room(begin)
start.start_end()

#while True:
	
	#print starting_room.description
	#choice = raw_input("> ")
	#choice = choice.lower()
	
	#if starting_room.has_exit_to(choice):
		#starting_room.moveto(choice)
	#else:
		#print "room does not exist."
		


