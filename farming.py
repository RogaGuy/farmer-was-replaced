# STATIC VARIABLES
GRASSLAND_ENTITIES = [Entities.Grass, Entities.Bush, Entities.Tree]


def plant_till_and_water(entity, should_water=False, water_below=.25, water_to=.7):
	if water_to > 1:
		water_to = 1
	if water_below >= 1:
		water_below = .7

	desired_ground = Grounds.Grassland
	if entity not in GRASSLAND_ENTITIES:
		desired_ground = Grounds.Soil
		
	if get_ground_type() != desired_ground:
		till()
		
	plant_status = None
	if entity != Entities.Grass:
		plant_status = plant(entity)
	
	if should_water and get_water() < water_below and not can_harvest():
		while get_water() <= water_to and num_items(Items.Water) > 0:
			use_item(Items.Water)
	return (plant_status or entity == Entities.Grass)


def harvest_if_able():
	if can_harvest():
		return harvest()
	return False