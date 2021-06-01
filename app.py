import PySimpleGUI as sg
import requests as req
import time
import news
import wikipedia
import sqlite3 as sq
from mutagen.mp3 import MP3
import os
from pygame import mixer
import converter
import webbrowser


sg.theme('DarkGrey1')

# ---------------------------------------------------------------------- #
#                    Default images and music used && CONSTANTS          #
# ---------------------------------------------------------------------- #

logos = {

	'wikipediaLogo' : "./Images/wikipedia.png",
	'musicLogo' : "./Images/music.png",
	'todoLogo' : "./Images/todo.png",
	'calculatorLogo' : "./Images/calculator.png",
	'jazzLogo' : "./Images/jazz.png"
}

imagesize = 250
mainButtonColor = "white"

#for music
playlist = []
status = None
songNumber = 0
waiting = 0
starting = 0


#for calculator

buttonSizeX = 15
buttonSizeY = 3
entered = "Lets Calculate"
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "(", ")"]
operators = ["+", "-", "/", "x"]
result = 0
count = 0


# for todo

Del = [f'_Del{i}_' for i in range(100)]
Edit = [f'_Edit{i}_' for i in range(100)]


# for credits
links ={
	"Python":'https://www.python.org/',
	'SUM4N':'https://twitter.com/tweetSUM4N',
	'BeautifulSoup':'https://www.crummy.com/software/BeautifulSoup/',
	"lxml":'https://lxml.de/',
	"Mutagen":'https://github.com/quodlibet/mutagen',
	"Pygame":'https://www.pygame.org/news',
	"PySimpleGUI":'https://github.com/PySimpleGUI/PySimpleGUI',
	"requests":'https://docs.python-requests.org/en/master/',
	"wikipedia":'https://github.com/goldsmith/Wikipedia'
}

packages = ["PySimpleGUI",'BeautifulSoup',"lxml","Mutagen","Pygame","requests","wikipedia","Python",'SUM4N']



#TODO

## To run this as exe Uncomment below function

# def resource_path(relative_path):
# 	try:
# 		base_path = sys._MEIPASS
# 	except Exception:
# 		base_path = os.path.abspath(".")

# 	return os.path.join(base_path, relative_path)




# to run it as  a python script uncomment this function   


# def resource_path(relative_path):
#     	return logos[relative_path.split('.')[0] + 'Logo']



# ---------------------------------------------------------------------- #
#                    INITIALISING DB for TODO                            #
# ---------------------------------------------------------------------- #

connection = sq.connect("ToDo.db", detect_types=sq.PARSE_DECLTYPES)

cursor = connection.cursor()
try:
	cursor.execute("CREATE TABLE Todo (todoName TEXT,addedTime TEXT)")
except:
	pass





# ---------------------------------------------------------------------- #
#                              TABS LAYOUT                               #
# ---------------------------------------------------------------------- #

default = [
   
	
	[
		sg.T(size = (72, None)),
		sg.Text("",size = (25,None), key = '-TIME-', font = (None,18)), 
	],
	[
		sg.T(size = (72, None)),
		sg.Text("postalCode,countryCode",size = (25,None), key = '-WEATHER-', font = (None,18),justification='left'), 
	],
	
	
	[ sg.Column(
		
		[   [sg.T(size = (None,3))],
			
			[
				
				sg.Button("", image_filename = resource_path("wikipedia.png"),image_size = (imagesize,imagesize),button_color = mainButtonColor, key = "Wikipedia"),
				sg.T(size=(5, 0)),
				sg.Button("", image_filename = resource_path("calculator.png"),image_size = (imagesize,imagesize),button_color = mainButtonColor, key = "Calculator"),
			],

				[sg.T(size=(0, 2))],
			[
				sg.Button("",image_filename =   resource_path("todo.png"),image_size = (imagesize,imagesize),button_color = mainButtonColor, key = "ToDo"),
				sg.T(size=(5,0)),
				sg.Button("", image_filename =  resource_path("music.png"),image_size = (imagesize,imagesize),button_color = mainButtonColor, key = "Music"),
			],
			
			[   sg.T(size=(30, 2)),
				sg.Button("Close All",)
			],
		], size = (700,800),
			 ), # column 1

	

	sg.Column(
		[
			[sg.T(size = (25,0)),
		sg.Input("PostalCode,countryCode for weather", size = (30,1), key = '-WL-'),
		sg.Input("keyword for news",key = '-NL-', size = (20,1)),
		sg.Button("search", key = '-SEARCH-'),
		],
		[sg.Column(
			
			[
			   [sg.Text("Currents News from google based on your keyword", font = (None,14), key = f'NEWS{i}', visible = True, size = (55,None), pad = ((5,5),(5,5)))] if i == 0 else [sg.Text("", font = (None,14), key = f'NEWS{i}', visible = True, size = (55,None), pad = ((5,5),(5,5)))]  for i in range(100) 
			],
			scrollable = True,
			vertical_scroll_only = True,
			size = (700,800),
			background_color = "grey"
			 
			
		)]

		]
	)

	]
]

