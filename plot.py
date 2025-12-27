def traverse_plot(action):
	result_list = []
	for y in range(get_world_size()):
		for x in range(get_world_size()):
			result = action()
			if result:
				result_list.append(result)
			move(East)
		move(North)
	return result_list