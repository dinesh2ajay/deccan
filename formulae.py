import numpy as np
import xlwt

class Calculation():
		#Array Elements
		column=["S.no","Speed","Delivery head","Velocity head","Loss of head","Total head","Rated head","Time for rise","Discharge","Rated discharge","Voltage","Current","Motor input","Rated input","Pump output","Overall efficiency"]
		actual_speed=np.array([2844,2843,2822,2815,2813,2819,2821,2829,2842,2870])
		del_head=np.array([0,20,40,60,80,100,120,130,140,150])
		loss_head=np.array([0,0,0,0,0,0,0,0,0,0])
		time=np.array([23.85,25.46,29.66,34.7,39.90,50.88,59.71,78.66,102.4,126.46])
		voltage=np.array([380,380,380,380,380,380,380,380,380,380])
		current=np.array([12.60,13.00,13.40,13.80,14.20,14.20,13.80,13.20,12.20,10.80])

		#Constants
		dis_const=150
		outlet_size=50
		cor_head=2.5
		rated_speed=2850.0
		EFFICIENCY=[]
		#Functions to calculate parameters
		def discharge(self,time):
		    return self.dis_const/self.time

		def vel_head(self,time):
		    return pow(self.discharge(self.time),2)*82711.17/pow(self.outlet_size,4)

		def tot_head(self,i):
			return self.del_head[i]+self.vel_head(self.time[i])+self.cor_head+self.loss_head[i]

		def rated_head(self,i):
		    return pow(self.rated_speed/self.actual_speed[i],2)*self.tot_head(i)

		def rated_discharge(self,time,i):
		    return (self.rated_speed/self.actual_speed[i])*self.discharge(self.time)

		def motor_input(self,i):
		    return self.voltage[i]*self.current[i]*1.5/1000

		def rated_input(self,i):
		    return pow(self.rated_speed/self.actual_speed[i],3)*self.motor_input(i)

		def pump_output(self,time,i):
		    return 9.81*self.rated_head(i)*self.rated_discharge(self.time,i)/1000

		def efficiency(self,time,i):
			return (self.pump_output(self.time,i)/self.motor_input(i))*100
		def worksheet(self):
			#creating a new worksheet
			wb=xlwt.Workbook()
			ws=wb.add_sheet("database")

			#Writing column headings in worksheet
			row=0
			for i in range(0,16):
				ws.write(row,i,self.column[i])

			#Writing S.no's in worksheet
			row=1
			for i in range(1,11):
				ws.write(row,0,i)
				row+=1

			#Writing data into the worksheet
			row=1
			for i in range(0,10):
				col=1
				ws.write(row,col,self.actual_speed[i])
				col+=1
				ws.write(row,col,self.del_head[i])
				col+=1
				ws.write(row,col,self.vel_head(self.time)[i])
				col+=1
				ws.write(row,col,self.loss_head[i])
				col+=1
				ws.write(row,col,self.tot_head(i)[i])
				col+=1
				ws.write(row,col,self.rated_head(i)[i])
				col+=1
				ws.write(row,col,self.time[i])
				col+=1
				ws.write(row,col,self.discharge(self.time[i])[i])
				self.DISCHARGE = self.discharge(self.time[i])
				col+=1
				ws.write(row,col,self.rated_discharge(self.time[i],i)[i])
				col+=1
				ws.write(row,col,self.voltage[i])
				col+=1
				ws.write(row,col,self.current[i])
				col+=1
				ws.write(row,col,self.motor_input(i))
				col+=1
				ws.write(row,col,self.rated_input(i))
				col+=1
				ws.write(row,col,self.pump_output(self.time[i],i)[i])
				col+=1
				ws.write(row,col,self.efficiency(self.time[i],i)[i])
				self.EFFICIENCY.append(self.efficiency(self.time[i],i)[i])
				row+=1

			wb.save("databaseee.xls")
			
