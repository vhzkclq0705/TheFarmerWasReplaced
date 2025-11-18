# Carrot
# time: 4.8s - 7.2s
# ground: only Soil
# cost: hay 16, wood 16

def run():
	while True:
		for y in range(get_world_size()):
			for x in range(get_world_size()):
				if get_ground_type() == Grounds.Grassland:
					till()
				if can_harvest():
					harvest()
				plant(Entities.Carrot)
				if get_water() < 0.5:
					use_item(Items.Water)
				move(East)
			move(North)