class Scenes(object):
				   
	def __init__(self):
		self.name = 'name'
		
	def startover(self):
		print "Which door do you pick? (1, 2, 3 or 4)"
				   
		choice = int(raw_input("> "))
	
		if choice is 1:
			a_scene[1].room1()
		elif choice is 2:
			a_scene[2].room2()
		elif choice is 3:
			a_scene[3].room3()
		elif choice is 4:
			a_scene[4].room4()
		else:
			print "This is your first adventure, isn't it? Try again.\n"
			self.startover()

			
class Death(Scenes):
	
	def game_over(self):
		print "				I hope you enjoyed my little experiment!				"
		print "				by Tycho Kerstens										"
		
		
class FirstSquare(Scenes):
		
	def room1(self):
		if "VARA" in BACKPACK:
			print "Been here, done that. Lets go back."
			self.startover()
			
		else:
			if "Silver Key" in BACKPACK:
					print "Now that you have the key you manage to unlock the door.\n"
					print "This room is bigger than the other rooms so far, you explore the far back."
					a_scene[5].room5()
					
			else: 
					print "The door is locked. You go back\n"
					self.startover()
			
class GoblinRoom(Scenes):
	
	def room2(self):
		if "Silver Key" in BACKPACK:
			print "Oh yeah. I already explored this room. Lets go back.\n"
			
		else:
			print """
			You enter the second door on the right. 
			When you look around the room you notice two red eyes glowing in the dark..
			Before you are allowed to react the creature leaps in front of you!
			A nasty looking goblin looks at you.
			Fight or Flee?
			"""
		
		choice = raw_input("> ")
		
		if choice == "Fight":
			print "\nYou have an intense battle with the goblin, you kill him but lost 8 hp.\n"
			
			print "Now that the goblin is dead, you loot his corpse and find a Silver Key!"
			print "Nothing else in this room. Might as well go back.\n"
			Key = "Silver Key"
			BACKPACK.append(Key)
			self.startover()

		elif choice == "Flee":
			print "You managed to run out of the door and close it before you could get hit..."
			print "It did look like he was guarding or protecting something of value.\n"
			self.startover()
			
		else:
			print "The goblin punches you out of the room. That hurt! You lose 2 hp.\n"
			self.startover()


class TrapRoom(Scenes):
	
	def room3(self):
		if "BARA" in BACKPACK:
			print "You've already got where you came for in this room.\n"
		
		else:
			print """
			You enter the third room from the right.
			Once inside, you smell a feint, musky odor...
			Do you enter? (Yes or No)"
			"""
	
			choice = raw_input("> ")
	
			if choice == "Yes":
				print """
				Brave, or stupid, you enter the room. You hear a 'click' sound to the right.
				This can mean only one thing!! Trap!!"
				Quick! Duck or Jump?
				"""
		
				move = raw_input("> ")
		
				if move == "Duck":
					print """
					Arrows shoot over your head, missing you by an inch...
					As you thank god for your quick wits, you look around the room...
					You see an altar at the southern wall.
					Upon taking a closer look, you see words etched in the altar:
				
					"The first part of HIS name is 'BARA'..."
				
					Nothing else of value seems to be in this room. You go back."
					"""
					word1 = "BARA"
					BACKPACK.append(word1)
					self.startover()
					
				else:
					print "You jump, lining your head perfectly with the volley of poisonous arrows of death +10."
					print "Yep, You've guessed it. You die!"
					a_scene[0].game_over()
				
			elif choice == "No":
				print "Sure, the only way to explore this cave and take it's powers is by... not exploring! Wait...\n"
				print "Try again."
				self.startover()
				
			else:
				print "Wut...?"
				a_scene[2].room3


class PotionRoom(Scenes):	

	def room4(self):
		if "HP_potion" or "No_potion" not in BACKPACK:
			print """
			You enter the room utmost to your left.
			Inside a rare tranquillity greets you. 
			In the exact middle of the room stands a chest on a small pedestal.
			As you take a closer look you see the chest is open.
			In it appears to be a potion of some sort, with red fluid. On it the two letters \n'HP' are written.
			Do you take the potion? (Yes?)
			"""
	
			choice = raw_input("> ")
	
			if choice == "Yes":
				print "You put the potion in your trusty backpack.\n"
				potion = "HP_potion"
				BACKPACK.append(potion)
				
			else:
				print "You take the potion. You typed yes didn't you?"
				print "No? Oh. Well. Your loss.\n"
				potion2 = "No_potion"
				BACKPACK.append(potion2)
		
			print "You already have the potion so..."
			print "You see a door to your left and straight ahead."
			print "Which door do you take? Or do you want to go back? (Left, Ahead or Back?)"
	
			choice2 = raw_input("> ")
	
			if choice2 == "Left":
				print "You take the door to your right."
				self.room7()
				
			elif choice2 == "Ahead":
				print "You take the door straight ahead of you.\n"
				
				if "BARA" and "VARA" not in BACKPACK:
					print "Something doesn't feel right..., you have the feeling to explore the other rooms first.\n"
					start()
				else:
					self.room6()
					
			else:
				print "You go all the way back."
				self.startover()
		else:
			print "You see a door to your left and straight ahead."
			print "Which door do you take? Or do you want to go back? (Left, Ahead or Back?)"
	
			choice2 = raw_input("> ")
	
			if choice2 == "Left":
				print "You take the door to your right."
				self.room7()
				
			elif choice2 == "Ahead":
				print "You take the door straight ahead of you.\n"
				
				if "BARA" and "VARA" not in BACKPACK:
					print "Something doesn't feel right..., you have the feeling to explore the other rooms first.\n"
					self.startover()
				else:
					self.room6()
					
			else:
				print "You go all the way back."
				self.startover()			
	

