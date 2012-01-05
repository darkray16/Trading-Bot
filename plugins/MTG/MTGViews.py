import os, sys, copy
sys.path.append(os.path.abspath("view"))
sys.path.append(os.path.abspath("model/pricelist"))

import TradeView, View, ViewHelper, ImageHelper
import PackInventoryModel, CardInventoryModel
from global_helpers import ApplicationHelper

import time, datetime, win32con
import win32clipboard as clipboard

class MTGView(View.View):
    def filter_product(self, filtering, value):
        confirm_button = ViewHelper.find(ImageHelper.get_trade("confirm_button"))
        if filtering is "rarity":
            filter_button = {"x":confirm_button.x+110, "y":confirm_button.y-26}
        elif filtering is "version":
            filter_button = {"x":confirm_button.x+210, "y":confirm_button.y-26}
        elif filtering is "set":
            filter_button = {"x":confirm_button.x+140, "y":confirm_button.y-65}
        else:
            raise ViewError("No filter passed to filter_product")
        ViewHelper.click(image=filter_button)
        
        filter_option = ViewHelper.find(ImageHelper.get_filter(filtering, value))
        ViewHelper.click(image=filter_option)
    
    def wait_for_message(self, message, timeout):
        if ViewHelper.find_loop(image=ImageHelper.get_chat_text(string), timeout=timeout)
            return True
        else:
            return False
    
    def send_message(self, message):
        typing_area = ViewHelper.find(pattern=ImageHelper.get_chat_window("type_area"))
        if typing_area
            ViewHelper.click(target=typing_area)
        ViewHelper.type(message)
        wait(0.1)
        ViewHelper.key(Key.ENTER)
            
class TradeMTGView(MTGView):
    def wait_for_trade(self, timeout=0):
        started = datetime.datetime.now()
        found = None
        while not found:
            found = ViewHelper.find_onscreen(ImageHelper.get_trade("incoming_request"))
            if datetime.datetime.now() - started > datetime.timedelta(seconds=timeout) and timeout is not 0:
                break
        
        return found    
    def open_trade(self):
        """
        returns customer info:name, etc.
        """
        ViewHelper.click(image=ImageHelper.get_trade("yes_button"))
        time.sleep(1)
        #minimize the chat window to the right side of screen
        ViewHelper.click(image=ImageHelper.get_chat_window("minimize"))
        time.sleep(4)
        customer_name = self.get_customer_name()
        return customer_name
    
    def greet_customer(self, customer_name, credit):
        greeting_msg = r"Hello, "
        if customer_name:
            greeting_msg += customer_name
        greeting_msg += ". You have " + str(credit) + " credits stored."
        greeting_msg += "You can either take a card to buy, or take tickets and I "
        greeting_msg += "will search through your collection for cards."

        ViewHelper.click(image=ImageHelper.get_chat_window("type_area"))
        ViewHelper.type(greeting_msg)
    
    def get_mode(self):
        """
        observe areas of the client to figure out whether the customer
        will be buying products or selling products.
        """
        #if the customer just grabs tickets/product to indicate trade mode
        productarea = ViewHelper.get_region(image=ImageHelper.trade["giving_window"])
        #will wait until an item appears in product giving area
        ViewHelper.lock_observe(region=productarea, tolerance=0.04)
        ticket_found = ViewHelper.find_loop(region=productarea, pattern=ImageHelper.ticket_text, timeout=120)
        #if ticket was found, buy mode, otherwise sell mode
        if ticket_found:
            mode = "Buy"
        else:
            mode = "Sell"
        return mode
    
    def cancel_trade(self):
        ViewHelper.click(image=ImageHelper.get_trade("cancel_trade"))
        time.sleep(2)
        yes_button = ViewHelper.find(ImageHelper.get_trade("yes_button"))
        if yes_button:
            ViewHelper.click(image=yes_button)
        time.sleep(2)
        ok_button = ViewHelper.find(ImageHelper.get_ok_button())
        if ok_button:
            ViewHelper.click(image=ok_button)
    
    def get_customer_name(self):
        #uses the confirm button as a point of reference
        confirm_button = ViewHelper.find_onscreen(ImageHelper.get_trade("confirm_button"))
        coordinates={"x":confirm_button["x"]+600, "y":confirm_button["y"]+561}
        ViewHelper.click(coordinates)
        time.sleep(0.2)
        ViewHelper.type("c", modifier="CONTROL")
        
        clipboard.OpenClipboard()
        customer_name = clipboard.GetClipboardData(win32con.CF_TEXT)
        clipboard.CloseClipboard()
        
        if not customer_name:
            customer_name = None
            return "Uknown"
        #if customer is on friends list, name will be preceded by a smiley, remove it
        if "[sS]" in customer_name:
            customer_name = customer_name.split("[sS]")[0]
        print "customer name = " + customer_name
        return customer_name.strip()