todo = [
	[
		sg.Column(
			[
				
			]
			,
			background_color = "grey",
			size = (400,800)
		),
		sg.Column([


			[   sg.T(size = (12,None),background_color = "blue",),
				sg.Input("Hello there", key = '-todo-'),
				sg.Button("Add", key = '-ADDTODO-'),
				sg.Button("reLoad", key = '-RELOAD-')
			],
			[
				sg.T(size = (2,None),background_color = "blue",)
			],
			[   
			sg.Column(
				   [
					   [
						   sg.Multiline("No\nTodo\nYou are all\n Caught up!",size = (68, 3), key = f'_Todo{i}_', visible = True,pad = ((5,5),(5,5)),justification='center',enable_events=True,no_scrollbar=True,disabled=True),
						   sg.pin(sg.Button("Edit", key=f"_Edit{i}_", visible = False)),
							sg.pin(sg.Button("Delete", key=f"_Del{i}_", visible = False)),
							]
							if i == 0 else [
						   sg.Multiline("",size = (68, 3), key = f'_Todo{i}_', visible = True,pad = ((5,5),(5,5)),enable_events=True,no_scrollbar=True,disabled=True),
							sg.pin(sg.Button("Edit", key=f"_Edit{i}_", visible = False)),
							sg.pin(sg.Button("Delete", key=f"_Del{i}_", visible = False)),
					   ]for i in range(100)


					
				   ],
					background_color = "grey",
					size = (600,700),
					scrollable = True,
					vertical_scroll_only = True,
					key = '-COL-'

			   ) 
			]
			   
			   
		]
		,
			background_color = "blue",
			size = (600,800)
		
		),
		sg.Column(
			[
				[
					sg.Input("",key = '-UPDATETODO-',size = (45,7),visible= False)
				],
				[sg.Button("Save", key = '-SAVEUPDATE-',visible= False)]
			]
			,
			background_color = "grey",
			size = (400,800)
		),
	]
]    