class SecondSquare(Scenes):

	def room5(self):
		print """
		As you explore the far back of the room, you notice a lever muffled away under some overgrowth.
		You manage to cut the overgrowth and pull the lever. 
		The moment you think you are going to die because you didn't check for traps,
		an altar seem to raise from the ground.
		In raising, it reveals a stone slab on it encarved:
	
		"The second part of HIS name is 'VARA'"
	
		Eerily, as soon as you read the words the slab descends into the ground again,
		as if it knew you were done reading.
		You decide to go back to the beginning and explore some more.
		"""
		word2 = "VARA"
		BACKPACK.append(word2)
	
		self.startover()


class Gargoyle_Room(Scenes):		
	
	def room6(self):
		if "Switched" in BACKPACK:
			print """
			The gargoyles remain silent.
			In the back of the great hall, you notice where once was a wall, 
			now a giant door has opened. We are getting closer.
			It's getting colder... and darker...
			Yes... we are definitely getting closer.
			Hurray?
			"""
		
			self.room8()
	
		elif "Lever" in BACKPACK:
			print "We are done here for now. Lets go back."
			self.room4()
			
		else:
			print """
			You enter a great hall, carved white stone everywhere.
			Every inch of wall seems to be covered in demonic writings.
			At the top of each supporting pillars is a darkblack gargoyle staring into your soul.
			They all seem to look directly at you even though they are face towards eachother.
			This is probably one of those moments where you will regret becoming an adventurer...
			Going back is no option though. You are either going home a rich and powerful man, 
			or you are not going home at all.
			As you move through half of the hall, 
			you here rocks grinding and suddenly four deafening screeches 
			makes you fall to the ground in agony.
			Standing up, you see 4 gargoyles surrounding you.
			What do you do? (Fight, Flee or Insight?)
			"""
	
			choice = raw_input("> ")
	
			if choice == "Fight":
				print """
				You try to fight the gargoyles.
				GARGOYLES...
				FOUR. GARGOYLES.
				Yeah. You are ripped to pieces. 
				Luckily it was a quick death!
				"""
		
				self.game_over()
				
			elif choice == "Flee":
				print """
				You try to turn around and flee.
				Even though you give it a valiant effort,
				these things can fly, and they had surrounded you.
				You knock one away and make for the door.
				For a moment you almost think you made it.
				A hand grasps your foot and drags you back into the great hall.
				The gargoyles pick you apart piece by piece. You die.
				"""
		
				self.game_over()
				
			elif choice == "Insight":
				print """
				Hopeless as this situation might look.
				You stand your ground. Fearless. 
				Your name isn't Alexander Hakomoto because you aren't afraid
				to kick people you are arresting at casino's.
				The moment the gargoyles lunge at you something inside you 
				tells you to utter the following words:
				BARAVARA!!! It echoes through the great hall.
				The gargoyles suddenly stop. 
				They move back to their spots on top of the pillars and resume their eternal sleep.
				At the end of the hall lies a loose lever. You take it.
				You explore the rest of the hall, but nothing else seems here.
				You go back to the previous room.
				"""
		
				thingy = "Lever"
				BACKPACK.append(thingy)
				self.room4()


class LeverRoom(Scenes): 				

	def room7(self):
		if "Lever" in BACKPACK:
			print """
			After 10 minutes of walking you enter a room.
			In the middle of this room is a switch with it's lever missing...
			You decide to see if your lever fits. 
			It does! You turn the lever. 
			This must've done... Something..
			You turn back.
			"""
		
			switch_on = "Switched"
			BACKPACK.append(switch_on)
			self.room4()
			
		elif "Switch" in BACKPACK:
			print "Well we now what's here. We need to find a lever."
			self.room4()
			
		else:
			print """
			As you enter the door to your left, you walk a long small corridor.
			It seems endless, but after a good 10 minutes you enter a small room.
			In the middle of the room sits a device.
			You have seen the device before: a same device was used to raise the slab containing "VARA"
			The actual lever is missing.
			You go back.
			"""
		
			switch = "Switch"
			BACKPACK.append(switch)
			self.room4()


