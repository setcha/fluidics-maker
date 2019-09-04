
import math
import numpy as np
import time

# given a point in form np.array(x,y),
# give the angle in radians
def get_vec_dir(point_a, point_b):
	dir_vec = point_b - point_a
	if dir_vec[0]==0:
		direction = math.pi/2
	else:
		direction = math.atan(dir_vec[1]/dir_vec[0])

	#if the y component is greater than 0, or its on the 0 or 180 degree line
	if dir_vec[1] > 0 or (dir_vec[1] == 0 and dir_vec[0] > 0): 
		return direction
	else:
		return direction + math.pi


#points are in counter clockwise order
#could also do this with dot product and vector stuff
#x, A, B, and C are all points
#having each of them as separate if statements should average two checks instead of guarantee three,
#because we have to do a lot of these
def is_in_triangle_angle(x, A, B, C):
	#the angles that the tested pont needs to be less than
	ang_1 = get_vec_dir(A, x) - get_vec_dir(A, C)
	#if it is outside of the triangle. On the line is included as inside of the triangle.
	if ang_1 > 0:
		return True

	ang_2 = get_vec_dir(B, x) - get_vec_dir(B, A)
	#if it is outside of the triangle. On the line is included as inside of the triangle.
	if ang_2 > 0:
		return True

	ang_3 = get_vec_dir(C, x) - get_vec_dir(C, B)
	#if it is outside of the triangle. On the line is included as inside of the triangle.
	if ang_3 > 0:
		return True

	return False



#helper function for checking points in a triangle
def sign(p1, p2, p3):
	return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])


#the version from online, uses checking the half planes of each 
def is_in_triangle(x, A, B, C):
	d1 = sign(x, A, B) #
	d2 = sign(x, B, C) #
	d3 = sign(x, C, A)

	has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
	has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

	return not (has_neg and has_pos)





#determine if two line segments cross each other
def line_cross(A, B, C, D):
	line_1_a = sign(A, C, D)
	line_1_b = sign(B, C, D)


	#XOR 
	line_1_crosses = line_1_a ^ line_1_b

	line_2_c = sign(C, A, B)
	line_2_d = sign(D, A, B)

	#XOR
	line_2_crosses = line_2_c ^ line_2_d






#turn the points in this component into triangles that can be checked easier
def make_point_triangles(self, points):

	pass




class component():
	#component_points should be defined counterclockwise, because this specifies what side is inside and what is outside
	#make a component 3D by making the array a 3D array (several 2D pieces placed on layers)
	#maybe save all this data as a "component_data" class?
	component_points = {'simple':np.array([[1,1],[-1,1],[-1,-1],[1,-1],[1,1]]),
						'box':np.array([[1,1],[2,1],[2,2],[1,2],[1,1]])}

	component_ports = {'simple':{'in_1':np.array([[1,-1],[1,1]]), 'out_1':np.array([[-1,1],[-1,-1]])}}

	def __init__(self, comp_type, position, direction):
		#component type, a string
		self.comp_type = comp_type
		#should be a numpy vector of x,y
		self.position = position
		#direction in radians
		self.direction = direction
		self.direction_matrix = np.array([[math.cos(direction), -math.sin(direction)],[math.sin(direction), math.cos(direction)]])
		
		#points initialized (rotate the points by "direction" radians, then move the position)
		self.untouched_points = self.component_points[comp_type]
		self.points = np.inner(self.untouched_points, self.direction_matrix) + position
		self.ports = self.component_ports[comp_type]
		for port in self.ports:
			self.ports[port] = np.inner(self.ports[port], self.direction_matrix) + position

		self.connections = {}

		self.bounding_box = self.get_bounding_box()
	

	def rotate_component(self, radians):
		self.direction = self.direction + radians
		self.direction_matrix = np.array([[math.cos(direction), -math.sin(direction)],[math.sin(direction), math.cos(direction)]])
		self.points = np.inner(self.untouched_points, self.direction_matrix) + self.position
		self.bounding_box = self.get_bounding_box()



	def place(self, position):
		delta = position - self.position
		self.position = position
		self.points = self.points + delta
		self.bounding_box = self.get_bounding_box()



	#define the structure of a new component, usually the shape of a wire
	def make_new_component(self, points, ports):

		pass



	#define a logical connection between one of this component's ports and one of 
	#another component's ports. other_port is of form [other_component_id, other_component_port]
	def add_connection(self, my_port, other_port):
		self.connections[my_port] = other_port



	#give the two [x,y] ports for the desired port
	def get_port_loc(self, port):
		return self.ports[port]



	#get the direction that a port is facing (uses the two points that make its end)
	def get_port_dir(self, port):

		point_a = self.ports[port][0]
		point_b = self.ports[port][1]
		#get the direction, subtract a right angle, then make it between 0 and 2 pi
		port_dir = (get_vec_dir(point_a, point_b) - math.pi/2) % 2*math.pi

		return port_dir



	#return the box of the component, for initial point checking
	def get_bounding_box(self):
		#get the upper left point on the screen
		xmin = np.min(self.points[:,0])
		ymin = np.min(self.points[:,1])

		#get the lower right point on the screen
		xmax = np.max(self.points[:,0])
		ymax = np.max(self.points[:,1])

		self.bounding_box = np.array([[xmin, ymin],[xmax, ymax]])

		return np.array([[xmin, ymin],[xmax, ymax]])




	#return true if the point given is within this component
	def point_in_component(self, point):
		#check bounding box first
		x = point[0]
		y = point[1]

		#check bounding box conditions
		lower_x = x >= self.bounding_box[0][0]
		lower_y = y >= self.bounding_box[0][1]
		upper_x = x <= self.bounding_box[1][0]
		upper_y = y <= self.bounding_box[1][1]

		if lower_x and lower_y and upper_x and upper_y:
			pass
		else:
			#if it isn't in the bounding box, it isn't in the component
			return False

		#check the rest of the component

		#split into triangles

		pass



	#return True if this line segment intersects any line segment
	def lines_over_component(self, point_1, point_2):

		pass



	#don't think its necessary, but its neat
	def convex_hull(self):

		pass


	#return a shell that indicates a boundary layer
	#ie if you are within the boundary, you are within boundary_width units of the component 
	def make_outer_boundary(self, boundary_width):

		pass





x=np.array([2,2])
y=np.array([10,2])

A=np.array([1,1])
B=np.array([3,1])
C=np.array([2,3])


start = time.time()
for i in range(100000):
	is_in_triangle_angle(x,A,B,C)
for i in range(100000):
	is_in_triangle_angle(y,A,B,C)

end = time.time()
print("Time for angle way: ", end-start)



start = time.time()
for i in range(100000):
	is_in_triangle(x,A,B,C)

print(is_in_triangle(x,A,B,C))

for i in range(100000):
	is_in_triangle(y,A,B,C)

print(is_in_triangle(y,A,B,C))

end = time.time()
print("Time for half plane way: ", end-start)


















