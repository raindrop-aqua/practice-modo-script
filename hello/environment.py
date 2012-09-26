#python

commands = [
    # Licensing.
    "query platformservice licensedto ?",
    "query platformservice expiresin ?",
    #"query platformservice serialnum ?", # output error message => invalid attribute
    "query platformservice numlicenses ?",
    # Application Information.
    "query platformservice appname ?",
    "query platformservice appversion ?",
    "query platformservice appbuild ?",
    "query platformservice isapp64bit ?",
    # Headless Operation
    "query platformservice isheadless ?",
    # Operationg System Information
    "query platformservice ostype ?",
    "query platformservice osname ?",
    "query platformservice osversion ?",
    # paths.path
    "query platformservice path.path ? current",
    "query platformservice path.path ? cwd",
    "query platformservice path.path ? program",
    "query platformservice path.path ? exename",
    "query platformservice path.path ? project",
    "query platformservice path.path ? temp",
    "query platformservice path.path ? license",
    "query platformservice path.path ? headless",
    "query platformservice path.path ? headless32",
    "query platformservice path.path ? help",
    "query platformservice path.path ? module",
    "query platformservice path.path ? resource",
    "query platformservice path.path ? prefs",
    "query platformservice path.path ? user",
    "query platformservice path.path ? content",
    "query platformservice path.path ? asset",
    "query platformservice path.path ? configs",
    "query platformservice path.path ? scripts",
    "query platformservice path.path ? documents",
    "query platformservice path.path ? configname",
    # importpaths
    "query platformservice importpaths ?",
]

def exe(command):
    result = ""
    try:
        result = lx.eval(command)
    except:
        pass
    lx.out("%s => %s" % (command, result))


for command in commands:
    exe(command)
