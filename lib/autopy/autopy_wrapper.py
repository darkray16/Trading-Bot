import autopy, time, datetime, os

def get_img_path(filename):
    img_location = os.path.abspath("database/Images/" + filename)
    print img_location
    return autopy.bitmap.Bitmap.open(img_location)

def click(coordinates, button, smooth=False):
    """
    coordinates
        dict object with indices x, y as locations for click event
    button
        str that is "LEFT" or "RIGHT"
    """
    mouse_button = getattr(autopy.mouse, str(button) + "_BUTTON")
    
    if smooth:
        autopy.mouse.smooth_move(coordinates["x"], coordinates["y"])
        autopy.mouse.click(mouse_button)
    else:
        autopy.mouse.move(coordinates["x"], coordinates["y"])
        time.sleep(0.1)
        autopy.mouse.click(mouse_button)
    
def type(text, key_modifier=None):
    if key_modifier is None:
        autopy.key.type_string(text)
    else:
        modifier = getattr(autopy.key, "MOD_" + str(key_modifier))
        autopy.key.tap(text, modifier)

def key(key, key_modifier=None):
    key = getattr(autopy.key, "K_" + str(key))
    if key_modifier is not None:
        modifier = getattr(autopy.key, "MOD_" + str(key_modifier).upper())
        autopy.key.tap(key, modifier)
    else:   
        autopy.key.tap(key)
        
def drag(target, destination, button, speed):
    autopy.mouse.move(target["x"], target["y"])
    autopy.mouse.smooth_move(destination.x, destination.y)

def move(target, smooth=False):
    if smooth:
        autopy.mouse.smooth_move(target["x"], target["y"])
    else:
        autopy.mouse.move(target["x"], target["y"])

def create_canvas():
    """
    to be used with all find operations that scan
    the current screen, restricting the canvas to the
    region occupied by the client app
    """
    ##DEBUG##
    #...create rect for app area of screen = app_region
    app_region = None
    canvas = autopy.bitmap.capture_screen(app_region)
    return canvas

def find(haystack, needle, offset=None):
    """
    haystack
        string of filename of image file to be used
        as a canvas
    needle
        string of filename of image file to search the
        canvas for
    offset
        future update
        
    returns tuple of (x,y) coordinates if found, None otherwise
    """
    canvas = autopy.bitmap.Bitmap.open(haystack)
    target = autopy.bitmap.Bitmap.open(needle)

    results = canvas.find_bitmap(target)
    position = {"x": results[0], "y": results[1]}
    return position

def find_all(haystack, needle, offset=None):
    """
    haystack
        string of filename of image file to be used
        as a canvas
    needle
        string of filename of image file to search the
        canvas for
    offset
        future update
        
    returns list of (x,y) tuples of all instances found
    """
    canvas = autopy.bitmap.Bitmap.open(haystack)
    target = autopy.bitmap.Bitmap.open(needle)
    
    positions = canvas.find_every_bitmap(target)
    return positions

def find_onscreen(needle, sub_region=None):
    """
    needle
        image to search the screen for
    sub_region
        rect coordinates of the specific area the search
        should be narrowed down to
    returns position on screen of needle
    """
    needle = get_img_path(needle)
    position = None
    screen = create_canvas()
    res = screen.find_bitmap(needle, 0.0, sub_region)
    position = {"x": res[0], "y":res[1]}
    return position

def find_loop(needle=None, region=None, rate=1.0, timeout=0, callback=None):
    """
    needle
        image to search the screen for, if None, then will search
        for any change in the area and return True when found
    region
        rect coordinates of area to narrow search to
    rate
        float that controls the frequency of the scans in terms of
        seconds, increasing will use more resources
    timeout
        number of seconds to observe until loop break and returns None
    callback
        function to call if timeout is reached, if not passed, then this function
        instead returns None
    """
    started = datetime.datetime.now()
    screen = create_canvas()
    position = None
    while not position:
        position = screen.find_bitmap(needle, rect=region)
        if datetime.datetime.now() - started > datetime.timedelta(seconds=timeout):
            break
        time.sleep(rate)
    
    if position and callback:
        callback()
    else:
        return position
        
def observe(region=None, rate=1.0, timeout=0, callback=None):
    """
    region
        rect coordinates of area to narrow search to
    rate
        float that controls the frequency of the scans in terms of
        seconds, increasing will use more resources
    timeout
        number of seconds to observe until loop break and returns None
    callback
        function to call if timeout is reached, if not passed, then this function
        instead returns None
    """
    started = datetime.datetime.now()
    screen = create_canvas()
    
    no_change = True
    while no_change:
        needle = create_canvas()
        nochange = screen.find_bitmap(needle, rect=region)
        if datetime.datetime.now() - started > datetime.timedelta(seconds=timeout):
            break
        time.sleep(rate)
        
    if no_change:
        return False
    else:
        return True