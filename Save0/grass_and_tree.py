def run():
	while True:
		for y in range(get_world_size()):
			for x in range(get_world_size()):
				if get_pos_y() < get_world_size() // 2:
					if can_harvest():
						harvest()
					if is_even(get_pos_x() + get_pos_y()):
						plant(Entities.Tree)
						if get_water() < 1:
							use_item(Items.Water)
					else:
						plant(Entities.Bush)
				else:
					if can_harvest():
						harvest()
					if get_ground_type() != Grounds.Grassland:
						till()
				move(East)
			move(North)