#python

try:
    lx.eval("dialog.setup fileOpen")
    lx.eval("dialog.title {Select a file to open}")
    lx.eval("dialog.result {myfile.txt}")

    lx.eval("dialog.open")
    filename = lx.eval("dialog.result ?")

    lx.out(filename)

except:
    lx.out("User abort.")
