import ViewHelper
from View import *

class ChatView(View):

    def __ini__(self):
        super(ChatView, self).__ini__(self)
        
    def send_msg(self, msg):
        """
        msg
            string to be sent
        """
        pass
        
    def wait_for_msg(self, msg_img):
        """
        msg_img
            an image of the text to wait for
        """
        pass
        
    def close_current_chat(self):
        pass
        
    def minimize_current_chat(self):
        pass
        
    def close_all_chat(self):
        pass
        
    def minimize_all_chat(self):
        pass
    