class ThirdSquare(Scenes):

	def room8(self):
		print """
		It's getting even colder. It's getting even darker.
		This. Does. Not. Feel. Good.
		Yet, you seem drawn towards what's next. 
		The more you realize power lurks nearby, the less the cold seems to bother you.
		As you move trough the room a sharp pain knocks you onto your knees.
	
		"THE THIRD PART OF HIS NAME IS 'SVARRA'... 
		ARE YOU SURE YOU ARE READY FOR THIS, MORTAL!!!?"
	
		A door opens before you.
		Do you enter, or get the HELL out of dodge? (Enter, Dodge)
		""" 
	
		choice = raw_input("> ")
		if choice == "Enter":
			print """
			You don't care. You want it. It's all you've ever wanted.
			Go back now? Go home? HOME?! POWERLESS??? NEVER!!!!
			"""
			
			self.room9()
			
		elif choice == "Dodge": 
			print """
			Wait. This is insane. 
			I am going to face a demon lord by myself? 
			I will unleash it's power over the world, through me?
			Hell no. What was I thinking. Lets get the hell out of here.
			You return home. 
			Slowly you'll forget what ever happened back there.
			Lets hope nobody else is stupid enough to venture inside this cave.
			Maybe... Maybe I should've sealed it...
			"""
			
			self.game_over()
			
		else:
			print """
			Hearing the dark lords voice through your head was too much.
			Yes you wanted power, yes you wanted riches.
			But this. This is.... This is....
			You feel your arteries drying up.
			You try to move, but it's too late. As you reach down to see you notice
			your legs all the way up to your feet have turned to stone.
			You should've listened. You should've never entered.
			"MUHAHAHAHA..." is the last you hear until you slip into an eternal stasis..
			"""
			
			self.game_over()

class FinalRoom(Scenes):
		
	def room9(self):
		print """
		You enter the room. Your hands and other extremities immediately begin to freeze.
		This is it, your future. The power that is rightfully yours.
		A dark loud voice speaks:
		"HELL MORTAL. I HAVE BEEN WAITING FOR YOU."
		"SEE, I WAS TRAPPED HERE ONES. BETRAYED BY MY BROTHER ANGEL TYREAL AEONS AGO."
		"FOR MILLENNIA I HAVE BEEN GATHERING THE SOULS OF THE STUPID, THE POWERHUNGRY."
		"I HAVE BEEN CRAVING FOR MY RETURN. AND YOUR SOUL. YOUR SOUL SHALL BE THE LAST ONE I NEED."
		"TYREAL MIGHT HAVE SAVED HUMANITY BACK THEN. BUT I LIKE TO THINK HUMANITY AND THEIR POWERHUNGRY,
		CURIOUS NATURE WILL INEVITABLY STILL DESTROY YOU."
		Shit. How could you have been so easy? Was I that eager to trap?
		But wait! "I know your full name demon! I SHALLT DESTROY YOU"
		The dark loud voice continues: "DO YOU NOW? I HAVE PURPOSELY LET YOU KNOW THE FIRST THREE PARTS"
		"THE FOURTH PART IS NOT KNOW TO MAN. HAHAHA YOU PETTY INSECTS ARE SO PREDICTABLE."
		Damn. He called our bluff. It was all a setup... Well, I might as well try a random fourth part...
		One try is all I've got before he absorbs my soul.
		"Silly demon! I know your full name. I MIGHT NOT GET YOUR POWERS, BUT I WILL GO INTO HISTORY AS,
		ALEXANDER HAKOMOTO, SAVIOR OF MANKIND"
		You utter the following name, praying to god it is the right one.
		"BARAVARASVARRABRADPITT"
		.........................
		.........................
		The dark loud voice shivers:
		"WHAT.. BUT...HOW?! HOW DID YOU..."
		An explosion follows, the demon lord obviously in pain.
		"I NEVER SHOULD HAVE DONE THAT MOVIE FIGHT CLUB. AAARGHJJ"
		"THE MONEY WAS SO GOOD THOUGH! AAAAAAAAH!"
		The last scream slowly fainted into oblivion.
		You did it....
		You've...
		You've won.
		or did you?
		"""
	
		self.game_over()

a_scene = [Death(),
		   FirstSquare(),
		   GoblinRoom(),
		   TrapRoom(),
		   PotionRoom(),
		   SecondSquare(),
		   Gargoyle_Room(),
		   LeverRoom(),
		   ThirdSquare(),
		   FinalRoom()]
			   

print """
	You enter a gloomy cave. 
	Your research leads you to believe that herein lies the remains of a dark lord who ruled ages ago.
	Many adventurers talked of the great riches and powers the ones
	who are brave enough to venture through brought back.
	Only... nobody has ever returned. 
	Oh well! More riches and powers for you, right?
	You enter the cave...
	You see four doors before you:
	"""

print "You have 20 HP and a BACKPACK.\n"

HP = 20
BACKPACK = []

death = Death()
game = Scenes()
game.startover()