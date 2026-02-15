import plot
import actions


def run_pumpkins():
	water_under_num_coords = 10
	while True:
		planted_coords = plot.traverse_plot(actions.pumpkins, False)
		while (len(planted_coords) > 0):
			should_water = (len(planted_coords) < water_under_num_coords)
			planted_coords = plot.traverse_coordinates(planted_coords,actions.pumpkins, should_water)
		harvest()


def run_hay_carrots_wood():
	while True:
		plot.traverse_plot(actions.hay_wood_carrot)


def clear_harvest():
	plot.traverse_plot(actions.harvest_only)
	clear()
	
	
def run_sunflowers():
	while True:
		sunflower_results = plot.traverse_plot(actions.plant_sunflowers)
		# oorganize sunflowers by measure
		grouped_sunflower_dict = {}
		for i in range(9):
			grouped_sunflower_dict[15 - i] = []
		for sf in sunflower_results:
			grouped_sunflower_dict[sf[0]].append(sf[1])
		for i in range(9):
			plot.traverse_nearest_coordinates(grouped_sunflower_dict[15 - i], actions.harvest_only)
			
	return None


def run_polyculture():
	desired_entity = Entities.Carrot
	active_companion_list = []
	
	param_tuple = (active_companion_list, desired_entity)
	while True:
		plot.traverse_plot(actions.polyculture, param_tuple)
		# placeholder for dynamically calculating the desired entity



def main():
	clear()
	# clear_harvest() 

	# run_hay_carrots_wood()
	# run_sunflowers()
	# run_pumpkins()
	# run_sunflowers()
	run_polyculture()


if __name__ == '__main__':
	main()