class TradePreConfirmReceiveFrameView(object):
    next_row = 17
    def get_product_region(self):
        return ViewHelper.get_region(image=ImageHelper.trade["taking_window"])
        
    def get_product_name_region(self, region):
        product_name_region = copy.copy(region)
        product_name_region.x 
        product_name_region.y
        product_name_region.w = 198
        product_name_region.h = 17
        return product_name_region
        
    def get_product_quantity_region(self, region):
        product_quantity = copy.copy(region)
        product_quantity_region.x
        product_quantity_region.y
        product_quantity_region.w = 32
        product_quantity_region = 17
        
    def get_product_premium_region(self, region):
        pass
        
    def get_product_set_region(self, region):
        pass
        
    def get_product_rarity_region(self, region):
        pass
        
class TradePreConfirmGiveFrameView(object):
    next_row = 17
    def get_product_name_region(self):
        pass
        
    def get_product_quantity_region(self):
        pass
        
    def get_product_premium_region(self):
        pass
        
    def get_product_set_region(self):
        pass
        
    def get_product_rarity_region(self):
        pass

class TradePreConfirmMainFrameView(object):
    next_row = 17
    def get_search_field(self):
        button = self.get_search_button()
        field = {"x": button["x"]+40, "y": button["y"]}
        return field
    
    def get_search_button(self):
        """
        will search the screen for the search button and return
        an dict with "x", "y" coordinates of the center of the button
        """
        find_results = ViewHelper.find(ImageHelper.trade["search_button"])
        if isinstance(find_results, tuple):
            #get center of the image
            find_results[0] += 25
            find_results[1] += 7
            coordinates = {"x": find_results[0], "y": find_results[1]}
            return coordinates
        else:
            raise ViewError("Couldn't find search button")
            
    def get_product_region(self, phase, frame):
        """
        helper function to grab product line.
        used in get_product methods
        """
        if isinstance(frame, str):
            if phase == "preconfirm":
                if frame == "giving":
                    frame_region = ViewHelper.get_region(ImageHelper.giving_window)
                elif frame == "taking":
                    frame_region = ViewHelper.get_region(ImageHelper.taking_window)
                else:
                    raise ViewError("param failure for TradeFrameView.get_product_name_region method")
            elif phase == "confirm":
                if frame == "giving":
                    pass
                elif frame == "taking":
                    pass
                else:
                    raise ViewError("param failure for TradeFrameView.get_product_name_region method")
            else:
                raise ViewError("param failure for TradeFrameView.get_product_name_region method")
        else:
                raise ViewError("param failure for TradeFrameView.get_product_name_region method")
        return frame_region
        
    def get_product_name_region(self, phase, frame):
        """
        frame
            a string which is either "giving" or "taking
            to denote which frame to get the product name slot for
            
        return a region object of the top product slot
        in the specified frame
        """
        frame_region = self.get_product_region(phase=phase, frame=frame)
        if phase == "preconfirm":
            try:
                #convert frame region to a product slot region
                    frame_region.x += 35
                    frame_region.y += 43
                    frame_region.w = 159
                    frame_region.h = 18
            except AttributeError:
                raise ViewError("fram_region is of unexpected type")
        elif phase == "confirm":
            pass
        return frame_region
        
    def get_product_quantity_region(self, phase, frame):
        """
        frame
            a string which is either "giving" or "taking
            to denote which frame to get the product slot for
            
        return a region object of the top product quantity slot
        in the specified frame
        """
        frame_region = self.get_product_region(phase=phase, frame=frame)
        if phase == "preconfirm":
            try:
                #convert frame region to a product slot region
                    frame_region.x += 4
                    frame_region.y += 43
                    frame_region.w = 40
                    frame_region.h = 18
            except AttributeError:
                raise ViewError("fram_region is of unexpected type")
        elif phase == "confirm":
            pass
        return frame_region
        
    def get_product_set_region(self, phase, frame):
        """
        frame
            a string which is either "giving" or "taking
            to denote which frame to get the product slot for
            
        return a region object of the top product set slot
        in the specified frame
        """
        frame_region = self.get_product_region(phase=phase, frame=frame)
        if phase == "preconfirm":
            try:
                #convert frame region to a product slot region
                    frame_region.x += 4
                    frame_region.y += 43
                    frame_region.w = 63
                    frame_region.h = 18
            except AttributeError:
                raise ViewError("fram_region is of unexpected type")
        elif phase == "confirm":
            pass
        return frame_region
            
    def get_product_rarity_region(self, phase, frame):
        """
        frame
            a string which is either "giving" or "taking
            to denote which frame to get the product slot for
            
        return a region object of the top product rarity slot
        in the specified frame
        """
        frame_region = self.get_product_region(phase=phase, frame=frame)
        if phase == "preconfirm":
            try:
                #convert frame region to a product slot region
                    frame_region.x += 4
                    frame_region.y += 43
                    frame_region.w = 79
                    frame_region.h = 18
            except AttributeError:
                raise ViewError("fram_region is of unexpected type")
        elif phase == "confirm":
            pass
        return frame_region
            
    def get_product_premium_region(self, phase, frame):
        """
        frame
            a string which is either "giving" or "taking
            to denote which frame to get the product slot for
            
        return a region object of the top product premium symbol slot
        in the specified frame
        """
        frame_region = self.get_product_region(phase=phase, frame=frame)
        if phase == "preconfirm":
            try:
                #convert frame region to a product slot region
                    frame_region.x += 4
                    frame_region.y += 43
                    frame_region.w = 32
                    frame_region.h = 18
            except AttributeError:
                raise ViewError("fram_region is of unexpected type")
        elif phase == "confirm":
            pass
        return frame_region
            
    def next_row(self, regions):
        """
        regions
            dict of region objects of each section of the product slot
            
        shift down a product slot for each section until entire slot is shifted.
        number of pixels to shift must alternate between 17/18.
        """
        if TradeFrameView.next_row == 17:
            TradeFrameView.next_row = 18
        else:
            TradeFrameView.next_row = 17
        for section, object in regions.iteritems():
            object["y"] += TradeFrameView.next_row
            
