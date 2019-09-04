import component
import numpy as np

#a basic component
class simple_component(component.component):

	def __init__(self):
		self.component.component.__init__()
		self.points = np.array([[1,1],[2,1],[2,2],[1,2],[1,1]])
	
