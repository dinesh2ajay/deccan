import numpy as np
import matplotlib.pyplot as plt
from formulae import Calculation

class Plot_Graphs(Calculation):
	def __init__(self,**kwargs):
		pass
	def plot(self):
		self.worksheet()
		fig, ax = plt.subplots()
		axes = [ax, ax.twinx(), ax.twinx()]
		fig.subplots_adjust(right=0.75)
		axes[-1].spines['right'].set_position(('axes', 1.2))
		colors = ('Green', 'Red', 'Blue')
		cur=np.poly1d(np.polyfit(self.DISCHARGE,self.current,2))
		eff=np.poly1d(np.polyfit(self.DISCHARGE,self.EFFICIENCY,2))
		head=np.poly1d(np.polyfit(self.DISCHARGE,self.del_head,2))
		dis=np.linspace(self.DISCHARGE[0],self.DISCHARGE[9],500)
		#Head Axis Plotting
		axes[2].plot(dis,eff(dis), color=colors[0])
		axes[2].plot(self.DISCHARGE,self.EFFICIENCY,'ko',color=colors[0])
		axes[2].set_ylabel('Efficiency (%)', color=colors[0])
		axes[2].tick_params(axis='y', colors=colors[0])
		#Current Axis Plotting
		axes[1].plot(dis,cur(dis), color=colors[1])
		axes[1].plot(self.DISCHARGE,self.current,'k+',color=colors[1])
		axes[1].set_ylabel('Current (A)', color=colors[1])
		axes[1].tick_params(axis='y', colors=colors[1])
		#Efficiency Axis Plotting
		axes[0].plot(dis,head(dis), color=colors[2])
		axes[0].plot(self.DISCHARGE,self.del_head,'kx',color=colors[2])
		axes[0].set_ylabel('Head (m)', color=colors[2])
		axes[0].tick_params(axis='y', colors=colors[2])
		axes[0].set_xlabel('Discharge in lps')
		plt.grid()
		plt.show()
		self.DISCHARGE = []
		self.EFFICIENCY= []
		
		
if __name__ == "__main__":
	Plot_Graphs()

