from src.Scene import Scene
import tkinter

root = tkinter.Tk()  # створюємо головне вікно програми
scene = Scene(root,
              width=800,  # ширина віджета у пікселях
              height=600)  # висота віджета у пікселях
scene.pack()

scene.addShip()
scene.setShipPosition(100, 100)
scene.update()


root.mainloop()
