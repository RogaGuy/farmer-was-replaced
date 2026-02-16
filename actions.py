import farming


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


def plant_sunflowers(param):
	# param is unused
	plant_status = farming.plant_till_and_water(Entities.Sunflower, True)
	if plant_status:
		plant_measure = measure()
		return (plant_measure, (get_pos_x(), get_pos_y()))
	return None


def harvest_only(param):
	return farming.harvest_if_able()
	# param is unused


def polyculture(polyculture_tuple):
	# 2 tasks:
		# 1 - harvest what's under us
		# 2 - update companion list if needed
		# 3 - determine what to plant, and plant it
	active_companion_list, desired_entity = polyculture_tuple
	
	current_coord = (get_pos_x(), get_pos_y())
	sensed_entity = get_entity_type()
	harvest_status = farming.harvest_if_able()
	
	if (not harvest_status) and sensed_entity:
		return None
	
	for c in active_companion_list:
		if c["src_coord"] == current_coord:
			active_companion_list.remove(c)
			break
		
	found_companion = False
	for c in active_companion_list:
		if c["companion_coord"] == current_coord:
			farming.plant_till_and_water(c["entity"], True)
			found_companion = True
			break
			
	if not found_companion:
		farming.plant_till_and_water(desired_entity, True)
		
	c_ent, c_coord = get_companion()
	active_companion_list.append({
		"src_coord": current_coord,
		"companion_coord": c_coord,
		"entity": c_ent
	})	

	
def plant_cacti(param):
	return farming.plant_till_and_water(Entities.Cactus, True)
	

def find_cacti_errors(param): # return True if sorting error, else False
	found_error = False 
	if get_pos_y() < get_world_size() -1:
		if measure() > measure(North):
			found_error = True
	if get_pos_x() < get_world_size() - 1:
		if measure() > measure(East):
			found_error = True
	return found_error
