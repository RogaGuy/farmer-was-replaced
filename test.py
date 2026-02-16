import plot 
import farming

def test_cacti():
	clear()
	values = []
	for i in range(get_world_size()):
		farming.plant_till_and_water(Entities.Cactus, False)		
		values.append(measure())
		move(East)
	quick_print("Unsorted values: " + str(values))
	
	plot.sort_axis(True)
	
	for i in range(get_world_size()):
		farming.plant_till_and_water(Entities.Cactus, False)		
		values.append(measure())
		move(East)
	quick_print("Sorted values? = " + str(values))


if __name__ == '__main__':
	test_cacti()
