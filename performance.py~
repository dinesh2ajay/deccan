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
from stdgraph import Plot_Graphs as PG
Builder.load_string("""
<SpecificPerformance>:
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
			pos_hint: {'center_x': .9, 'center_y': .2}
			cols: 2
			rows: 7
			row_force_default: True
			row_default_height: 43
			col_force_default: True
			col_default_width: 100
			minimum_size: 50,100
			spacing: 1,1
		
			Label:
				text: "N"
				color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			Label:
				text: 'H'
				color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			Label:
				text: "H per Stage"
				color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			Label:
				text: "Flow rate"
				color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			Label:
				text: "Efficiency"
				color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
			Label:
				text: "Power"
				color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)	
			Label:
				text: "Nq"
				color: (0,0,0,1)
			TextInput:
				multiline: False
				cursor_color: (0,0,0,1)
		Button:
			text: 'Plot'
			size_hint: .07,.05
			pos_hint: {'center_x': .85, 'center_y': .42}
			on_press: root.proceedToPlot()

""")

	
class SpecificPerformance(Screen,PG):
	def __init__(self,**kwargs):
		super(SpecificPerformance,self).__init__(**kwargs)
		Window.clearcolor = (0.9,0.9,0.9,1)
		pass
	def proceedToPlot(self):
		self.plot()
			
sm = ScreenManager()
sm.add_widget(SpecificPerformance(name='Table'))
	

class deccan(App):
	def build(self):
		return sm



if __name__ == "__main__":
	deccan().run()
