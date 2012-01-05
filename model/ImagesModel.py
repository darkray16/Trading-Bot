from sikuli.Sikuli import *

path_to_bot = getBundlePath().rsplit("\\", 1)[0] + "\\"

class ImagesModel(object):
    #stores the all images to be used by bot into tuples
    #used as a library object, primarily by the interface object
    """returns the images to be used for pixel search"""
    
    #image of blank area
    blank = "../Images/trade/blank.png"
    def get_blank(self):
        return self.blank
    
    #image of the ok button, e.g. after completing a trade
    ok_button = "../Images/ok_button.png"
    def get_ok_button(self):
        return self.ok_button
        
    #stores image of a ticket
    ticket =  "../Images/product/misc/ticket.png"
    
    def get_ticket(self):
        return self.ticket
        
    #stores image of a ticket text
    ticket_text = "../Images/product/misc/text/event_ticket_text.png"
    
    def get_ticket_text(self):
        return self.ticket_text
        
    amount = {1:"../Images/trade/context_menu/get_1.png", 4:"../Images/trade/context_menu/get_4.png", 10:"../Images/trade/context_menu/get_10.png", 32:"../Images/trade/context_menu/get_32.png"}
    def get_amount(self, amount):
        return self.amount[amount]
        
    #store images of each number in a tuple
    #the image for numbers depend on the context, e.g. number images in the giving window are different from the ones in collection or taking_window
    
    def get_number(self, number, category, phase=None):
        filepath = "../Images/numbers/" + str(category) + "/"
        if phase:
            filepath += str(phase) + "/"
        filepath += "number_" + str(number) + ".png"
        return filepath
    def get_all_numbers_as_dict(self, category, phase=None):
        numbers_list = dict((num, self.get_number(number=num, category=category, phase=phase)) for num in range(75) if num is not 0)
        return numbers_list  
          
    #stores images for the classified window
    classified = {'posting': "../Images/posting_text_area.png", 
                    "submit_posting": "../Images/submit_posting_button.png", 
                    'cancel_edit': "../Images/cancel_edit_button.png", 
                    'submit_edit': "../Images/submit_edit_button.png", 
                    'edit_posting': "../Images/edit_posting_button.png", 
                    "search_posts":"../Images/search_posts.png"}
    
    def get_classified(self, filename):
        return self.classified[filename]
    
    collection = {"export_to_csv": "../Images/collection/export_selected.png",
                  "explorer_file_path_bar": "../Images/collection/file_path_bar.png",
                  "explorer_file_name_bar": "../Images/collection/file_name_bar.png",
                  "explorer_save_button": "../Images/collection/save_button.png", 
                  "select_all": "../Images/collection/select_all.png",
                  "increase_tradability": "../Images/collection/increase_tradability.png",
                  "decrease_tradability": "../Images/collection/decrease_tradability.png",
                  "mark_all_tradable": "../Images/collection/mark_all_tradable.png",
                  "mark_all_untradable": "../Images/collection/mark_all_untradable.png",
                  "mark_selected_tradable_to": "../Images/collection/mark_selected_tradable_to.png",
                  "mark_all_beyond_4_tradable": "../Images/collection/mark_all_beyond_4_tradeable.png",
                  "import_trade_data": "../Images/collection/import_trade_data.png",
                  "list_view_collection_window":"../Images/collection/list_view_button_collection_window.png", 
                  "thumbnail_view_collection_window":"../Images/collection/thumbnail_view_button_collection_window.png",
                  "sort_by_name": "../Images/collection/sort_name.png",
                  "32": "../Images/collection/32.png", 
                  "10": "../Images/collection/10.png", 
                  "4": "../Images/collection/4.png", 
                  "3": "../Images/collection/3.png", 
                  "2": "../Images/collection/2.png", 
                  "1": "../Images/collection/1.png",
                  "search_button": "../Images/collection/search_button.png"}
    
    filters = {"version": {"all_versions": "../Images/filters/version/all_versions.png",
                                   "packs_tickets": "../Images/filters/version/packs_tickets.png",
                                   "premium": "../Images/filters/version/premium.png",
                                   "regular": "../Images/filters/version/regular.png"},
               "rarity": {"any": "../Images/filters/rarity/Any.png",
                          "common": "../Images/filters/rarity/Common.png",
                          "uncommon": "../Images/filters/rarity/Uncommon.png",
                          "rare": "../Images/filters/rarity/Rare.png",
                          "mythic": "../Images/filters/rarity/Mythic.png"},
               "set":{"scroll_down": "../Images/filters/set/scroll_down.png",
                      "scroll_up": "../Images/filters/set/scroll_up.png",
                      "Standard": "../Images/filters/set/Standard.png",
                      "Extended": "../Images/filters/set/Extended.png",
                      "Classic": "../Images/filters/set/Classic.png",
                      "Legacy": "../Images/filters/set/Legacy.png",
                      "Scars of Mirrodin": "../Images/filters/set/Scars of Mirrodin.png",
                      "Mirrodin Besieged": "../Images/filters/set/Mirrodin Besieged.png",
                      "Zendikar": "../Images/filters/set/Zendikar.png",
                      "Worldwake": "../Images/filters/set/Worldwake.png",
                      "Rise of the Eldrazi": "../Images/filters/set/Rise of the Eldrazi.png",
                      "Shards of Alara": "../Images/filters/set/Shards of Alara.png",
                      "Conflux": "../Images/filters/set/Conflux.png",
                      "Alara Reborn": "../Images/filters/set/Alara Reborn.png",
                      "Lorwyn": "../Images/filters/set/Lorwyn.png",
                      "Morningtide": "../Images/filters/set/Morningtide.png",
                      "Shadowmoor": "../Images/filters/set/Shadowmoor.png",
                      "Eventide": "../Images/filters/set/Eventide.png",
                      "Time Spiral": "../Images/filters/set/Time Spiral.png",
                      "Timeshifted": "../Images/filters/set/Timeshifted.png",
                      "Planar Chaos": "../Images/filters/set/Planar Chaos.png",
                      "Future Sight": "../Images/filters/set/Future Sight.png",
                      "Ice Age": "../Images/filters/set/Ice Age.png",
                      "Alliance": "../Images/filters/set/Alliance.png",
                      "Coldsnap": "../Images/filters/set/Coldsnap.png",
                      "Ravnica": "../Images/filters/set/Ravnica.png",
                      "Guildpact": "../Images/filters/set/Guildpact.png",
                      "Dissension": "../Images/filters/set/Dissension.png",
                      "Champions of Kamigawa": "../Images/filters/set/Champions of Kamigawa.png",
                      "Betrayers of Kamigawa": "../Images/filters/set/Betrayers of Kamigawa.png",
                      "Saviors of Kamigawa": "../Images/filters/set/Saviors of Kamigawa.png",
                      "Mirrodin": "../Images/filters/set/Mirrodin.png",
                      "Darksteel": "../Images/filters/set/Darksteel.png",
                      "Fifth Dawn": "../Images/filters/set/Fifth Dawn.png",
                      "Onslaught": "../Images/filters/set/Onslaught.png",
                      "Legion": "../Images/filters/set/Legion.png",
                      "Scourge": "../Images/filters/set/Scourge.png",
                      "Odyssey": "../Images/filters/set/Odyssey.png",
                      "Torment": "../Images/filters/set/Torment.png",
                      "Judgment": "../Images/filters/set/Judgment.png",
                      "Invasion": "../Images/filters/set/Invasion.png",
                      "Planeshift": "../Images/filters/set/Planeshift.png",
                      "Apocalypse": "../Images/filters/set/Apocalypse.png",
                      "Urza's Saga": "../Images/filters/set/Urza's Saga.png",
                      "Urza's Legacy": "../Images/filters/set/Urza's Legacy.png",
                      "Urza's Destiny": "../Images/filters/set/Urza's Destiny.png",
                      "Tempest": "../Images/filters/set/Tempest.png",
                      "Stronghold": "../Images/filters/set/Stronghold.png",
                      "Exodus": "../Images/filters/set/Exodus.png",
                      "Mirage": "../Images/filters/set/Mirage.png",
                      "Visions": "../Images/filters/set/Visions.png",
                      "Weatherlight": "../Images/filters/set/Weatherlight.png",
                      "Seventh Edition": "../Images/filters/set/Seventh Edition.png",
                      "Eighth Edition": "../Images/filters/set/Eighth Edition.png",
                      "Ninth Edition": "../Images/filters/set/Ninth Edition.png",
                      "Tenth Edition": "../Images/filters/set/Tenth Edition.png",
                      "Magic 2010": "../Images/filters/set/Magic 2010.png",
                      "Magic 2011": "../Images/filters/set/Magic 2011.png",
                      "Masters Edition": "../Images/filters/set/Masters Edition.png",
                      "Masters Edition II": "../Images/filters/set/Masters Edition II.png",
                      "Masters Edition III": "../Images/filters/set/Masters Edition III.png",
                      "Masters Edition IV":"../Images/filters/set/Masters Edition IV.png"}}
    
    #stores the screencaps for trade window
    trade = {"confirm":{"confirm_button":"../Images/trade/confirm_window/confirm_button_confirm.png", 
                        "confirm_cancel":"../Images/trade/confirm_window/confirm_cancel.png", 
                        "rarity":{"mythic": "../Images/trade/confirm_window/Mythic.png",
                                  "rare": "../Images/trade/confirm_window/Rare.png",
                                  "uncommon": "../Images/trade/confirm_window/Uncommon.png",
                                  "common": "../Images/trade/confirm_window/Common.png",
                                  "none": "../Images/trade/confirm_window/None.png"}}, 
           "canceled_trade": "../Images/trade/canceled_trade.png", 
           "empty": "../Images/trade/empty.png",
           "sort_name": "../Images/trade/sort_name.png", 
           "list_view_collection_window":"../Images/trade/list_view_button_collection_window.png", 
           "thumbnail_view_collection_window":"../Images/trade/thumbnail_view_button_collection_window.png", 
           "confirm_button":"../Images/trade/confirm_button.png", 
           "cancel_trade":"../Images/trade/cancel_trade.png", 
           "incoming_request": "../Images/incoming_request.png", 
           "yes_button": "../Images/yes_button.png",  
           "turn_right": "../Images/turn_right.png", 
           "turn_left": "../Images/turn_left.png",
           "giving_window":"../Images/trade/products_giving.png", 
           "taking_window":"../Images/trade/products_taking.png", 
           "scroll_bar_regular":"../Images/trade/scroll_bar_regular.png", 
           "scroll_bar_mini":"../Images/trade/scroll_bar_mini.png"}
    
    def get_trade(self, filename, *subsection):
        if len(subsection) == 0:
            return self.trade[filename]
        elif len(subsection) == 1:
            return self.trade[subsection[0]][filename]
        elif len(subsection) == 2:
            return self.trade[subsection[0]][subsection[1]][filename]
            
    #stores the screencaps for chat window
    chat = {"minimize":"../Images/chat/minimize_button.png", 
              "expand_close":"../Images/chat/expand_close_button.png", 
              "type_area":"../Images/chat/type_area.png", 
              "buddies": "../Images/buddies_tab.png", 
              'my_cart': "../Images/my_cart_tab.png", 
              'games': "../Images/games_tab.png", 
              'card': "../Images/card_tab.png", 
              'text':{"done":"../Images/chat/text/done.png"}}
    def get_chat_text(self, filename):
        return self.chat['text'][filename]
    def get_chat_window(self, filename):
        return self.chat[filename]
    
    #stores the images of each card
    cards = {}
    def get_cards(self, filename=None):
        if filename:
            return self.cards[filename]
        else:
            return self.cards
    
    #card images
    card_names_list = {"M11": {"Primeval Titan":""}, 
                    "ME4": {},
                    "MBS": {"Tezzeret, Agent of Bolas": ""},
                    "ROE": {"Gideon Jura": ""},
                    "SOM": {"Venser, the Sojourner": ""},
                    "WWK": {"Jace, the Mind Sculptor": ""},  
                    "ZEN": {"":""}}
                    
    def get_card_text(self, phase, cardname):
        #if can't find png file for cardname in one phase, try other phase, most cards are the same except for longer names
        try:
            card = open(path_to_bot + "Images/product/cards/text/" + phase + "/" + cardname.lower() + ".png", "r")
        except IOError:
            try:
                if phase == "confirm":
                    alt_path = "preconfirm"
                else:
                    alt_path = "confirm"
                card = open(path_to_bot + "Images/product/cards/text/" + alt_path + "/" + cardname.lower() + ".png", "r")
            except IOError:
                raise Exception("PNG file for " + cardname.lower() + " text not found.")
            else:
                card.close()
                filepath = "../Images/product/cards/text/" + alt_path + "/" + cardname.lower() + ".png"
                return filepath
        else:
            card.close()
            filepath = "../Images/product/cards/text/" + phase + "/" + cardname.lower() + ".png"
            return filepath
            
    def get_card_image(self, set, cardname):
        try:
            card = open(path_to_bot + "Images/product/cards/img/" + phase + "/" + cardname.lower() + ".png", "r")
        except IOError:
            raise Exception("PNG file for " + cardname + " image not found")
        else:
            card.close()
            filepath = "../Images/product/cards/img/" + phase + "/" + cardname.lower() + ".png"
            return filepath
    
    card_names_list = ["Primeval Titan", "Tezzeret, Agent of Bolas", "Gideon Jura", "Venser, the Sojourner", "Jace, the Mind Sculptor"]
    
    def get_card_keys(self):
        return self.card_names_list
    def get_pack_text(self, phase, packname):
        try:
            pack = open(path_to_bot + "Images/product/packs/text/" + phase + "/" + packname.lower() + ".png", "r")
        except IOError:
            print(path_to_bot + "Images/product/packs/text/" + phase + "/" + packname.lower() + ".png" + " not found")
            raise KeyError(packname + " not found")
        else:
            pack.close()
            filepath = "../Images/product/packs/text/" + phase + "/" + packname.lower() + ".png"
            return filepath

    def get_all_pack_text_as_dict(self, phase):
        packs_dict = dict((abbr, self.get_packs_text(phase=phase, packname=abbr)) for abbr in self.__pack_names_list)
        return packs_dict
    
    def get_pack_image(self, packname):
        try:
            pack = open(path_to_bot + "/Images/product/packs/img/" + packname.lower() + ".png", "r")
        except:
            raise KeyError(packname + " not found")
        else:
            pack.close()
            filepath = "../Images/product/packs/" + packname.lower() + ".png"
            return filepath
        
    def get_all_pack_image_as_dict(self):
        packs_dict = dict((abbr, self.get_packs_image(abbr)) for abbr in self.__pack_names_list)
        return packs_dict
        
    #stores image of login screen
    login = {'password_field': "../Images/password_field.png" , 
               'login_success': "../Images/login_success.png" , 
               'login_fail': "../Images/login_fail.png" , 
               'login_button': "../Images/login_button.png" }
    def get_login(self, filename):
        return self.login[filename]
    
    #stores image of menu options
    menu = {'community': "../Images/community_button.png", 
              'menu': "../Images/menu_button.png", 
              'collection': "../Images/collection_button.png", 
              'home': "../Images/home_button.png", 
              'marketplace': "../Images/marketplace_button.png", 
              'classified': "../Images/classified_button.png"}
    def get_menu(self, filename):
        return self.menu[filename]