#python

try:
    lx.eval("dialog.setup fileOpenMulti")
    lx.eval("dialog.title {Select some files to open}")
    lx.eval("dialog.result {myfile.txt}")

    lx.eval("dialog.open")
    filenames = lx.eval("dialog.result ?")

    for filename in filenames:
        lx.out(filename)

except:
    lx.out("User abort.")