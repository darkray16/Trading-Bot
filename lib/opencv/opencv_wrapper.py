import time, datetime, os, sys

#handle mouse control
import win32api, win32con, win32gui, win32ui, win32com

#user defined module that controls keyboard input and window focusing
import win32com.client

from cv import *
#from global_helpers import ApplicationHelper
#from ApplicationRegistry import *

from collections import namedtuple
Region = namedtuple("Region", "x y w h")

#threshold = ApplicationHelper.get_match_threshold("opencv")
threshold = 0.19

#images directory
dir = "database/Images/"
##DEBUG##
#dir = "c:/"

def get_image(filename):
    img_location = os.path.abspath(dir + filename)
    return LoadImage(img_location)

def focus(app):
    """
    app
        string name of window to change focus to
    
    brings the specified app to the foreground and set
    focus on it
    """
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.AppActivate(app)
    
def type(string, modifier=None):
    shell = win32com.client.Dispatch("WScript.Shell")
    if modifier is None:
        shell.SendKeys(string)
        
    else:
        pass
def click(coordinates=None, button="LEFT", smooth=False):
    """
    button
        string "LEFT" or "RIGHT", indicates which mouse button
        to depress
    coordinates
        string if supplied, then will be coordinates for the mouse click
        else mouse will click on its current position
    smooth
        boolean if supplied, will move the mouse in a smooth motion
        from its current location to the destination
    """
    win32api.SetCursorPos((coordinates["x"],coordinates["y"]))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,coordinates["x"],coordinates["y"],0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,coordinates["x"],coordinates["y"],0,0)

def drag(target, destination, button, speed):
    pass

def move(target, smooth=False):
    """
    target
        list that contains x, y coordinates to move mouse to
    """
    if smooth is False:
        win32api.SetCursorPos((target["x"], target["y"]))
    else:
        pass
        
def get_image_size(image):
    img_obj = LoadImage(os.path.abspath(dir + image))
    return GetSize(img_obj)
    
def get_region(image):
    """
    searches screen for image, then returns coordinates and dimensions
    of the image.  to be used with find commands to restrict where find
    operations are run
    """
    results = find_onscreen(image)
    w, h = GetSize( get_image(image) )
    region = Region( results["x"], results["y"], w, h)
    print str(region.x) + " " + str(region.y) + " " + str(region.w) + " " + str(region.h)
    return region
    
def create_canvas(filepath=None, region=None):
    """
    filepath
        string specified filepath for screen cap.  if None, then
        uses default location
    region
        dict returned by get_region method used to create a 
        canvas of only the area designated by region
    
    """
    hwnd = win32gui.GetDesktopWindow()
    if region is not None:
        w, h = region[2], region[3]
        #x, y is used later as both an offset, and decreases w, h of the image
        x, y = -(region[0]), -(region[1])
    else:
        region = win32gui.GetWindowRect(hwnd)
        x, y, w, h = -(region[0]), -(region[1]), region[2], region[3]
    rect = Region(x, y, w, h)

    #returns the device context, including entire window, toolbars, scrollbars, etc.
    wDC = win32gui.GetWindowDC(hwnd)

    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, rect.w, rect.h)
    cDC.SelectObject(dataBitMap)
    screen_width, screen_height = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
    cDC.BitBlt((rect.x, rect.y),(screen_width, screen_height) , dcObj, (0, 0), win32con.SRCCOPY)
    
    if isinstance( filepath, str ) :
        canvas_filepath = filepath
    else:
        canvas_filepath = "temp.png"
    dataBitMap.SaveBitmapFile(cDC, os.path.abspath(dir + canvas_filepath))
    time.sleep(1)
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    return canvas_filepath

def remove_temp_file(filepath=None):
    if filepath is None:
        os.remove(os.path.abspath(dir + "temp.png"))
    else:
        try:
            os.remove(os.path.abspath(filepath))
        except WindowsError:
            try:
                os.remove(os.path.abspath(dir + filepath))
            except:
                pass
    time.sleep(0.2)

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
    global threshold
    
    print "needle: " + needle
    print "haystack " + haystack
    needle = get_image(needle)
    haystack = get_image(haystack)
    W,H = GetSize(haystack)
    w,h = GetSize(needle)
    width = W - w + 1
    height = H - h + 1
    
    print "width: " + str(width) + ", height: " + str(height)
    result = CreateImage((width, height), 32, 1)
    MatchTemplate(needle, haystack, result, CV_TM_SQDIFF_NORMED)
    (min_x, max_y, minloc, maxloc) = MinMaxLoc(result)
    print str(min_x)
    
    if min_x < threshold:
        position = {"x":minloc[0], "y":minloc[1]}
        return position
    else:
        return False

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
    pass

def find_onscreen(needle, region=None):
    """
    needle
        image to search the screen for
    sub_region
        rect coordinates of the specific area the search
        should be narrowed down to
    returns position on screen of needle
    """
    haystack = create_canvas(region)
    result = find(haystack, needle, None)
    remove_temp_file(haystack)
    return result

def find_loop(pattern, region=None, timeout=180, rate=1):
    """
    pattern
        the area of screen to create haystack from, if None, then will search
        for any change in the area and return True when found
    region
        rect coordinates of area to narrow search to, if none, then will search entire screen
    rate
        float that controls the frequency of the scans in terms of
        seconds, increasing will use more resources
    timeout
        number of seconds to observe until loop break and returns None, if
        0 supplied, then goes on forever
    """
    started = datetime.datetime.now()
    screen = create_canvas(region)
    position = None
    while not position:
        if not timeout == 0:
            if datetime.datetime.now() - started > datetime.timedelta(seconds=timeout):
                break
        position = find(screen, pattern)
        time.sleep(rate)
        #new pointer assignment unnecessary as filepath remains, only file itself changes
        create_canvas(region)
        
    remove_temp_file(screen)
    return position
        
def observe(region=None, rate=0.3, timeout=180, callback=None, tolerance=None):
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
    tolerance
        float that changes the threshold for template matching. when you want the
        template matching to be more/less sensitive for a single operation.
    """
    global threshold
    if isinstance( tolerance, float ) :
        current_tol = threshold
        threshold = tolerance
        
    started = datetime.datetime.now()
    original = create_canvas(region=region)
    
    no_change = True
    while no_change:
        current = create_canvas(filepath="current.png", region=region)
        no_change = find(original, current)
        if datetime.datetime.now() - started > datetime.timedelta(seconds=timeout):
            break
        time.sleep(rate)
    
    ##DEBUG##
    #should be uncommented for live
    #remove_temp_file(screen)
    #remove_temp_file(current)
    
    if isinstance( tolerance, float ) :
        threshold = current_tol
        
    if no_change:
        return False
    else:
        return True
        
if __name__ == "__main__":
    if len(sys.argv) > 0:
        args = [ value for index, value in enumerate(sys.argv) if index > 1 ]
        print args
        m = globals()[sys.argv[1]]
        r = Region(463, 712, 396, 142)
        result = m(region = r)