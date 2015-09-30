
#!/usr/bin/env python
from kivy.config import Config
Config.set('graphics', 'height', 800)
Config.set('graphics', 'width', 1280)
Config.set('graphics', 'resizable', 0)
Config.write()

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
#from formulae import Calculation
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from interpolate import Plot_Graphs as PG
#from KivyCalendar import DatePicker


Builder.load_string("""
<deccanInputTable>:
	FloatLayout:
		canvas:
			Color:
				rgb: 1,1,1
			Rectangle:
				source: "logo200.png"
				size: 200,200
				pos: 125,600
		GridLayout:
			size_hint: 1,1
			pos_hint: {'center_x': .6, 'center_y': .3}
			cols: 9
			rows: 11	
			row_force_default: True
			row_default_height: 43
			col_force_default: True
			col_default_width: 100
			minimum_size: 50,100
			spacing: 1,1
		
			Label:
				text: "S.No"
				color: (0,0,0,1)
			Label:
				text: '''Head(m)'''
				color: (0,0,0,1)
			Label:
				text: "Time(sec)"
				color: (0,0,0,1)
			Label:
				text: "A(Amps)"
				color: (0,0,0,1)
			Label:
				text: "W1"
				color: (0,0,0,1)
			Label:
				text: "W2"
				color: (0,0,0,1)
			Label:
				text: "Frequency(Hz)"
				color: (0,0,0,1)
			Label:
				text: "Speed(RPM)"
				color: (0,0,0,1)
			Label:
				text: "Slip(%)"
				color: (0,0,0,1)
		
		###################################################### Row Entry 1 ###################################################
			Label:
				text: "1"
				color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
		
		###################################################### Row Entry 2 ###################################################
			Label:
				text: "2"
				color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
		###################################################### Row Entry 3 ###################################################
			Label:
				text: "3"
				color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
		###################################################### Row Entry 4 ###################################################
			Label:
				text: "4"
				color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
		###################################################### Row Entry 5 ###################################################
			Label:
				text: "5"
				color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
		###################################################### Row Entry 6 ###################################################
			Label:
				text: "6"
				color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
		###################################################### Row Entry 7 ###################################################
			Label:
				text: "7"
				color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
		###################################################### Row Entry 8 ###################################################
			Label:
				text: "8"
				color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
		###################################################### Row Entry 9 ###################################################
			Label:
				text: "9"
				color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
		###################################################### Row Entry 10 ###################################################
			Label:
				text: "10"
				color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
		Button:
			text: 'Back'
			on_press:
				root.manager.transition.direction = 'right'
				root.manager.current = 'Constants'
			size_hint: .07,.05
			pos_hint: {'center_x': .85, 'center_y': .32}
		Button:
			text: 'Plot'
			size_hint: .07,.05
			pos_hint: {'center_x': .85, 'center_y': .42}
			on_press: root.proceedToPlot()
<deccanInputConstants>
	FloatLayout:
		##############################################CONSTANT INPUT COLUMN 1############################################
		canvas:
			Color:
				rgb: 1,1,1
			Rectangle:
				source: "logo200.png"
				size: 200,200
				pos: 125,600
		Label:
			text: "Type"
			color: (0,0,0,1)
			font_size: 18
			size_hint: .1,.1
			pos_hint: {'center_x': .3, 'center_y': .82}
		TextInput:
			multiline: False
			cursor_color: (0,0,0,1)
			size_hint: .07,.04
			pos_hint: {'center_x': .45, 'center_y': .82}
		Label:
			text: "Unit No"
			color: (0,0,0,1)
			font_size: 18
			size_hint: .1,.1
			pos_hint: {'center_x': .3, 'center_y': .77}
		TextInput:
			multiline: False
			cursor_color: (0,0,0,1)
			size_hint: .07,.04
			pos_hint: {'center_x': .45, 'center_y': .77}
		Label:
			text: "Model"
			color: (0,0,0,1)
			font_size: 18
			size_hint: .1,.1
			pos_hint: {'center_x': .3, 'center_y': .72}
		TextInput:
			multiline: False
			cursor_color: (0,0,0,1)
			size_hint: .07,.04
			pos_hint: {'center_x': .45, 'center_y': .72}
		Label:
			text: "Rated Motor"
			color: (0,0,0,1)
			font_size: 18
			size_hint: .1,.1
			pos_hint: {'center_x': .3, 'center_y': .67}
		TextInput:
			multiline: False
			cursor_color: (0,0,0,1)
			size_hint: .07,.04
			pos_hint: {'center_x': .45, 'center_y': .67}
		Label:
			text: "Outlet Size"
			color: (0,0,0,1)
			font_size: 18
			size_hint: .1,.1
			pos_hint: {'center_x': .3, 'center_y': .62}
		TextInput:
			multiline: False
			cursor_color: (0,0,0,1)
			size_hint: .07,.04
			pos_hint: {'center_x': .45, 'center_y': .62}
		Label:
			text: "Discharge Constant"
			color: (0,0,0,1)
			font_size: 18
			size_hint: .1,.1
			pos_hint: {'center_x': .3, 'center_y': .57}
		TextInput:
			multiline: False
			cursor_color: (0,0,0,1)
			size_hint: .07,.04
			pos_hint: {'center_x': .45, 'center_y': .57}
		Label:
			text: "Rated Frequency"
			color: (0,0,0,1)
			font_size: 18
			size_hint: .1,.1
			pos_hint: {'center_x': .3, 'center_y': .52}
		TextInput:
			multiline: False
			cursor_color: (0,0,0,1)
			size_hint: .07,.04
			pos_hint: {'center_x': .45, 'center_y': .52}
		Label:
			text: "Liquid Temperature"
			color: (0,0,0,1)
			font_size: 18
			size_hint: .1,.1
			pos_hint: {'center_x': .3, 'center_y': .47}
		TextInput:
			multiline: False
			cursor_color: (0,0,0,1)
			size_hint: .07,.04
			pos_hint: {'center_x': .45, 'center_y': .47}
		Label:
			text: "Test Voltage"
			color: (0,0,0,1)
			font_size: 18
			size_hint: .1,.1
			pos_hint: {'center_x': .3, 'center_y': .42}
		TextInput:
			multiline: False
			cursor_color: (0,0,0,1)
			size_hint: .07,.04
			pos_hint: {'center_x': .45, 'center_y': .42}
		
		##############################################CONSTANT INPUT COLUMN 2############################################
		Label:
			text: "Date"
			color: (0,0,0,1)
			font_size: 18
			size_hint: .1,.1
			pos_hint: {'center_x': .66, 'center_y': .82}
		TextInput:
			multiline: False
			cursor_color: (0,0,0,1)
			size_hint: .07,.04
			pos_hint: {'center_x': .85, 'center_y': .82}
			on_focus: root.pickDate()
		Label:
			text: "Observed Frequency"
			color: (0,0,0,1)
			font_size: 18
			size_hint: .1,.1
			pos_hint: {'center_x': .66, 'center_y': .77}
		TextInput:
			multiline: False
			cursor_color: (0,0,0,1)
			size_hint: .07,.04
			pos_hint: {'center_x': .85, 'center_y': .77}
		Label:
			text: "Correction Head"
			color: (0,0,0,1)
			font_size: 18
			size_hint: .1,.1
			pos_hint: {'center_x': .66, 'center_y': .72}
		TextInput:
			multiline: False
			cursor_color: (0,0,0,1)
			size_hint: .07,.04
			pos_hint: {'center_x': .85, 'center_y': .72}
		Label:
			text: "Watt Meter Constant"
			color: (0,0,0,1)
			font_size: 18
			size_hint: .1,.1
			pos_hint: {'center_x': .66, 'center_y': .67}
		TextInput:
			multiline: False
			cursor_color: (0,0,0,1)
			size_hint: .07,.04
			pos_hint: {'center_x': .85, 'center_y': .67}
		Label:
			text: "Duty"
			color: (0,0,0,1)
			font_size: 18
			size_hint: .1,.1
			pos_hint: {'center_x': .66, 'center_y': .62}
		TextInput:
			multiline: False
			cursor_color: (0,0,0,1)
			size_hint: .07,.04
			pos_hint: {'center_x': .85, 'center_y': .62}
		Label:
			text: "Phases"
			color: (0,0,0,1)
			font_size: 18
			size_hint: .1,.1
			pos_hint: {'center_x': .66, 'center_y': .57}
		TextInput:
			multiline: False
			cursor_color: (0,0,0,1)
			size_hint: .07,.04
			pos_hint: {'center_x': .85, 'center_y': .57}
		Label:
			text: "Rated Speed"
			color: (0,0,0,1)
			font_size: 18
			size_hint: .1,.1
			pos_hint: {'center_x': .66, 'center_y': .52}
		TextInput:
			multiline: False
			cursor_color: (0,0,0,1)
			size_hint: .07,.04
			pos_hint: {'center_x': .85, 'center_y': .52}
		Label:
			text: "No. of Stages"
			color: (0,0,0,1)
			font_size: 18
			size_hint: .1,.1
			pos_hint: {'center_x': .66, 'center_y': .47}
		TextInput:
			multiline: False
			cursor_color: (0,0,0,1)
			size_hint: .07,.04
			pos_hint: {'center_x': .85, 'center_y': .47}
		Label:
			text: "Surface Finish of Pump Shaft"
			color: (0,0,0,1)
			font_size: 18
			size_hint: .1,.1
			pos_hint: {'center_x': .66, 'center_y': .42}
		TextInput:
			multiline: False
			cursor_color: (0,0,0,1)
			size_hint: .07,.04
			pos_hint: {'center_x': .85, 'center_y': .42}
		Button:
			text: 'Next'
			on_press:
				root.manager.transition.direction = 'left'
				root.manager.current = 'Table'
			size_hint: .07,.04
			pos_hint: {'center_x': .85, 'center_y': .32}
""")	
	
class deccanInputTable(Screen,PG):
	def __init__(self,**kwargs):
		super(deccanInputTable,self).__init__(**kwargs)
		pass
	def proceedToPlot(self):
		self.plot()
class deccanInputConstants(Screen):
	def __init__(self,**kwargs):
		super(deccanInputConstants,self).__init__(**kwargs)
		Window.clearcolor = (0.9,0.9,0.9,1)
	def pickDate(self):
		return DatePicker()
		
			
sm = ScreenManager()
sm.add_widget(deccanInputConstants(name='Constants'))
sm.add_widget(deccanInputTable(name='Table'))


class deccanMain(App):
	def build(self):
		return sm



if __name__ == "__main__":
	deccanMain().run()