class BuyMTGView(MTGView):
    trade_frame = TradePreConfirmMainFrameView()
    trade_functions = TradeMTGView()
    pack_inventory = PackInventoryModel.PackInventoryModel(ApplicationHelper.get_inventory_adapter())
    card_inventory = CardInventoryModel.CardInventoryModel(ApplicationHelper.get_inventory_adapter())
    
    def get_packs(self, transaction):
        """
        transaction
            Transaction object which holds information on all products taken/given
            so far. to be written and read from.
        """
        self.filter_product("version", "packs_tickets")
        product_region = {
                            "name": BuyMTGView.trade_frame.get_product_name_region(),
                            "quantity": BuyMTGView.trade_frame.get_product_quantity_region()
        }
        #first slot may be an event ticket which isn't a product
        if ViewHelper.find(pattern=ImageHelper.get_ticket_text(), region=product_region["name"]):
            product_region["name"]["y"] += 16
            product_region["quantity"]["y"] += 16

        searchfield = BuyMTGView.trade_frame.get_search_field()
        searchbutton = BuyMTGView.trade_frame.get_search_button()

        pack_names_keys = placeholder
        numbers_list = ImageHelper.get_all_numbers_as_dict(category="trade", phase="collection")

        tickets_to_give = 0
        found = True
        while found:
            if ViewHelper.find(pattern=ImageHelper.get_trade["empty"], region=product_region["name"]):
                break
            found = False
            if tickets_to_give >= ApplicationHelper.get("MAX_PRODUCTS_PER_TRADE"):
                break
            if transaction.take_count() >= ApplicationHelper.get("MAX_PRODUCTS_PER_TRADE"):
                break
            for packname in pack_names_keys:
                try:
                    pack_text_filepath = ImageHelper.get_pack_text(phase="preconfirm", packname=packname)
                except KeyError:
                    raise ViewError(str(packname) + " pack not found")
                    continue
                if ViewHelper.find(pattern=pack_text_filepath, region=product_region["name"]):
                    print(str(pack_text_filepath) + " found.")
                    found = True
                    current_product_click_location = {"x": product_region["name"]["x"] + product_region["name"]["w"] / 2,
                                                      "y":  product_region["name"]["y"] + product_region["name"]["h"] / 2}
                    #max amount to buy of the current product
                    max_buy = placeholder
                    
                    if max_buy <= 0:
                        self.trade_frame.next_row(product_region["name"])
                        #remove all products that are not found in frame
                        found_pack = packname
                        pack_names_keys = pack_names_keys[found_pack:]
                        break
                        
                    amount = 0
                    
                    for num in range(numbers_list):
                        if num == 0:
                            continue
                        if ViewHelper.find(pattern=numbers_list[num], region=product_region["quantity"]):
                            if num <= max_buy:
                                #customer has less than your max buy, so take all that they have
                                amount = num
                            else:
                                #if customer has more packs then you want, only take however much you want
                                amount = max_buy if max_buy > 0 else 0
                                #since there will be left over product in the current product slot, move the scan region
                                #down to move onto the next product
                                self.trade_frame.next_row(product_region)
                            print("Amount to take: " + str(amount))
                            break
                            
                    if amount > 0:
                        #if the amount of products would push the ticket total or products total over 75, then take just enough to get to 75 or closest
                        if transaction.take_count() + amount > ApplicationHelper.get("MAX_PRODUCTS_PER_TRADE"):
                            amount = ApplicationHelper.get("MAX_PRODUCTS_PER_TRADE") - transaction.take_count()
                        if tickets_to_give + (BuyMTGView.pack_inventory.get_buy_price(packname) * amount) > ApplicationHelper.get("MAX_PRODUCTS_PER_TRADE"):
                            amount = int((ApplicationHelper.get("MAX_PRODUCTS_PER_TRADE") - tickets_to_give) / self.pack_inventory.get_buy_price(packname))
                        
                        
                        self.take_product(product_loc=self.topmost_product_name_area.getCenter(), quantity_to_take=amount)
                        time.sleep(0.5)
                        pack_obj = Product.Product(name=cardname, buy=self.card_inventory.get_buy_price(cardname), sell=self.card_inventory.get_sell_price(cardname), quantity=amount)
                        self.transaction.take_product(pack_obj)
                        tickets_to_give += amount * self.pack_inventory.get_buy_price(packname)
                        break
                    else:
                        break
        if ViewHelper.find(pattern=ImageHelper.get_trade("canceled_trade")):
            return False
        else:
            return True
                        
    def get_bulk_cards(self):
        pass
        
    def get_specific_cards(self, transaction):
        #this will search for specific cards on the buy list to buy
        if ApplicationHelper.get("BUY_FOIL") == "yes":
            self.filter_product_version("all_versions")
        else:
            self.filter_product_version("regular")
        wait(1)
        
        searchfield = BuyMTGView.trade_frame.get_search_field()
        searchbutton = BuyMTGView.trade_frame.get_search_button()
        product_region = {
                            "name": BuyMTGView.trade_frame.get_product_name_region(),
                            "quantity": BuyMTGView.trade_frame.get_product_quantity_region()
        }
        numbers_list = ImageHelper.get_all_numbers_as_dict(category="trade", phase="collection")
        number_of_searches = 2 if ApplicationHelper.get("BUY_FOIL") == "yes" else 1
        tickets_to_give = 0
        for cardname, inv in self.card_inventory.inventory.items():
            #MTGO has a maximum of 75 products that can be given or taken in a single transaction
            if tickets_to_give  >= ApplicationHelper.get("MAX_PRODUCTS_PER_TRADE"):
                break
            
            if transaction.take_count() >= ApplicationHelper.get("MAX_PRODUCTS_PER_TRADE"):
                break
                
            #check how many copies of the card to buy, if 0 cards are desired, skip to the next card on list
            max_buy = self.card_inventory.get_max_stock(cardname) - self.card_inventory.get_stock(cardname)
            if max_buy <= 0:
                continue

            print(str(cardname))
            ViewHelper.click(image=searchfield)
            type(cardname + Key.ENTER)
            wait(2)
            if ViewHelper.find(image=ImageHelper.get_card_text(phase="preconfirm", card=cardname), region=self.get_product_name_region()):
                #sweeps have to be done twice in case there is a foil version AND a regular version of card
                for x in range(number_of_searches):
                    print(cardname + " has been found!")
                    
                    print("Max amount to buy: " + str(max_buy))
                    
                    amount = 0
                    for num in range(len(numbers_list)):
                        if num == 0:
                            continue
                        
                        #if current number being checked, is higher than max buy, then take all that they have
                        if num > max_buy:
                            amount = max_buy
                            break
                        if ViewHelper.find(region=product_region.quantity, pattern=number_list[num]):
                            if num < max_buy:
                                    #customer has less than your max buy, so take all that they have
                                    amount = num
                            elif max_buy > 0:
                                #if customer has more packs then you want, only take however much you want
                                amount = max_buy
                            else:
                                raise Exception("Max_Buy exception")
                            break
                    
                    if amount > 0:
                        if transaction.take_count() + amount > ApplicationHelper.get("MAX_PRODUCTS_PER_TRADE"):
                            amount = ApplicationHelper.get("MAX_PRODUCTS_PER_TRADE") - transaction.take_count()
                        if tickets_to_give + (BuyMTGView.card_inventory.get_buy_price(cardname) * amount) > ApplicationHelper.get("MAX_PRODUCTS_PER_TRADE"):
                            amount = int((ApplicationHelper.get("MAX_PRODUCTS_PER_TRADE") - tickets_to_give) / BuyMtGView.card_inventory.get_buy_price(cardname))
                        
                        self.take_product(product_loc=self.topmost_product_name_area.getCenter(), quantity_to_take=amount)
                        wait(0.5)
                        card_obj = Product.Product(name=cardname, buy=self.card_inventory.get_buy_price(cardname), sell=self.card_inventory.get_sell_price(cardname), quantity=amount)
                        self.transaction.take_product(card_obj)
                        tickets_to_give += amount * BuyMTGView.card_inventory.get_buy_price(cardname)
                        break
                    else:
                        break
                    
        if ViewHelper.find(pattern=ImageHelper.get_trade("canceled_trade")):
            return False
        else:
            return True
    
    def take_product(self, product_loc, quantity_to_take):
        #right click on the product to open context menu
        while quantity_to_take > 0:
            wait(0.2)
            if quantity_to_take < 10:
                ViewHelper.dblclick(product_loc)
                quantity_to_take -= 1
            else:
                ViewHelper.click(loc=product_loc, button="Right")
                if quantity_to_take >= 32:
                    ViewHelper.click(ImageHelper.get_amount(32))
                    quantity_to_take -= 32
                elif quantity_to_take >= 10:
                    ViewHelper.click(ImageHelper.get_amount(10))
                    quantity_to_take -= 10
        return True
    
    def go_to_confirmation(self):
        confirm_button = ImageHelper.get_trade("confirm_button")
        ViewHelper.click(pattern=confirm_button)
    
    def final_product_check(self, transaction):
        pass
    
