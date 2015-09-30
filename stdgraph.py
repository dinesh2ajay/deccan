import numpy as np
import matplotlib.pyplot as plt
q=[0,0.25,0.5,0.75,1,1.25,1.5,1.75,2,2.25,2.5,2.75,3,3.25,3.5,4]
h=[104.8,106.5,106.1,105.5,104.4,102.1,98.0,95.4,92.7,90.6,87.0,78.1,69.2,58.6,46.2,33.7]
e=[0,11,18.5,23.5,27.5,30,32.5,35,37.5,39.5,40,38.5,37,35,33,31]
p=[2.14,2.38,2.81,3.30,3.72,4.17,4.44,4.68,4.85,5.06,5.33,5.47,5.51,5.34,4.80,4.00]
class Plot_Graphs():
	def __init__(self,**kwargs):
		pass
	def plot(self):
		fig, ax = plt.subplots()
		axes = [ax, ax.twinx(), ax.twinx()]
		fig.subplots_adjust(right=0.75)
		axes[-1].spines['right'].set_position(('axes', 1.2))
		colors = ('Green', 'Red', 'Blue')
                powr=np.poly1d(np.polyfit(q,p,2))
		eff=np.poly1d(np.polyfit(q,e,2))
		head=np.poly1d(np.polyfit(q,h,2))
		dis=np.linspace(q[0],q[15],500)
		#Efficiency Axis Plotting
		axes[2].plot(dis,eff(dis), color=colors[0])
		axes[2].plot(q,e,'ko',color=colors[0])
		axes[2].set_ylabel('Efficiency (%)', color=colors[0])
		axes[2].tick_params(axis='y', colors=colors[0])
		#power Axis Plotting
		axes[1].plot(dis,powr(dis), color=colors[1])
		axes[1].plot(q,p,'k+',color=colors[1])
		axes[1].set_ylabel('Power (kW)', color=colors[1])
		axes[1].tick_params(axis='y', colors=colors[1])
		#Head
		axes[0].plot(dis,head(dis), color=colors[2])
		axes[0].plot(q,h,'kx',color=colors[2])
		axes[0].set_ylabel('Head (m)', color=colors[2])
		axes[0].tick_params(axis='y', colors=colors[2])
		axes[0].set_xlabel('Discharge in lps')
		plt.grid()
		plt.show()
			
		
if __name__ == "__main__":
	Plot_Graphs()

