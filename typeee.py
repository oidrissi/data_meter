from ctypes import windll, Structure, c_long, byref


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]



def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}

def idle():
    pos = queryMousePosition()
    time.sleep(30)
    pos2 = queryMousePosition()
    if pos == pos2:
        return True
    
idle()
print(pos)