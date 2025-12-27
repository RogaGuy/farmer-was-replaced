import plot
import actions

clear()

# begin farming and don't stop
while True:
	# plot.traverse_plot(actions.trees_and_carrots)
	loop_check = True
	while loop_check:
		planted_coords = plot.traverse_plot(actions.pumpkins)
		# TODO: check if list of coordinates is the full grid
		loop_check = (len(planted_coords) > 0)
		# if there are coordinates returned from the traverse_plot action, keep looping
		# else break out of the loop
	harvest()
		
	