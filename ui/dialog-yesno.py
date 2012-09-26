#python

try:
    lx.eval("dialog.setup yesNo")
    lx.eval("dialog.title {Confirm Operation}")
    lx.eval("dialog.msg {Perform the operation?}")
    lx.eval("dialog.result ok")

    lx.eval("dialog.open")
    lx.eval("dialog.result ?")

    lx.out("You selected Yes")

except:
    lx.out("You selected No")
