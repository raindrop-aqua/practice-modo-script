#python

try:
    lx.eval("dialog.setup fileSave")
    lx.eval("dialog.title {Save file}")
    lx.eval("dialog.fileType image")
    lx.eval("dialog.fileSaveFormat tga extension")

    lx.eval("dialog.open")
    filename = lx.eval("dialog.result ?")
    format = lx.eval("dialog.fileSaveFormat ? format")
    extension = lx.eval("dialog.fileSaveFormat ? extension")

    lx.out(filename)
    lx.out(format)
    lx.out(extension)

except:
    lx.out("User abort.")