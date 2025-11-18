import grass_and_tree
import only_carrot

# TODO: 해바라기, 소모 재료 같이 심기

def is_even(n):
	return n % 2 == 0

def pre_run():
	world_size = get_world_size()
	now_x = get_pos_x()
	
	if now_x < world_size // 2:
		for _ in range(now_x):
			move(West)
	else:
		for _ in range(world_size - now_x):
			move(East)

def run():
	pre_run()
	only_carrot.run()
	

run()