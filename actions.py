import farming

# TODO: probably delete this
def trees_and_carrots(param):
	# param is unused, but actions need to handle an optional parameter
	x_pos = get_pos_x()
	y_pos = get_pos_y()
	
	# harvesting
	if can_harvest():
		harvest()
	
	# planting new crop
	if (x_pos + y_pos) % 2 == 1:
		farming.plant_till_and_water(Entities.Tree, False)
	else:
		farming.plant_till_and_water(Entities.Carrot, False)
	return None


def pumpkins(should_water):
	# should_water is a boolean that determines if a pumpkin square should be watered
	
	# TODO: use fertilizer if parameter passed
	
	while not (can_harvest() or get_entity_type() in [None, Entities.Dead_Pumpkin]):
		do_a_flip()
	
	if farming.plant_till_and_water(Entities.Pumpkin, should_water):
		return (get_pos_x(), get_pos_y())
	return None


def hay_wood_carrot(param):
	# param is unused, but actions need to handle an optional parameter
	x_pos = get_pos_x()
	y_pos = get_pos_y()
	
	# harvesting
	if can_harvest():
		harvest()
	
	# planting new crop
	if (x_pos + y_pos) % 2 == 1:
		farming.plant_till_and_water(Entities.Tree, False)
	elif y_pos >= get_world_size() / 2:
		farming.plant_till_and_water(Entities.Carrot, False)
	else:
		farming.plant_till_and_water(Entities.Grass, False)
	return None


# TODO: can probably be deleted
def hay_carrots(param):
	# param is unused, but actions need to handle an optional parameter
	
	# harvesting
	if can_harvest():
		harvest()

	if get_pos_y() >= get_world_size() / 2:
		farming.plant_till_and_water(Entities.Carrot, False)
	else:
		farming.plant_till_and_water(Entities.Grass, False)


def plant_sunflowers(param):
	# param is unused
	plant_status = farming.plant_till_and_water(Entities.Sunflower, False)
	if plant_status:
		plant_measure = measure()
		return (plant_measure, (get_pos_x(), get_pos_y()))


def harvest_only(param):
	# param is unused
	harvest()


def polyculture(current_companions):
	current_x = get_pos_x()
	current_y = get_pos_y()
	current_coord = (current_x, current_y)
	
	desired_entity = Entities.Grass
	harvest_result = farming.harvest_if_able()

	remove_index = None
	for companion in current_companions:
	# for c in range(len(current_companions)):
		source_coord, companion_coord, companion_entity = companion
		src_x, src_y = source_coord
		cmp_x, cmp_y = companion_coord

		if harvest_result:
			if (current_x == src_x and current_y == src_y):
				current_companions.remove(companion)

		if cmp_x == current_x and cmp_y == current_y:
			desired_entity = companion_entity

	should_water = (desired_entity == Entities.Tree)
	plant_status = farming.plant_till_and_water(desired_entity, should_water)
	if plant_status:
		companion = get_companion()
		if companion:
			companion_entity, companion_coord = companion
			return (current_coord, companion_coord, companion_entity)
		return None

	else:
		quick_print("unable to print " + str(desired_entity) + " on ground " + str(get_ground_type()))
		return None

	