import os, sys, time

sys.path.append(os.path.abspath("../../command"))
sys.path.append(os.path.abspath("../../domain"))

from command import *
from MTGViews import *
from domain import Customer, Transaction
from global_helpers import ApplicationHelper


class LoginMTGCommand(LoginCommand):
    pass
    
class BuyMTGCommand(BuyCommand):
    trade_functions = TradeMTGView()
    view = BuyMTGView()
    
    def complete_purchase(self, registry):
        transaction_id = registry.get("customer").get_name() + str(time.time())
        transaction = Transaction(transaction_id)
        self.get_products(transaction)
        self.view.go_to_confirmation()
        verfication = self.verify_confirm(transaction)
        if verification:
            registry.add("products", self.products)
        else:
            trade_functions.cancel_trade()
    def get_products(self, transaction):
        if not self.view.get_packs(transaction):
            #trade canceled
            pass
        buy_mode = ApplicationHelper.get_setting("buy_cards")
        if buy_mode == "bulk":
            self.view.get_bulk_cards(transaction)
        elif buy_mode == "specific":
            self.view.get_specific_cards(transaction)
        return transaction
        
    def verify_confirm(self, products):
        """
        products
            products found at confirmation screen will be matched
            with provided products to verify everything is as
            expected
        a verification scan will be done at the final
        confirmation window before accepting the trade
        """
        found_products = self.view.check_products()
        if found_products == products:
            #passed
            
            return True
        else:
            #products don't match
            self.view.cancel_trade()
            return False

class SellMTGCommand(SellCommand):
    trade_functions = TradeMTGView()
    view = SellMTGView()
        
    def complete_sale(self, registry):
        if not view.wait_customer_finish():
            trade_functions.cancel_trade()
            return False
        self.trade_functions.send_message("Calculating tickets to take.  Please wait..")
        transaction_id = registry.get("customer").get_name() + str(time.time())
        transaction = Transaction(transaction_id)
        self.check_products_taken(transaction)
        self.view.initial_product_check(transaction)
        self.view.go_to_confirmation()
        self.view.final_product_check(transaction)
        
class StartTradeMTGCommand(StartTradeCommand):
    view = TradeMTGView()
    
    def trade_start(self, session_registry):
        self.view.wait_for_trade()
        customer_name = self.view.open_trade()
        customer = Customer(customer_name)
        session_registry.set("customer", customer)
        self.view.greet_customer(customer.get_name(), customer.get_credits())
        mode = self.view.get_mode()
        
        session_registry.set( "trade_mode", mode )
        return
        
    def wait_for_trade(self):
        ViewHelper.wait(ImageHelper.get_trade("incoming_request"))
    
    def retrieve_records(self, customer_name):
        customer = Customer(ApplicationHelper.get_customer_adapter(), customer_name)
        credits = customer.get_credits()
    
class TradeCleanupMTGCommand(TradeCleanupCommand):
    
    def cleanup(self, session_registry):
        pass
