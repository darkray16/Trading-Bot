import os
current_path = os.path.realpath(__file__)

image_path = current_path + "/"

states = {"login":"...",
          "lobby":"...",
          "trade_request":"...",
          "mid_trade":"...",
          "mid_game":"..."
          }

amount = {1:"trade/context_menu/get_1.png", 4:"trade/context_menu/get_4.png", 10:"trade/context_menu/get_10.png", 32:"trade/context_menu/get_32.png"}
collection = {"export_to_csv": "collection/export_selected.png",
              "explorer_file_path_bar": "collection/file_path_bar.png",
              "explorer_file_name_bar": "collection/file_name_bar.png",
              "explorer_save_button": "collection/save_button.png", 
              "select_all": "collection/select_all.png",
              "increase_tradability": "collection/increase_tradability.png",
              "decrease_tradability": "collection/decrease_tradability.png",
              "mark_all_tradable": "collection/mark_all_tradable.png",
              "mark_all_untradable": "collection/mark_all_untradable.png",
              "mark_selected_tradable_to": "collection/mark_selected_tradable_to.png",
              "mark_all_beyond_4_tradable": "collection/mark_all_beyond_4_tradeable.png",
              "import_trade_data": "collection/import_trade_data.png",
              "list_view_collection_window":"collection/list_view_button_collection_window.png", 
              "thumbnail_view_collection_window":"collection/thumbnail_view_button_collection_window.png",
              "sort_by_name": "collection/sort_name.png",
              "32": "collection/32.png", 
              "10": "collection/10.png", 
              "4": "collection/4.png", 
              "3": "collection/3.png", 
              "2": "collection/2.png", 
              "1": "collection/1.png",
              "search_button": "collection/search_button.png"}
filters = {"version": {"all_versions": "filters/version/all_versions.png",
                               "packs_tickets": "filters/version/packs_tickets.png",
                               "premium": "filters/version/premium.png",
                               "regular": "filters/version/regular.png"},
           "rarity": {"any": "filters/rarity/Any.png",
                      "common": "filters/rarity/Common.png",
                      "uncommon": "filters/rarity/Uncommon.png",
                      "rare": "filters/rarity/Rare.png",
                      "mythic": "filters/rarity/Mythic.png"},
           "set":{"scroll_down": "filters/set/scroll_down.png",
                  "scroll_up": "filters/set/scroll_up.png",
                  "Standard": "filters/set/Standard.png",
                  "Extended": "filters/set/Extended.png",
                  "Classic": "filters/set/Classic.png",
                  "Legacy": "filters/set/Legacy.png",
                  "Scars of Mirrodin": "filters/set/Scars of Mirrodin.png",
                  "Mirrodin Besieged": "filters/set/Mirrodin Besieged.png",
                  "Zendikar": "filters/set/Zendikar.png",
                  "Worldwake": "filters/set/Worldwake.png",
                  "Rise of the Eldrazi": "filters/set/Rise of the Eldrazi.png",
                  "Shards of Alara": "filters/set/Shards of Alara.png",
                  "Conflux": "filters/set/Conflux.png",
                  "Alara Reborn": "filters/set/Alara Reborn.png",
                  "Lorwyn": "filters/set/Lorwyn.png",
                  "Morningtide": "filters/set/Morningtide.png",
                  "Shadowmoor": "filters/set/Shadowmoor.png",
                  "Eventide": "filters/set/Eventide.png",
                  "Time Spiral": "filters/set/Time Spiral.png",
                  "Timeshifted": "filters/set/Timeshifted.png",
                  "Planar Chaos": "filters/set/Planar Chaos.png",
                  "Future Sight": "filters/set/Future Sight.png",
                  "Ice Age": "filters/set/Ice Age.png",
                  "Alliance": "filters/set/Alliance.png",
                  "Coldsnap": "filters/set/Coldsnap.png",
                  "Ravnica": "filters/set/Ravnica.png",
                  "Guildpact": "filters/set/Guildpact.png",
                  "Dissension": "filters/set/Dissension.png",
                  "Champions of Kamigawa": "filters/set/Champions of Kamigawa.png",
                  "Betrayers of Kamigawa": "filters/set/Betrayers of Kamigawa.png",
                  "Saviors of Kamigawa": "filters/set/Saviors of Kamigawa.png",
                  "Mirrodin": "filters/set/Mirrodin.png",
                  "Darksteel": "filters/set/Darksteel.png",
                  "Fifth Dawn": "filters/set/Fifth Dawn.png",
                  "Onslaught": "filters/set/Onslaught.png",
                  "Legion": "filters/set/Legion.png",
                  "Scourge": "filters/set/Scourge.png",
                  "Odyssey": "filters/set/Odyssey.png",
                  "Torment": "filters/set/Torment.png",
                  "Judgment": "filters/set/Judgment.png",
                  "Invasion": "filters/set/Invasion.png",
                  "Planeshift": "filters/set/Planeshift.png",
                  "Apocalypse": "filters/set/Apocalypse.png",
                  "Urza's Saga": "filters/set/Urza's Saga.png",
                  "Urza's Legacy": "filters/set/Urza's Legacy.png",
                  "Urza's Destiny": "filters/set/Urza's Destiny.png",
                  "Tempest": "filters/set/Tempest.png",
                  "Stronghold": "filters/set/Stronghold.png",
                  "Exodus": "filters/set/Exodus.png",
                  "Mirage": "filters/set/Mirage.png",
                  "Visions": "filters/set/Visions.png",
                  "Weatherlight": "filters/set/Weatherlight.png",
                  "Seventh Edition": "filters/set/Seventh Edition.png",
                  "Eighth Edition": "filters/set/Eighth Edition.png",
                  "Ninth Edition": "filters/set/Ninth Edition.png",
                  "Tenth Edition": "filters/set/Tenth Edition.png",
                  "Magic 2010": "filters/set/Magic 2010.png",
                  "Magic 2011": "filters/set/Magic 2011.png",
                  "Magic 2012": "filters/set/Magic 2012.png",
                  "Masters Edition": "filters/set/Masters Edition.png",
                  "Masters Edition II": "filters/set/Masters Edition II.png",
                  "Masters Edition III": "filters/set/Masters Edition III.png",
                  "Masters Edition IV":"filters/set/Masters Edition IV.png"}}
