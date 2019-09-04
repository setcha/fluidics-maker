import math

class Crawler():

	#x and y are euclidean, direction is in radians, velocity is 1px/sec, timestep = 0.01 sec (sec is not really 1 sec)
	def __init__(x=0, y=0, direction=0, velocity=1, angular_velocity=1, path=[], timestep=0.01):
		self.x = x
		self.y = y
		self.direction = direction%(2*math.pi)
		self.velocity = velocity
		self.angular_velocity=angular_velocity
		self.path = []

	
	#adds the current [x,y,dir] position to the path
	def record_position():
		self.path.append([self.x, self.y, self.direction])
		return [self.x, self.y, self.direction]

	#position is (x,y)
	def get_position():
		return(self.x, self.y)


	#position is (x,y)
	def set_position(position):
		self.x = position[0]
		self.y = position[1]


	def get_direction():
		return self.direction


	#direction is a number between 0 and 2*pi
	def set_direction(direction):
		self.direction = direction%(2*math.pi)



	def get_dir_to_point(point):
		x_end, y_end = point
		direction = math.atan((y_end - self.y)/(x_end - self.x))
		if y_end < self.y:
			direction += math.pi
		return direction


	def next_step():
		x = self.x + velocity*timestep*math.cos(self.direction)
		y = self.y + velocity*timestep*math.sin(self.direction)
		return [x, y]



	#position is (x,y)
	def go_to(position):

		dir_to_point = self.get_dir_to_point(position)
		turn_plus = 1
		if dir_to_point - self.direction < 0:
			turn_plus = -1

		#turn toward that direction as quickly as possible?


		#turn_right = 
		while self.x != x_end and self.y != y_end:
			#predict where the next step will be
			next_step = self.next_step()
			#set the actual crawler position
			self.set_position(next_step)
			self.record_position()

			#rotate a bit

			




	



