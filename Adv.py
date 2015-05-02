def new_adventure(Name, gender, race, choice):
	print "So your name is %r?\n" % name
	print "And your gender is %r?\n" % gender
	print "And you are a %r? Haven't seen one of you in a while!\n" % race
	print "A %r?! Excellent! We are in short supply of your talents\n" % choice

print "Hello adventurer! What is your name?\n"
name = raw_input("> ")
print "What is your gender?\n"
gender = raw_input("> ")
print "What is your race?\n"
race = raw_input("> ")
print "We are in need of a warrior, a wizard or a cleric, what do you choose to become?\n"
choice = raw_input("> ")

new_adventure(name, gender, race, choice)
