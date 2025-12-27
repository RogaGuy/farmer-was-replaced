clear()

# setup
for y in range(get_world_size()):
	for x in range(get_world_size()):
		till()
		move(East)
	move(North)

# begin farming and don't stop
while True:
	for y in range(get_world_size()):
		for x in range(get_world_size()):
			# harvest if able
			if can_harvest():
				harvest()
				
			# planting the next crop
			if (x + y) % 2 == 1:
				# grid position: plant a tree
				plant(Entities.Tree)
			else:
				plant(Entities.Carrot)
				
			# elif y <= 1:
			# 	plant(Entities.Carrot)
			# else:
			#	plant(Entities.Bush)
			
			move(East)
		move(North)
	