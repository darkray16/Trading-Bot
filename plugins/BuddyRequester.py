from sikuli.Sikuli import *
path_to_bot = getBundlePath().rsplit("\\", 1)[0] + "\\"

exec(open(path_to_bot + "ini.py", "rb").read())

sys.path.append(path_to_bot + "model")
sys.path.append(path_to_bot + "view")


class BuddyRequester(object):
    """
    BuddyRequester will make a call to MySQL
    db to get a list of all people who have pending
    transactions and will return that list of names
    """
    
    def request_buddy():
        
        return buddy_name
        
    def convert_buddy_name(name):
        pass