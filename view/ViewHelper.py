import threading, sys, os
from global_helpers import ApplicationHelper
gui_lib_path = ApplicationHelper.get_gui_lib()
vision_lib_path = ApplicationHelper.get_vision_lib()
sys.path.append(os.path.abspath("lib/" + gui_lib_path))
sys.path.append(os.path.abspath("lib/" + vision_lib_path))

gui_script = __import__(gui_lib_path + "_wrapper")
vision_script = __import__(vision_lib_path + "_wrapper")


def get_observe_rate():
    """
    return the rate at which observe should scan in float
    e.g. 0.3 means scan should be done every 0.3 sec
    """
    return 0.3

def click(coordinates=None, image=None, button="LEFT", smooth=False):
    #move the mouse to an area, then click
    if image and not coordinates:
        coordinates = vision_script.find_onscreen(image)
        #get the center of the image for mouse movement
        (w, h) = get_image_size(image)
        coordinates["x"] += w/2
        coordinates["y"] += h/2
    gui_script.click(coordinates=coordinates, button=button, smooth=smooth)

def get_image_size(image):
    return vision_script.get_image_size(image)
    
def type(text, modifier=None):
    #type in the message entered
    gui_script.type(text, modifier)

def key(key, modifier=None):
    #to send keyboard input for non-character key, e.g. key down
    gui_script.key(key, modifier)
    
def drag(coordinates, destination, button, speed):
    #speed indicates how quickly to drag to wait after 
    #reaching destination to release the button
    gui_script.drag(coordinates, destination, button, speed)

def find_onscreen(pattern, region=None):
    return vision_script.find_onscreen(needle=pattern, region=region)
    
def find(pattern, canvas=None):
    #searches the region for the given pattern
    if canvas is None:
        return vision_script.find_onscreen(pattern, None)
    return vision_script.find(needle=pattern, haystack=canvas)

def find_loop(region, pattern, timeout=0, rate=1.0):
    return vision_script.find_loop(pattern=pattern, region=region, timeout=timeout, rate=rate)
    
def lock_observe(region, timeout=180, tolerance=None):
    """
    returns True if there is any change in region, otherwise returns False
    """
    return vision_script.observe(region=region, 
        rate=get_observe_rate(), timeout=timeout, tolerance=tolerance)
        
def get_region(image):
    """
    will search screen for image, than return coordinates and dimensions of that image found
    as a dict. dict to be used with find functions to set the region to run find operations 
    with.
    """
    return vision_script.get_region(image=image)
    
def auto_observe(region, pattern, timeout, callback=None):
    #waits and observes an area for given pattern
    #will return location of pattern when found or timeout
    observe = Observer()
    
    def observer_wrapper():
        return vision_script.observe(needle=pattern, sub_region=region, 
            rate=ViewHelper.get_observe_rate(), timeout=timeout, callback=callback)
    observe.add_callable(observer_wrapper)
    
    location = observe.run()
    return location