calculator = [[
	sg.Column(
	[
	[sg.T(size=(0, 10))],
	
	[
		sg.Text(
			"Lets Calculate",
			size=(31, 2),
			justification="center",
			key="_INPUT_",
			font="Any 28",
			background_color="yellow",
			text_color="black",
		)
	],
	[sg.T(size=(0, 5))],
	[
		# sg.T(size=(30, 0)),
		sg.Button("1", size=(buttonSizeX, buttonSizeY)),
		sg.Button("2", size=(buttonSizeX, buttonSizeY)),
		sg.Button("3", size=(buttonSizeX, buttonSizeY)),
		sg.Button("+", size=(buttonSizeX, buttonSizeY)),
		sg.Button("/", size=(buttonSizeX, buttonSizeY)),
	],
	[
		# sg.T(size=(30, 0)),
		sg.Button("4", size=(buttonSizeX, buttonSizeY)),
		sg.Button("5", size=(buttonSizeX, buttonSizeY)),
		sg.Button("6", size=(buttonSizeX, buttonSizeY)),
		sg.Button("-", size=(buttonSizeX, buttonSizeY)),
		sg.Button("C", size=(buttonSizeX, buttonSizeY)),
	],
	[
		# sg.T(size=(30, 0)),
		sg.Button("7", size=(buttonSizeX, buttonSizeY)),
		sg.Button("8", size=(buttonSizeX, buttonSizeY)),
		sg.Button("9", size=(buttonSizeX, buttonSizeY)),
		sg.Button("x", size=(buttonSizeX, buttonSizeY)),
		sg.Button("AC", size=(buttonSizeX, buttonSizeY)),
	],
	[
		# sg.T(size=(30, 0)),
		sg.Button(".", size=(buttonSizeX, buttonSizeY)),
		sg.Button("0", size=(buttonSizeX, buttonSizeY)),
		sg.Button("(", size=(buttonSizeX, buttonSizeY)),
		sg.Button(")", size=(buttonSizeX, buttonSizeY)),
		sg.Button("=", size=(buttonSizeX, buttonSizeY)),
	],
	],
	size = (750,800)
	),

	sg.Column(
		[   
			[sg.T(size=(0, 5))],

			[   sg.Input("Enter numerical here",size = (20,1), key = '-NUMI-'),
				sg.Combo(
				values = ["Convert Numerical","Decimal to Binary", "Decimal to Hex","Decimal to Oct", "Binary to Decimal","Binary to Hex", "Binary to Oct","Hex to Decimal", "Hex to Binary", "Hex to Oct"],
				key = '-NUM-',
				default_value='Convert Numerical',
				readonly = True,
				size = (20,None),
				enable_events=True
			),
			sg.Text("Result",size = (30,1), background_color = "white",text_color = "black", key = '-NUMR-'),
			],
			[sg.T(size = (20,None)),sg.Button("Convert Numerical",key = '-NUMC-')],

			############## MASS #####################

			[sg.T(size=(0, 3))],
			[   sg.Input("Enter Mass here",size = (20,1), key = '-MASSI-'),
				sg.Combo(
				values = ["Convert Mass","Kg to Gram","Gram to Kg" ,"Kg to Pound","Pound to Kg", "Gram to Pound"],
				key = '-MASS-',
				default_value='Convert Mass',
				readonly = True,
				size = (20,None),
				enable_events=True
			),
			sg.Text("Result",size = (30,1), background_color = "white",text_color = "black", key = '-MASSR-'),
			],
			[sg.T(size = (20,None)),sg.Button("Convert Mass", key = '-MASSC-')],

			######### TEMPERATURE #############

			[sg.T(size=(None, 3))],
			[   sg.Input("Enter Temp here",size = (20,1), key = '-TEMPI-'),
				sg.Combo(
				values = ["Convert Temperature","°F to °C", "°C to °F","°C to K","°F to K", "K to °C", "K to °F"],
				key = '-TEMP-',
				default_value='Convert Mass',
				readonly = True,
				size = (20,None),
				enable_events=True
			),
			sg.Text("Result",size = (30,1), background_color = "white",text_color = "black", key = '-TEMPR-'),
			],
			[sg.T(size = (20,None)),sg.Button("Convert Temperature",key = '-TEMPC-')],



			####### LENGTH  ############

			[sg.T(size=(None, 3))],
			[   sg.Input("Enter length here",size = (20,1),key = '-LENI-'),
				sg.Combo(
				values = ["Convert Length","Feet to Inch","Feet to CM","Feet to Meter","Inch to Feet","Inch to CM","Inch to Meter","CM to Feet","CM to Inch","CM to Meter","Meter to Inch","Meter to Feet","Meter to CM","Meter to KM","Meter to Mile","KM to Mile","Mile to KM"],
				key = '-LEN-',
				default_value='Convert Mass',
				readonly = True,
				size = (20,None),
				enable_events=True
			),
			sg.Text("Result",size = (30,1), background_color = "white",text_color = "black",key = '-LENR-'),
			],
			[sg.T(size = (20,None)),sg.Button("Convert Length",key = '-LENC-')],



			####### AGE  ############

			[sg.T(size=(None, 5))],
			[   sg.Input("YYYY,MM,DD",size = (20,1),key = '-AGEI-',),
				sg.Combo(
				values = ["Current Age","Full Details","Years", "Days","Month"],
				key = '-AGE-',
				default_value='Calculate Age',
				readonly = True,
				size = (20,None),
				enable_events=True
			),
			sg.Text("Result",size = (30,1), background_color = "white",text_color = "black",key = '-AGER-',),
			],
			[sg.T(size = (20,None)),sg.Button("Calculate Age",key = '-AGEC-',)]







		],
		# background_color = "yellow",
		size = (800,800)
	)
	]
]

