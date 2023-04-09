import PySimpleGUI as sg
import pyautogui as pg
import time
import keyboard

layout = [
	[sg.Push(), sg.Text('OP BOT Copy V. 0.02b'), sg.Push()],
	[sg.Frame('Click Interval', 
	layout = [
	[sg.Input('0', key ='-IN_HOURS-', size = (4, 10)), sg.Text('hours'), 
	sg.Input('0', key ='-IN_MINS-', size = (4,10)), sg.Text('minutes'), 
	sg.Input('0', key ='-IN_SECS-', size = (4,10)), sg.Text('secs'), 
	sg.Input('0', key ='-IN_MILI-', size = (4,10)), sg.Text('milisecs')]])],
	[sg.Frame('Click Options', 
	layout = [
	[sg.Text('Mouse Button'), sg.Combo(values = ('left', 'middle', 'right'), default_value = 'left', key ='-BUTTON_LIST-')]]), 
	sg.Frame('Click Repeat', 
	layout = [
        [sg.Radio('Repeat', 'RADIO1', default = False, key = '-REPEAT-'), sg.Input('1', key = '-TIMES-', size = (4,10)) , sg.Text('Times')],
        [sg.Radio('Dont Repeat', 'RADIO1', default = True)]])],
	[sg.Text('Set Location'), 
	sg.Input('0', key ='-XXX-', size = (4, 10)), sg.Text('X'), 
	sg.Input('0', key ='-YYY-', size = (4, 10)), sg.Text('Y'), 
	sg.Button('Pick Location on Screen\n (Wait 3 Seconds)', key = '-PICK-', size = (20, 5)) ],
	[sg.Push(), sg.Button('Start\n(F6)', key = '-START-', size = (8, 4)), sg.Button('Stop\n(F7)', key = '-STOP-', size = (8, 4)), sg.Push(), sg.Quit()]
	]

window = sg.Window('OP BOT Copy', layout)

var_start = False

while True:
	event, values = window.read(timeout = 10)
	if event in (sg.WIN_CLOSED, 'Quit'):
		break
	if event == '-PICK-':
		time.sleep(3)		
		x, y = pg.position()
		window['-XXX-'].update(f'{x}')
		window['-YYY-'].update(f'{y}')
	if event == '-STOP-' or keyboard.is_pressed('F7'):
		var_start = False
	
	if event == '-START-' or keyboard.is_pressed('F6'):
		var_start = True
		init_time = time.time()
		times = int(values['-TIMES-'])
		total = 0
		x = int(values['-XXX-'])
		y = int(values['-YYY-'])
		interval = (0.001*int(values['-IN_MILI-'])) + int(values['-IN_SECS-']) + (60*int(values['-IN_MINS-'])) + (3600*int(values['-IN_HOURS-']))
	if var_start:
		current_time = time.time()
		if values['-REPEAT-']:
			print(current_time - init_time)
			if int(current_time - init_time) == interval:
				init_time = time.time()
				pg.click(x, y, button=values['-BUTTON_LIST-'])
				total += 1
				if total == times:
					var_start = False
		else:
			if int(current_time - init_time) == interval:
				init_time = time.time()
				pg.click(x, y)
window.close()
