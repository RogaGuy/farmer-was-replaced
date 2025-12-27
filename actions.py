import farming


def trees_and_carrots():
	x_pos = get_pos_x()
	y_pos = get_pos_y()
	
	# harvesting
	if can_harvest():
		harvest()
	
	# planting new crop
	if (x_pos + y_pos) % 2 == 1:
		farming.plant_till_and_water(Entities.Tree, True)
	else:
		farming.plant_till_and_water(Entities.Carrot, True)


def pumpkins():
	while not (can_harvest() or get_entity_type() in [None, Entities.Dead_Pumpkin]):
		do_a_flip()
		
	if farming.plant_till_and_water(Entities.Pumpkin, True):
		return (get_pos_x(), get_pos_y())
	return None
