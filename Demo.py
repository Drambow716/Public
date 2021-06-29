from pywinauto import application 
import time 

app = application.Application()
app.Start("Notepad.exe")
time.sleep(1)
app.Notepad.edit.TypeKeys("Fuck")
app.Notepad.edit.TypeKeys(" ")
app.Notepad.edit.TypeKeys("You")
time.sleep(1)
app.Notepad.MenuSelect("File -> SaveAs")
app.SaveAs.edit.SetText("pywinautodemo.txt")
app.SaveAs.Save.Click()
app.Notepad.MenuSelect("File -> Exit")