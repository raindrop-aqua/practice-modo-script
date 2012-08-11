#python

wday = ("sun", "mon", "tue", "wed", "thu", "fri", "sat")
def cal0(n, m):
    s= ""
    for x in wday:
        s = s + " " + x
    lx.out(s)
    lx.out()
    s = ""
    for x in range(0, n):
        s = s + "  ---",
    lx.out(s)
    s = ""
    for x in range(1, m + 1):
        s = s + "%5d" %x
        if (x + n) % 7 == 0 : lx.out()
    lx.out(s)
    lx.out()

cal0(6, 31)