wiki = [
[
	sg.T(size=(50,None)),
	sg.Input(focus=True, key="_QUERY_"),
	sg.Button("Check if available"),
	sg.Button("search"),
],
[
	
	sg.Multiline(size=(250,600), key="_output_",background_color="black",font = ('Any', 14), text_color="white", pad=((10,10),(10,10))),
	
	
],
]

music = [[
	sg.Column(
		[
		[  sg.Column([ [
			sg.Button('Hello There\nHow are you',pad = ((20,20),(20,20)),disabled=True,image_filename=resource_path("jazz.png"),image_size=(600,500),font = 32,key = '-ALBUMART-')
			]
			],
			size = (650,550),element_justification='center',pad = ((20,20),(20,20)))
		],
		[sg.T(size = (25,None),background_color = "black"),
		sg.Button("previous", size=(10, 2), key = '-PREV-'),
		sg.Button("play", size=(10, 2),key = '-PLAY/PAUSE-'),
		sg.Button("Next", size=(10, 2),key = '-NEXT-'),
		
		],
		[
			sg.FolderBrowse(key="_GetFolder_", size = (85,2)),
		],
		[
			sg.Text("Song  Name", size=(85, 2), key="_SongName_",justification='center'),
		]

		],
		size = (700,800),
		background_color = "black"
	),
	sg.Column(
		[
			[
				sg.Text("We will add downloading song from youtube ui here but not now it will be after i complte the full app or will just be an extension",font = (None,23),size = (35,None), pad = ((10,10),(10,10)),background_color = "white",text_color = "black")
			]
		],
		size = (700,800),
		background_color = "white"
	)
	
	
	
]
	
		 
]



credits = [

	[
		sg.Column(
			[   [sg.T(size = (1400,12))],
				 [ sg.Column([[sg.Text("Language Used:",font = 'Any 12'),sg.T(size = (50,None),background_color = "lightBlue") ,sg.Text(packages[7],enable_events=True, font = 'Any 24',background_color = "lightBlue",text_color = "blue")]],size = (2400,50),background_color = "lightBlue")],
				 [sg.T(size = (1400,2))],
				[sg.Column([[sg.Text("External Packages Used:",font = 'Any 12')],
				[
				sg.T(size = (50,None),background_color = "lightBlue"),
				sg.Text(packages[0],enable_events=True,pad = ((10,10),(10,10)),background_color = "lightBlue",text_color = 'blue', font = 'Any 14') ,
				sg.Text(packages[1],enable_events=True,pad = ((10,10),(10,10)),background_color = "lightBlue",text_color = 'blue', font = 'Any 14'),
				# [sg.T(size = (5,None),background_color = "lightBlue"),
				sg.Text(packages[2],enable_events=True,pad = ((10,10),(10,10)),background_color = "lightBlue",text_color = 'blue', font = 'Any 14'),
				sg.Text(packages[3],enable_events=True,pad = ((10,10),(10,10)),background_color = "lightBlue",text_color = 'blue', font = 'Any 14'),
				],
				# [sg.T(size = (5,None),background_color = "lightBlue"),
				[
				sg.T(size = (50,None),background_color = "lightBlue"),
				sg.Text(packages[4],enable_events=True,pad = ((10,10),(10,10)),background_color = "lightBlue",text_color = 'blue', font = 'Any 14'),
				sg.Text(packages[5],enable_events=True,pad = ((10,10),(10,10)),background_color = "lightBlue",text_color = 'blue', font = 'Any 14'),
				
				sg.Text(packages[6],enable_events=True,pad = ((10,10),(10,10)),background_color = "lightBlue",text_color = 'blue', font = 'Any 14')
				]],size = (1400,120),background_color = "lightBlue"),],
				[sg.T(size = (1400,2))],
				[sg.Column([[sg.Text("Developed By:",font = 'Any 12'),sg.T(size = (50,None),background_color = "lightBlue") ,sg.Text(packages[8], enable_events=True,font = 'Any 24',background_color = "lightBlue",text_color = "blue")]],size = (1400,50),background_color = "lightBlue"),]

			 ]

			,size = (1400,800)),
		
   ]
]