#stores the screencaps for trade window
trade = {"confirm":{"confirm_button":"trade/confirm_window/confirm_button_confirm.png", 
                    "confirm_cancel":"trade/confirm_window/confirm_cancel.png", 
                    "rarity":{"mythic": "trade/confirm_window/Mythic.png",
                              "rare": "trade/confirm_window/Rare.png",
                              "uncommon": "trade/confirm_window/Uncommon.png",
                              "common": "trade/confirm_window/Common.png",
                              "none": "trade/confirm_window/None.png"}}, 
       "search_button": "trade/search_button.png",
       "canceled_trade": "trade/canceled_trade.png", 
       "empty": "trade/empty.png",
       "sort_name": "trade/sort_name.png", 
       "list_view_collection_window":"trade/list_view_button_collection_window.png", 
       "thumbnail_view_collection_window":"trade/thumbnail_view_button_collection_window.png", 
       "confirm_button":"trade/confirm_button.png", 
       "cancel_trade":"trade/cancel_trade.png", 
       "incoming_request": "incoming_request.png", 
       "yes_button": "yes_button.png",  
       "turn_right": "turn_right.png", 
       "turn_left": "turn_left.png",
       "giving_window":"trade/products_giving.png", 
       "taking_window":"trade/products_taking.png", 
       "scroll_bar_regular":"trade/scroll_bar_regular.png", 
       "scroll_bar_mini":"trade/scroll_bar_mini.png"}
#image of the ok button, e.g. after completing a trade
ok_button = "ok_button.png"
#stores image of a ticket
ticket =  "product/misc/ticket.png"
#stores image of a ticket text
ticket_text = "product/misc/text/event_ticket_text.png"
#image of blank slot in the trade windows
blank = "trade/blank.png"
#stores images for the classified window
classified = {'posting': "posting_text_area.png", 
                "submit_posting": "submit_posting_button.png", 
                'cancel_edit': "cancel_edit_button.png", 
                'submit_edit': "submit_edit_button.png", 
                'edit_posting': "edit_posting_button.png", 
                "search_posts":"search_posts.png"}
#stores the screencaps for chat window
chat = {"minimize":"chat/minimize_button.png", 
          "expand_close":"chat/expand_close_button.png", 
          "type_area":"chat/type_area.png", 
          "buddies": "buddies_tab.png", 
          'my_cart': "my_cart_tab.png", 
          'games': "games_tab.png", 
          'card': "card_tab.png", 
          'text':{"done":"chat/text/done.png"}}
menu = {'community': "community_button.png", 
          'menu': "menu_button.png", 
          'collection': "collection_button.png", 
          'home': "home_button.png", 
          'marketplace': "marketplace_button.png", 
          'classified': "classified_button.png"}
