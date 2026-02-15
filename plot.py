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


def traverse_nearest_coordinates(coordinate_list, action):
	result_list = []
	while coordinate_list:
		to_coord = get_nearest_coord_from_list(coordinate_list)
		move_to_coordinate(to_coord[0], to_coord[1])
		if action(None):
			coordinate_list.remove(to_coord)
	return None


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


def get_nearest_coord_from_list(coordinate_list):
	# disallow current coordinate unless only coord left
	min_dist = 99
	nearest_coord = None
	for c_x, c_y in coordinate_list:
		total_dist = abs(get_axis_dist(get_pos_x(), c_x)) + abs(get_axis_dist(get_pos_y(), c_y))
		if total_dist < min_dist and (total_dist > 0 or len(coordinate_list) == 1):
			min_dist = total_dist
			nearest_coord = (c_x, c_y)
	return nearest_coord


def move_to_coordinate(x_val, y_val):
	move_on_axis(x_val, True)
	move_on_axis(y_val, False)
	return None


def get_axis_dist(from_point, to_point):
	move_dist = (to_point - from_point) % get_world_size() # positive distance
	if move_dist > get_world_size() / 2:
		move_dist = (move_dist - get_world_size())
	quick_print("from " + str(from_point) + " to " + str(to_point) + " is " + str(move_dist) + " distance")
	return move_dist
	

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
	move_dir = pos_dir
	move_dist = get_axis_dist(pos_check_func(), to_point)
	if move_dist < 0:
		move_dir = neg_dir

	# move in the calcualted direction until we reach our point
	while pos_check_func() != to_point:
		move(move_dir)
	
	return None
