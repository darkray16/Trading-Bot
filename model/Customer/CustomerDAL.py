"""handles reading and writing to customer records like saved credits
using this as a data abstraction layer will allow me to switch out the CustomerModel
which handles all the db adapter functions, useful if I later switch 
to a different db, i.e. Excel, MySQL, etc"""

from sikuli.Sikuli import *
path_to_bot = getBundlePath().rsplit("\\", 1)[0] + "\\"

from sys import *
sys.path.append(path_to_bot + "model/customer" )
import TextAdapter
import MySQLAdapter
import ExcelAdapter

from datetime import datetime

class CustomerDAL(object):

    def __init__(self, adapter, customer_name):
        adapters = {"txt":TextAdapter.TextAdapter(customer_name=customer_name),
                    "excel":ExcelAdapter.ExcelAdapter(customer_name=customer_name),
                    "mysql":MySQLAdapter.MySQLAdapter(customer_name=customer_name)}
        self.db_adapter = adapters.get(adapter, lambda: None)
        self.record = {}
    
    def write_transaction(self, type, productname, quantity):
        self.record["type"] = type
        self.record[productname] = quantity
        
    def read_credits(self):
        #will return the last value of credit
        credit_request = self.db_adapter.read_row(row_name="credit")
        try:
            credits = float(credit_request)
        except ValueError:
            self.write_credits(0)
            credits = 0
        finally:
            return credits

    def write_credits(self, amount):
        self.record["credit"] = str(amount)

    def write_transaction_date(self, time):
        self.record["date"] = str(time)

    def write_comments(self, comment):
        self.record["comment"] = str(datetime.now()) + "    " + str(comment)

    def save(self):
        #call the write_row method for each of the transaction rows
        if self.db_adapter.write_all_rows(self.record):
            return True
        else:
            return False