login = {'password_field': "password_field.png" , 
           'login_success': "login_success.png" , 
           'login_fail': "login_fail.png" , 
           'login_button': "login_button.png" }

card_names_list = ["Primeval Titan", "Tezzeret, Agent of Bolas", "Gideon Jura", "Venser, the Sojourner", "Jace, the Mind Sculptor"]

#card images
card_names_list = {"M11": {"Primeval Titan":""}, 
                "ME4": {},
                "MBS": {"Tezzeret, Agent of Bolas": ""},
                "ROE": {"Gideon Jura": ""},
                "SOM": {"Venser, the Sojourner": ""},
                "WWK": {"Jace, the Mind Sculptor": ""},  
                "ZEN": {"":""}}
#stores the images of each card
cards = {}


def get_filter(filter, value):
    return filters[filter][value]

def get_client_state():
    return states

def get_blank():
    return blank

def get_ok_button():
    return ok_button

def get_ticket():
    return ticket

def get_ticket_text():
    return ticket_text

def get_amount(amount):
    return amount[amount]

def get_number(number, category, phase=None):
    filepath = "numbers/" + str(category) + "/"
    if phase:
        filepath += str(phase) + "/"
    filepath += "number_" + str(number) + ".png"
    return filepath

def get_all_numbers_as_dict(category, phase=None):
    numbers_list = dict((num, get_number(number=num, category=category, phase=phase)) for num in range(75) if num is not 0)
    return numbers_list

def get_classified(filename):
    return classified[filename]

def get_trade(filename, *subsection):
    if len(subsection) == 0:
        return trade[filename]
    elif len(subsection) == 1:
        return trade[subsection[0]][filename]
    elif len(subsection) == 2:
        return trade[subsection[0]][subsection[1]][filename]

def get_chat_text(filename):
    return chat['text'][filename]

def get_chat_window(filename):
    return chat[filename]

def get_card(filename=None):
    if filename:
        return cards[filename]
    else:
        return cards

def get_card_text(phase, cardname):
    #if can't find png file for cardname in one phase, try other phase, most cards are the same except for longer names
    try:
        card = open(image_path + "product/cards/text/" + phase + "/" + cardname.lower() + ".png", "r")
    except IOError:
        try:
            if phase == "confirm":
                alt_path = "preconfirm"
            else:
                alt_path = "confirm"
            card = open(image_path + "product/cards/text/" + alt_path + "/" + cardname.lower() + ".png", "r")
        except IOError:
            raise Exception("PNG file for " + cardname.lower() + " text not found.")
        else:
            card.close()
            filepath = "product/cards/text/" + alt_path + "/" + cardname.lower() + ".png"
            return filepath
    else:
        card.close()
        filepath = "product/cards/text/" + phase + "/" + cardname.lower() + ".png"
        return filepath

def get_card_image(set, cardname):
    try:
        card = open(image_path + "product/cards/img/" + phase + "/" + cardname.lower() + ".png", "r")
    except IOError:
        raise Exception("PNG file for " + cardname + " image not found")
    else:
        card.close()
        filepath = "product/cards/img/" + phase + "/" + cardname.lower() + ".png"
        return filepath

def get_card_keys():
    return card_names_list
def get_pack_text(phase, packname):
    try:
        pack = open(image_path + "product/packs/text/" + phase + "/" + packname.lower() + ".png", "r")
    except IOError:
        print(image_path + "product/packs/text/" + phase + "/" + packname.lower() + ".png" + " not found")
        raise KeyError(packname + " not found")
    else:
        pack.close()
        filepath = "product/packs/text/" + phase + "/" + packname.lower() + ".png"
        return filepath

def get_all_pack_text_as_dict(phase):
    packs_dict = dict((abbr, get_packs_text(phase=phase, packname=abbr)) for abbr in __pack_names_list)
    return packs_dict

def get_pack_image(packname):
    try:
        pack = open(image_path + "/product/packs/img/" + packname.lower() + ".png", "r")
    except:
        raise KeyError(packname + " not found")
    else:
        pack.close()
        filepath = "product/packs/" + packname.lower() + ".png"
        return filepath
    
def get_all_pack_image_as_dict():
    packs_dict = dict((abbr, get_packs_image(abbr)) for abbr in __pack_names_list)
    return packs_dict

def get_login(filename):
    return login[filename]

def get_menu(filename):
    return menu[filename]