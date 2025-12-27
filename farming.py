
def plant_till_and_water(entity, should_water=False, water_below=.25, water_to=.7):
	if water_to > 1:
		water_to = 1
	if water_below >= 1:
		water_below = .7

	desired_ground = Grounds.Grassland
	if entity in [Entities.Carrot, Entities.Pumpkin]:
		desired_ground = Grounds.Soil
		
	if get_ground_type() != desired_ground:
		till()
	plant_status = plant(entity)
	
	if should_water and get_water() < water_below:
		while get_water() <= water_to:
			use_item(Items.Water)
	return plant_status
	
	
	