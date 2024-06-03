import eel

eel.init('Gui')

@eel.expose
def App():
    print("Aplication is running")

App()

eel.start('index.html', size=(800, 600))