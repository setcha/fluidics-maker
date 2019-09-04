import svgwrite
import math
import numpy as np
from numpy import arange

#channel_width = "1mm"
mm = 3.543307
channel_width = 1*mm

dwg = svgwrite.Drawing('test.svg', profile='tiny')
#dwg = svgwrite.Drawing(name + ".svg", (1000, 1000), debug=True)

#dwg.add(dwg.polygon([[10, 10],[40, 10],[40, 40],[10, 40]], stroke=svgwrite.rgb(10, 10, 16, '%'), fill='none'))


#radius in px, center in px, direction is +- 1, start and end are in radians, resolution is angular resolution
def circle_points(radius, center, direction=1, start_rad=0, end_rad=2*math.pi, resolution=0.01):
	num_points = int(end_rad - start_rad/resolution)
	points=[]
	for i in arange(start_rad, end_rad, resolution):
		points.append([radius*math.cos(i)+center[0], radius*math.sin(i)+center[1]])
	return points


#end direction is the point to aim at after the turn is done
def circular_channel(radius, channel_width, current_point, previous_point, next_point, start_rad=0, resolution=0.01):
	#find the center
	#center

	#find the start_rad and end_rad
	return






def points_to_mm(points):
	points_np = np.array(points)
	points_np = points_np * 3.543307
	return points_np.tolist()



# def direct_toward(curr_direction, end_direction, min_turning_radius=3*mm):
# 	#a = v^2/r
# 	new_direction = np.array(curr_direction)
# 	magnitude = np.inner(curr_direction, curr_direction)
# 	new_direction = new_direction/magnitude
# 	new_direction = 
# 	return new_direction


#the derivative at this point should be halfway between the previous point and the next point
#define by the middle point, or the outer point?
#keeps all channel pieces separate, combine them after
def channel_points(points, channel_width=channel_width, min_turning_radius=3, velocity=2, resolution=0.01):
	right_wall = []
	left_wall = []
	#end x - start x, end y - start y
	direction = [points[1][0]-points[0][0], points[1][1]-points[0][1]]





	# for point in points[1:-1]




dwg.add(dwg.polygon(points_to_mm(circle_points(10, [20,20], end_rad=2*math.pi)), stroke=svgwrite.rgb(10, 10, 16, '%'), fill='none'))
dwg.save()