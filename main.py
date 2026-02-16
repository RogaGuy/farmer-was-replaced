import plot
import actions


def run_pumpkins():
	clear()
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


def run_cacti():
	clear()
	while True:
		plot.traverse_plot(actions.plant_cacti)
		# when adding while loop, make sure to start on 0,0
		num_swaps = 99
		total_swaps = 0
		
		# while num_swaps > 0:
		#	num_swaps = 0 # reset num_swaps to 0
		for axis in range(2):
			is_x_axis = (axis == 0)
			for i in range(get_world_size()):
				if is_x_axis:
					plot.move_to_coordinate(0, i)
				else:
					plot.move_to_coordinate(i, 0)
					
				num_swaps += plot.sort_axis(is_x_axis)
		total_swaps += num_swaps
		error_list = plot.traverse_plot(actions.find_cacti_errors)
		quick_print("Sorted x and y axis with " + str(num_swaps) + " swaps.")
		quick_print("Finished in " + str(total_swaps) + " swaps!")
		
		harvest()
		# clear() # just in case something went wrong. . .append
		
		# uncomment for debugging
		#if error_list:
			#quick_print("Sorting errors found!: " + str(len(error_list)))
			
	

def main():
	clear()
	# clear_harvest() 

	# run_hay_carrots_wood()
	# run_sunflowers()
	# run_pumpkins()
	# run_sunflowers()
	# run_polyculture()
	run_cacti()


if __name__ == '__main__':
	main()

