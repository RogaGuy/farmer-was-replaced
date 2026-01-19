import plot
import actions


def run_pumpkins():
	water_under_num_coords = 10
	
	while True:
		planted_coords = []
		continue_planting = True
		
		while continue_planting:
			if planted_coords:
				should_water = (len(planted_coords) < water_under_num_coords)
				planted_coords = plot.traverse_coordinates(planted_coords,actions.pumpkins, should_water)
			else:
				
				planted_coords = plot.traverse_plot(actions.pumpkins, False)
			continue_planting = (len(planted_coords) > 0)
		harvest()


def run_hay_carrots_wood():
	while True:
		plot.traverse_plot(actions.hay_wood_carrot)


def clear_harvest():
	plot.traverse_plot(actions.harvest_only)
	clear()
	
	
def run_sunflowers():
	sunflower_results = plot.traverse_plot(actions.plant_sunflowers)
	
	# oorganize sunflowers by measure
	grouped_sunflower_dict = {}
	for i in range(9):
		grouped_sunflower_dict[15 - i] = []
	
	for sf in sunflower_results:
		grouped_sunflower_dict[sf[0]].append(sf[1])
	
	for i in range(9):
		plot.traverse_coordinates(grouped_sunflower_dict[15 - i], actions.harvest_only)
	
	return None



def main():
	clear()
	# clear_harvest() 
	
	while True:
		run_sunflowers()
		
	# run_hay_carrots_wood()
	# run_pumpkins()
	# run_sunflowers()


if __name__ == '__main__':
	main()