class SellMTGView(MTGView):
    trade_frame = TradePreConfirmMainFrameView()
    trade_functions = TradeMTGView()
    pack_inventory = PackInventoryModel.PackInventoryModel(ApplicationHelper.get_inventory_adapter())
    card_inventory = CardInventoryModel.CardInventoryModel(ApplicationHelper.get_inventory_adapter())
    
    def wait_customer_finish(self):
        chat_window = ViewHelper.get_region(pattern=ImageHelper.get_chat_window)
        if self.wait_for_message(pattern=ImageHelper.get_chat_text, region=chat_window, duration=240):
            return True
        else:
            return False
    
    def initial_product_check(self, transaction):
        #searches a certain area for any image in a dictionary
        #combine all cards and packs for sale into a list
        product_names_list = self.pack_inventory.get_sorted_pack_list() + self.card_inventory.get_card_name_list()
        product_names_list.sort()
        numbers_list = ImageHelper.get_all_numbers_as_dict(category="trade", phase="preconfirm")

        #if area searched contains a full sized scroll bar, then scroll down
        #variable to hold last mouse position for the scrollbar movement code
        self.last_mouse_position = False
        
        number_of_tickets_to_take = 0 - credit
        #keep a record of product names found to prevent duplicates
        
        #mouse will hover over scroll bar and wheel down after 
        scroll_bar_x_loc = self.giving_window_region.getX() + self.giving_window_region.getW() - 1
        scroll_bar_y_loc = self.giving_window_region.getY() + (self.giving_window_region.getH()/2)
        scroll_bar_loc = {"x": scroll_bar_x_loc, "y": scroll_bar_y_loc}
        
        #scan_region will be used as the region to scan for the packs and number of packs
        #using the giving window as region, each product row is scanned for a product name and quantity
        #NOTE: A single area reserved for the text of a single product is a 192px(width) by 16/17px(height) area, with a 1px buffer in between each string
        #scan_region = Region(self.giving_window_region.getX(), self.giving_window_region.getY()+43, 198, 17)
        
        giving_product_name_area = self.trade_frame.get_trade_frame(app_region=self.app_region, phase="preconfirm", frame_name="giving_window", subsection="product_name_area")
        giving_product_quantity_area = self.trade_frame.get_trade_frame(app_region=self.app_region, phase="preconfirm", frame_name="giving_window", subsection="product_quantity_area")
        product_region = {
                            "name": BuyMTGView.trade_frame.get_product_name_region(),
                            "quantity": BuyMTGView.trade_frame.get_product_quantity_region()
        }
        #keep while loop as long as there is still a pack to be scanned
        found = True
        while found:
            found = False
            if ViewHelper.find(pattern=ImageHelper.trade["empty"], region = product_region["name"]):
                print("blank line found")
                break
            print("scanning " + str(product_region["name"].x) + ", "  + str(product_region["name"].y) + ", "  + str(product_region["name"].w) + ", "  + str(product_region["name"].h))
            for product_name in product_names_list:
                #if the product name to check is not a pack name, it must be a card name, if not then skip the product
                #because there is no png file for the product
                try:
                    product = ImageHelper.get_pack_text(phase="preconfirm", packname=product_name)
                except KeyError:
                    try:
                        product = ImageHelper.get_card_text(phase="preconfirm", cardname=product_name)
                    except KeyError:
                        continue
                    else:
                        product_type = "card"
                else:
                    product_type = "pack"
                print("searching for " + str(product))
                if ViewHelper.find(pattern=product, region=product_region["name"]):
                    print("found " + str(product))
                    found = True

                    for key in range(len(numbers_list)):
                        if key == 0:
                            continue
                        
                        searchPattern = Pattern(numbers_list[key]).exact()
                        if ViewHelper.find(pattern=numbers_list[key], region=product_region["quantity"]):
                            amount = key
                            #for booster packs, there is a specific order in which they appear in the list,
                            #when a pack is found, remove all packs before and including that pack in the keys
                            #list as they will not appear any further below
                            pack_index = product_names_list.index(product_name)
                            product_names_list = product_names_list[pack_index:]
                            break
                    
                    if product_type == "pack":
                        product_obj = Product.Product(name=productname, buy=self.pack_inventory.get_buy_price(productname), sell=self.pack_inventory.get_sell_price(productname), quantity=amount)
                        print(product_name + ": " + str(self.pack_inventory.get_sell_price(product_name)))
                    elif product_type == "card":
                        product_obj = Product.Product(name=productname, buy=self.card_inventory.get_buy_price(productname), sell=self.card_inventory.get_sell_price(productname), quantity=amount)
                    else:
                        raise ErrorHandler("Product type has not been set, but product detected")
                    transaction.add_product(product_obj)
                    if found:
                        break
                    else:
                        raise ErrorHandler("Unrecognized card found")
            wheel(scroll_bar_loc, WHEEL_DOWN, 2)
            
            #if after the mousewheel down action, the products have not moved, then move down a slot.
            #if the products have shifted up, that means the scroll bar moved and product scan slot should remain the same,
            #because there is a new product in the current product slot
            if giving_product_name_area.exists(self._images.get_pack_text(phase="preconfirm", packname=product_names_list[0])):
                #if first scan area was already set, then relative distance from last region
                #scan area will be slightly larger than estimated height of product slot to compensate for any variances, to compensate for larger region, the Y coordinate -1
                self.next_row(giving_product_name_area, giving_product_quantity_area)
            
        #in case the customer has canceled the trade
        if ViewHelper.find(ImageHelper.get_trade("canceled_trade")):
            return False
        else:
            return True
    
    def final_product_check(self, transaction):
        #does a scan depending on which type is requested.  Each pass should scan the window differently
        #to confirm that the correct
        
        #verify confirm window by checking for confirm cancel buttons, then set regions relative to those buttons
        confirm_button = ViewHelper.find_loop(pattern=ImageHelper.get_trade("confirm_button", "confirm"), duration=60)
        
        if confirm_button:
            products_names_list = [ productname for productname in self.products ]
            #product_names_list = self.card_inventory.get_card_name_list() + self.pack_inventory.get_sorted_pack_list()
            product_names_list.sort()
            
            numbers = ImageHelper.get_all_numbers_as_dict(category="trade", phase="preconfirm")
            #confirm products receiving
            #set the regions of a single product and and the amount slow
            #number region is 20px down and 260px to the left, 13px height and 30px wide, 4px buffer vertically
            #receiving_number_region = Region(confirm_button.getX()-289, confirm_button.getY()+42, 34, 14)
            #height for each product is 13px, and 4px buffer vertically between each product slot
            #receiving_name_region = Region(confirm_button.getX()-257, confirm_button.getY()+42, 163, 14)
            receiving_number_region = self.frame_grab.get_trade_frame(app_region=self.app_region, phase="confirm", frame_name="taking_window", subsection="product_quantity_area")
            receiving_name_region = self.frame_grab.get_trade_frame(app_region=self.app_region, phase="confirm", frame_name="taking_window", subsection="product_name_area")
            
            giving_number_region = self.frame_grab.get_trade_frame(app_region=self.app_region, phase="confirm", frame_name="giving_window", subsection="product_quantity_area")
            giving_name_region = self.frame_grab.get_trade_frame(app_region=self.app_region, phase="confirm", frame_name="giving_window", subsection="product_name_area")
            
            #confirm products giving
            #giving_number_region = Region(confirm_button.getX()-291, confirm_button.getY()+391, 34, 14)
            #giving_name_region = Region(confirm_button.getX()-260, confirm_button.getY()+391, 163, 14)
            #this is a variable that will hold the number of pixels to move down after scanning each area
            #between some rows, theres a 4 pixel space buffer, between others there is 5, this variable will hold
            #alternating numbers 4 or 5
            
            found = True
            while found:
                if giving_name_region.exists(self._images.trade["empty"]):
                    break
                print("scanning region: " + str(giving_name_region.x) + ", " + str(giving_name_region.y) + ", " + str(giving_name_region.w) + ", " + str(giving_name_region.h))
                hover(Location(giving_number_region.getX(), giving_number_region.getY()))
                found=False
                for product_name in product_names_list:
                    
                    try:
                        product_image_filepath = self._images.get_pack_text(phase="confirm", packname=product_name)
                    except KeyError:
                        try:
                            product_image_filepath = self._images.get_card_text(phase="confirm", cardname=product_name)
                        except KeyError:
                            continue
                        else:
                            product_type = "card"
                    else:
                        product_type = "pack"
                    print("searching for " + str(product_image_filepath))
                    if giving_name_region.exists(Pattern(product_image_filepath).exact()):
                        print("found " + str(product_name))
                        #if still at 0 after for loop, error raised
                        amount = 0
                        for number in range(len(numbers)):
                            if number == 0:
                                continue
                            if giving_number_region.exists(Pattern(numbers[number]).similar(0.8)):
                                amount = number
                                print("found " + str(amount) + " copies")
                                #packs are listed in Magic in the same sequence they are listed in the list of pack keys,
                                #if a pack is found, all packs including it and before, are removed from the list of packs
                                #to search
                                product_index = product_names_list.index(product_name) + 1
                                product_names_list = product_names_list[product_index:]
                                break
                        if product_type == "pack":
                            product_obj = Product.Product(name=product_name, buy = self.pack_inventory.get_buy_price(product_name), sell = self.pack_inventory.get_sell_price(product_name), quantity=amount)
                            giving_products_found["packs"].append(product_obj)
                        elif product_type == "card":
                            product_obj = Product.Product(name=product_name, buy = self.card_inventory.get_buy_price(product_name), sell = self.card_inventory.get_sell_price(product_name), quantity=amount)
                            giving_products_found["cards"].append(product_obj)
                        else:
                            raise Errorhandler("Product type has not been set, but product detected")
                                            
                        if amount == 0:
                            raise ErrorHandler("Could not find a number for product: " + str(product_abbr))
                        found=True
                        if found:
                            break
                        else:
                            raise ErrorHandler("Unrecognized card found")
                self.next_row(giving_number_region, giving_name_region)
            
            #get image of number expected to scan for it first, to save time, else search through all other numbers
            expected_number = 0
            for product_type, products in giving_products_found.items():
                for product in products:
                    expected_number += product["quantity"] * product["sell"]
                    print(expected_number)
            expected_number -= credit
            print("expected tickets: " + str(expected_number))

            if not expected_number == tickets_to_take:
                return False

            #in case the customer has canceled trade
            if self.app_region.exists(self._images.get_trade("canceled_trade")):
                return False

            hover(Location(receiving_number_region.getX(), receiving_number_region.getY()))
            if expected_number > 0 and expected_number is not False:
                ticket_text_image = Pattern(self._images.get_ticket_text()).similar(1)
                if receiving_name_region.exists(ticket_text_image):
                    print("ticket image found")
                    expected_number_image = Pattern(self._images.get_number(number=int(math.ceil(expected_number)), category="trade", phase="confirm")).similar(0.9)
                    print(str(expected_number_image))
                    if receiving_number_region.exists(expected_number_image):
                        print("ticket amount image found")
                        return giving_products_found
                    else:
                        return False
            elif expected_number <= 0:
            
                return giving_products_found
            else:
                return False
    
    def go_to_confirmation(self):
        confirm_button = ImageHelper.get_trade("confirm_button")
        ViewHelper.click(pattern=confirm_button)
