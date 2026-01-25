def traverse_plot(action, action_param=None):
	result_list = []
	for y in range(get_world_size()):
		for x in range(get_world_size()):
			action_result = action(action_param)
			if action_result:
				result_list.append(action_result)
			move(East)
		move(North)
	return result_list

	
def traverse_coordinates(coordinate_list, action, action_param=None):
	# coordinate list will be a list of tuples (x_cord, y_cord)
	# TODO: optptionally, sort the list
	
	result_list = []
	for coordinate in coordinate_list:
		move_to_coordinate(coordinate[0], coordinate[1])
		action_result = action(action_param)
		if action_result:
			result_list.append(action_result)
	return result_list

	
	
def move_to_coordinate(x_val, y_val):
	move_on_axis(x_val, True)
	move_on_axis(y_val, False)
	return None
	

def move_on_axis(to_point, is_x_axis):
	# ensure to_point is within the bounds of the world size
	to_point = to_point % get_world_size()
	
	# set default directions and position check function (assuming x is theh move axis)
	pos_dir = East
	neg_dir = West
	pos_check_func = get_pos_x
	
	# update directions and position check if y is the move axis
	if not is_x_axis:
		pos_dir = North
		neg_dir = South
		pos_check_func = get_pos_y
		
	# calculate move direction & increment value
	move_dist = (to_point - pos_check_func())
	move_dir = pos_dir
	if move_dist > move_dist % (get_world_size() / 2):
		move_dir = neg_dir
	
	# move in the calcualted direction until we reach our point
	while pos_check_func() != to_point:
		move(move_dir)
	
	return None

	
	
		
	
	
	
