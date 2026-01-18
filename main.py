import plot
import actions

clear()

def run_pumpkins():
	while True:
		planted_coords = []
		continue_planting = True
		
		while continue_planting:
			if planted_coords:
				planted_coords = plot.traverse_coordinates(planted_coords,actions.pumpkins)
			else:
				planted_coords = plot.traverse_plot(actions.pumpkins)
			continue_planting = (len(planted_coords) > 0)
		harvest()


def run_hay_carrots_wood():
	while True:
		plot.traverse_plot(actions.hay_wood_carrot)


if __name__ == '__main__':
	# run_hay_carrots_wood()
	run_pumpkins()
	