# ---------------------------------------------------------------------- #
#                              GROUPING TABS                             #
# ---------------------------------------------------------------------- #


tab_group = [[
	sg.Tab('Main Page', default, key = '-DEFAULT-'),
	sg.Tab('Todo',todo, key = '-TODO-', visible = False),
	sg.Tab('Wiki', wiki, key = '-WIKI-', visible = False),
	sg.Tab('Calculator', calculator, key = '-CALC-', visible = False),
	sg.Tab('Music', music, key = '-MUSIC-', visible = False),
	sg.Tab("Credits",credits, key = '-CREDITS-',visible = True)
]]


layout = [[
	sg.TabGroup(tab_group, enable_events = True, key = '-TABGROUP-', selected_title_color='red')
]]



# ---------------------------------------------------------------------- #
#                           CREATING THE WINDOW                          #
# ---------------------------------------------------------------------- #


window = sg.Window("Student Utility App", layout, size=(1400, 800), no_titlebar = False)
tab_keys = ('-TODO-', '-WIKI-', '-CALC-', '-MUSIC-','-CREDITS-')


# ---------------------------------------------------------------------- #
#                               MAIN LOOP                                #
# ---------------------------------------------------------------------- #
try:
	while True:
		event, values = window.read(timeout = 1000)
		
		
		currentTime = time.asctime(time.localtime(time.time()))
		if event == sg.WIN_CLOSED:
			break
		if int(time.time()) - starting == waiting:
			event = "-NEXT-"
		
		#----------------------#
		#       Main Page      #
		#----------------------#
		window['-TIME-'].update(value = currentTime)
		if event == "ToDo" :
			window[tab_keys[0]].update(visible = True)
			try:
				cursor = cursor.execute("Select * from Todo")
				time.sleep(0.1)
				rows = cursor.fetchall()[::-1]
				if len(rows) >= 1:
					for index, row in enumerate(rows):
						if index == 95:
							break
						window[f"_Todo{index}_"].update(value=f"{row[0]}\n{row[1]}", visible = True)
						window[f"_Edit{index}_"].update(visible = True)
						window[f"_Del{index}_"].update(visible = True)
			except:
				pass
		if event == "Wikipedia":
			window[tab_keys[1]].update(visible = True)
			window["_output_"].update(value = "SEARCH ANYTHING")
		if event == "Calculator":
			window[tab_keys[2]].update(visible = True)
		if event == "Music":
			window[tab_keys[3]].update(visible = True)


		if event == "-SEARCH-":
			try:
				lst = news.getNews(values['-WL-'],values["-NL-"])
				window['-WEATHER-'].update(value = lst[1])

				for index, headline in enumerate(lst[0]):
					if index == 100:
						break
					window[f'NEWS{index}'].update(value=f"{headline[0]}\n{headline[1]} \n----------------------------------------------------------", visible = True)
			except:
				pass
	   

		if event == "Close All":
			window[tab_keys[0]].update(visible = False)
			window[tab_keys[1]].update(visible = False)
			window[tab_keys[2]].update(visible = False)
			window[tab_keys[3]].update(visible = False)
		#----------------------#
		#       Todo Page      #
		#----------------------#

		if event == "-ADDTODO-":
			try:
				if len(values["-todo-"]) > 1:
					cursor.execute(
					"INSERT INTO Todo VALUES (?,?)",
					(
						values["-todo-"],
						time.strftime("%a, %d %b %Y %T", time.localtime())
						
					),
				)
				connection.commit()
				cursor = cursor.execute("Select * from Todo")
				time.sleep(0.1)
				rows = cursor.fetchall()[::-1]
				if len(rows) >= 1:
					for index, row in enumerate(rows):
						if index == 95:
							break
						window[f"_Todo{index}_"].update(value=f"{row[0]}\n{row[1]}", visible = True)
						window[f"_Edit{index}_"].update(visible = True)
						window[f"_Del{index}_"].update(visible = True)
				   
			except:
				pass

		if event == '-RELOAD-':
		   
			try:
				cursor = connection.cursor()
				cursor = cursor.execute("Select * from Todo")
				time.sleep(0.1)
				rows = cursor.fetchall()[::-1]
				
				if len(rows) >= 1:
					for index, row in enumerate(rows):
						if index == 95:
							break
						window[f"_Todo{index}_"].update(value=f"{row[0]}\n{row[1]}", visible = True)
						window[f"_Edit{index}_"].update(visible = True)
						window[f"_Del{index}_"].update(visible = True)
				for index in range(len(rows),100):
					window[f"_Todo{index}_"].update(value="", visible = True)
					window[f"_Edit{index}_"].update(visible = False)
					window[f"_Del{index}_"].update(visible = False)
					
			except:
				pass

		
		if event in Del:
			try:
				if event[-3] != 'l':
					index = event[-3] + event[-2]
				else:
					index = int(event[-2])
				todo = values[f'_Todo{index}_'].split('\n')[0]
				addTime = values[f'_Todo{index}_'].split('\n')[1]

				cursor = connection.cursor()
				cursor.execute("DELETE FROM Todo WHERE todoName=:todo and addedTime=:addTime",{"todo":todo, "addTime":addTime})
				connection.commit()
				event = '-R-'
				window[f"_Todo{index}_"].update(value = "")
				window[f"_Edit{index}_"].update(visible=False)
				window[f"_Del{index}_"].update(visible=False)

			except:
				pass

		



		if event in Edit:
			if event[-3] != 't':
				index = event[-3] + event[-2]
			else:
				index = int(event[-2])
			try:
				todo1 = values[f'_Todo{index}_'].split('\n')
				todo2 = todo1[:-2]
				lTodo = ' '.join(todo2)
				lTime = values[f'_Todo{index}_'].split('\n')[-2]
			except:
				todo = "Not Found"
			window['-UPDATETODO-'].update(value = lTodo,visible = True)
			window['-SAVEUPDATE-'].update(visible = True)

		if event == '-SAVEUPDATE-':
			updatedTodo = values['-UPDATETODO-']
			
			updatedTime = time.strftime("%a, %d %b %Y %T", time.localtime())
			cursor = connection.cursor()
			cursor.execute("UPDATE Todo SET todoName=:updatedTodo , addedTime=:updatedTime WHERE todoName=:lTodo AND  addedTime=:lTime",{"updatedTodo":updatedTodo,"updatedTime":updatedTime, "lTodo": lTodo,"lTime":lTime})
			connection.commit()
			window['-UPDATETODO-'].update(visible = False)
			window['-SAVEUPDATE-'].update(visible = False)
			event = '-R-'



		if event == '-R-':
			try:
				cursor = connection.cursor()
				cursor = cursor.execute("Select * from Todo")
				time.sleep(0.1)
				rows = cursor.fetchall()[::-1]
				
				if len(rows) >= 1:
					for index, row in enumerate(rows):
						if index == 95:
							break
						window[f"_Todo{index}_"].update(value=f"{row[0]}\n{row[1]}", visible = True)
						window[f"_Edit{index}_"].update(visible = True)
						window[f"_Del{index}_"].update(visible = True)
				for index in range(len(rows),100):
					window[f"_Todo{index}_"].update(value="", visible = True)
					window[f"_Edit{index}_"].update(visible = False)
					window[f"_Del{index}_"].update(visible = False)
				
			   

			except:
				pass





		#----------------------#
		#       Wiki Page      #
		#----------------------#
		if event == "search":
			try:
				text = wikipedia.page(values["_QUERY_"]).content
			except:
				search = values["_QUERY_"]
				text = f"{search} Not Found"
			window["_output_"].update(value = text)

		if event == "Check if available":
			try:
				text = ",".join(wikipedia.search(values["_QUERY_"]))
			except:
				text = "Not Found"
			window["_output_"].update(value = text, font = 'Any 18')




		#----------------------#
		#       Calc Page      #
		#----------------------#
		if event in numbers:
			if entered == "Lets Calculate":
				entered = ""
			entered += event
			window["_INPUT_"].update(value=entered)
		if (
			event in operators
			and entered[-1] not in operators
			and entered != "Lets Calculate"
		):

			entered += event
			window["_INPUT_"].update(value=entered)
		if event == "C" and entered != "Lets Calculate":
			entered = entered[:-1]
			if entered == "":
				entered = "Lets Calculate"
				window["_INPUT_"].update(value=entered)
				continue

			window["_INPUT_"].update(value=entered)
		if event == "AC":
			entered = "Lets Calculate"
			window["_INPUT_"].update(value=entered)

		if event == "=":
			try:

				result = eval(entered.replace("x", "*"))
				window["_INPUT_"].update(value=result)

			except:
				window["_INPUT_"].update(value="ERRROR")
				entered = ""

		if event == ".":
			for index,char in enumerate(entered):
				if char in operators:
					count = index
			if count == 0 and '.' not in entered:
				entered += "."
				window["_INPUT_"].update(value=entered)
			elif "." not in entered[count+1:]:
				entered += "."
				window["_INPUT_"].update(value=entered)
		if event == "-NUMC-":
			result = converter.numericalConverter(values['-NUMI-'],values['-NUM-'])
			window['-NUMR-'].update(value = result)

		if event == "-TEMPC-":
			result = converter.tempConverter(values['-TEMPI-'],values['-TEMP-'])
			window['-TEMPR-'].update(value = result)

		if event == "-MASSC-":
			result = converter.massConverter(values['-MASSI-'],values['-MASS-'])
			window['-MASSR-'].update(value = result)

		if event == "-LENC-":
			result = converter.lenConverter(values['-LENI-'],values['-LEN-'])
			window['-LENR-'].update(value = result)

		if event == "-AGEC-":
			result = converter.ageConverter(values['-AGEI-'],values['-AGE-'])
			window['-AGER-'].update(value = result)







		#----------------------#
		#       Music Page      #
		#----------------------#
	
	
		if event == "-PLAY/PAUSE-":
			try:
				
				if status == None:
					for root, dirs, files in os.walk(values["_GetFolder_"]):
						for name in files:
							
							name = name.split('.')
							if name[-1] == 'mp3':
								playlist.append(values["_GetFolder_"] + "/" + '.'.join(name))
					window["_SongName_"].update(
						value=playlist[songNumber].split("/")[-1].split(".mp3")[0]
					)

					mixer.init()
					starting = int(time.time())
					mixer.music.load(playlist[songNumber])
					waiting = int(MP3(playlist[songNumber]).info.length)
					songNumber +=1 
					status = "playing"
					mixer.music.play()

				elif status == "playing":
					mixer.music.pause()
					status = "paused"

				elif status == "paused":
					mixer.music.unpause()
					status = "playing"
					
			except:
				pass
		
		if event == "-NEXT-" and status != None:
			if songNumber == len(playlist):
				songNumber = 0
			waiting = int(MP3(playlist[songNumber]).info.length)
			starting = int(time.time())
			mixer.music.load(playlist[songNumber])
			waiting = int(MP3(playlist[songNumber]).info.length)
			songNumber += 1
			status = "playing"
			mixer.music.play()
			window["_SongName_"].update(
						value=playlist[songNumber-1].split("/")[-1].split(".mp3")[0]
					)

		if event == '-PREV-' and status != None:
			songNumber -= 1
			if songNumber <= 0:
				songNumber = 0
			starting = int(time.time())
			mixer.music.load(playlist[songNumber])
			waiting = int(MP3(playlist[songNumber]).info.length)
			songNumber -= 1
			status = "playing"
			mixer.music.play()
			window["_SongName_"].update(
						value=playlist[songNumber].split("/")[-1].split(".mp3")[0]
					)


		 #----------------------#
		 #       Credits Page   #
		 #----------------------#


		if event in packages:
			try:
				webbrowser.open(links[event])
			except:
				pass

		
		

except :
	pass




# ---------------------------------------------------------------------- #
#                         DESTROYING THE WINDOW                          #
# ---------------------------------------------------------------------- #
window.close()
