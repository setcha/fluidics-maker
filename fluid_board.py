import math
import numpy as np
import component as ct


#Holds the path
#1. Add connections/pass in connections (netlist?)
#2. Place components
#3. Path finding
#4. Meld points

class fluid_board():
	
	max_turning_radius = 0.1 #radians/unit

	#Example points
	def __init__(self):
		self.points = points
		#Items are [component, connections]
		#Just give the components, in order
		#elements of connections are {connection_1:connection_1_destination, connection_2:connection_2_destination,...}
		#Destinations are [comp_id, port]
		self.components = []
		#Should this be called a netlist? This basically gives an ordering so that we can just connect them one at a time
		self.edge_list = []
		#Also might be able to determine if a piece is "trapped" and needs to escape into another layer
		

		#make inputs/power a component, or not?

	

	def point_is_available(self, position):
		for component in components:
			#if point in component.bounding_box



	#Place components
	def add_component(self, comp_type, position, direction):
		#In the future, specify connections, layer, collision detection
		#Place in components without connections, gradually add them in
		self.components.append([ct.component(comp_type, position, direction), {}])
		#check for collisions here?
		


	#comp_1 and comp_2 are just integers that give the id with the point in the list
	def connect(self, comp_1, comp_2, comp_1_port, comp_2_port):
		#index into comp_1 connections


		#this is screwy, change this
		self.components[comp_1][1][comp_1_port] = [comp_2, comp_2_port]
		self.components[comp_2][1][comp_2_port] = [comp_2, comp_2_port]
		#keep where every component should be connected to every other component
		self.edge_list.append([[comp_1, comp_1_port], [comp_2, comp_2_port]])
		#add component connections to the components themselves
		self.components[comp_1].add_connection(comp_1_port, [comp_2, comp_2_port])
		self.components[comp_2].add_connection(comp_2_port, [comp_1, comp_1_port])




	#take into account the location of the ports, whether we are trapped and need to move around, and line drawing
	def draw_connection(self, edge):
		#edges are [[comp_1, comp_1_port], [comp_2, comp_2_port]]
		#edge[0][0] is comp_1 (its id number), so get its port location (ie edge[0][1] says something like 'out_1')
		
		#two (x,y) points
		port_1_loc = self.components[edge[0][0]].get_port_loc(edge[0][1]) 
		#a direction in radians, perpendicular to the two points (going counterclockwise from the origin)
		port_1_dir = self.components[edge[0][0]].get_port_dir(edge[0][1]) 

		#two (x,y) points
		port_2_loc = self.components[edge[1][0]].get_port_dir(edge[1][1])
		#a direction in radians, perpendicular to the two points (going counterclockwise from the origin)
		port_2_dir = self.components[edge[1][0]].get_port_dir(edge[1][1])

		#making an edge also makes a new component, with custom points

		#A* search, bidirectional breadth first search, layers above work too
		#minimize total distance 


		#keep a list of points, and minimum distance to that point (square?)
		#maybe keep some preset 


		#find next available point, only able to turn x radians per unit


		#make a "point is available" function














