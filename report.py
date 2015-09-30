#from formulae import Calculation
#from reportlab.lib import colors
import numpy as np
import xlwt
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from formulae import Calculation
doc = SimpleDocTemplate("report.pdf", pagesize=landscape(A4),rightMargin=40,leftMargin=40,topMargin=30 )



class Calculation():
		#Array Elements
		column=["S.no","Speed","Delivery head","Velocity head","Loss of head","Total head","Rated head","Time for rise","Discharge","Rated discharge","Voltage","Current","Motor input","Rated input","Pump output","Efficiency"]
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
		elements=[]
		d=[]
		strdata=[['-' for x in range(16)] for x in range(11)]
		data=[[0 for x in range(16)] for x in range(11)]
		style = TableStyle([('ALIGN',(1,1),(-2,-2),'CENTER'),('BACKGROUND',(0,0),(15,0),colors.gray),
                       ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
                       ('VALIGN',(0,0),(0,-1),'BOTTOM'),
                       ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
                       ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                       ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                       ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ])
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
			self.rep()

	
		def rep(self):
			self.d= [['Deccan Industries, Ganapathy']]
			t=Table(self.d,1*[4*inch], 1*[0.5*inch])
			t.setStyle(TableStyle([('VALIGN',(0,-1),(-1,-1),'MIDDLE'),('FONTSIZE', (0,0), (-1, -1), 15),('TEXTCOLOR',(0,0),(0,-1),colors.blue),('BACKGROUND',(0,0),(5,0),colors.gray),('INNERGRID',(0,0), (-1,-1), 0.25, colors.black),('BOX', (0,0), (-1,-1), 0.25, colors.black),]))
			self.elements.append(t)
			for i in range(0,16):
				self.data[0][i]=self.column[i]
				
			for i in range(0,10):
				self.data[i+1][0]=i+1
				self.data[i+1][1]=self.actual_speed[i]
				self.data[i+1][2]=self.del_head[i]
				self.data[i+1][3]="%0.2f" %self.vel_head(self.time)[i]
				self.data[i+1][4]=self.loss_head[i]
				self.data[i+1][5]="%0.2f" %self.tot_head(i)[i]
				self.data[i+1][6]="%0.2f" %self.rated_head(i)[i]
				self.data[i+1][7]=self.time[i]
				self.data[i+1][8]="%0.2f" %self.discharge(self.time[i])[i]
				self.data[i+1][9]="%0.2f" %self.rated_discharge(self.time[i],i)[i]
				self.data[i+1][10]=self.voltage[i]
				self.data[i+1][11]=self.current[i]
				self.data[i+1][12]=self.motor_input(i)
				self.data[i+1][13]="%0.2f" %self.rated_input(i)
				self.data[i+1][14]="%0.2f" %self.pump_output(self.time[i],i)[i]
				self.data[i+1][15]="%0.2f" %self.efficiency(self.time[i],i)[i]
				
			t=Table(self.data,16*[0.4*inch], 11*[0.4*inch])
			s = getSampleStyleSheet()
			s = s["BodyText"]
			s.wordWrap = 'CJK'
			for i in range(0,11):
				for j in range(0,16):
					self.strdata[i][j]=str(self.data[i][j])
			data2 = [[Paragraph(cell, s) for cell in row] for row in (self.strdata)]
			t=Table(data2,colWidths=[0.65*inch] * 16,rowHeights=[0.4*inch]*11)
			t.setStyle(self.style)
			self.elements.append(t)
			doc.build(self.elements)



