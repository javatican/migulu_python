from appJar import gui

def func1(button):
    if button=="Submit":
        print("username:", app.getEntry("user"), ", password:", app.getEntry("password"))
        app.infoBox("result","登入成功")
    else:
        app.stop()

app=gui()

app.addLabel("label1", "登入畫面",0,0,2)
app.addLabel("label2", "使用者名稱", 1,0)
app.addEntry("user",1,1)

app.addLabel("label3", "密碼", 2,0)
app.addSecretEntry("password",2,1)
#app.addButtons(["Submit","Cancel"], func1, 3,0,2)
app.addNamedButton("送出","Submit",func1,3,0)
app.addNamedButton("取消","Cancel",func1,3,1)
app.go()

