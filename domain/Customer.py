from DomainObject import *

class Customer(DomainObject):
	
    def __init__(self, name):
        super(self.__class__, self).__init__(name)
    
    def get_name(self):
        """
        returns id, which in this context is the customer's name
        """
        return self.id
        
    def set_credits(self, credits):
        if isinstance(credits, float):
            self.credits = credits
        else:
            raise DomainError("Non-float passed as credit to Customer object")
    
    def get_credits(self):
        try:
            self.credits
        except AttributeError:
            self.credits = 0
        return self.credits
            
    def set_transactions(transactions):
        if isinstance(transactions, TransactionCollection):
            self.transactions = transactions
        else:
            raise DomainError("Non-TransactionCollection passed to setTransactions")
    
    def get_transactions(self):
        return self.transactions
        
    def add_transaction(self, transaction):
        if isinstance(transaction, Transaction):
            self.transaction.add( transaction )
        else:
            raise DomainError("Non-Transaction object passed to addTransaction")
    
    def set_comments(self, comments):
        if isinstance(comments, CommentCollection):
            self.comments = comments
        else:
            raise DomainError("Non-CommentsCollection passed to setComments")
    
    def get_comments(self):
        return self.comments
        
    def add_comment(self, comment):
        if isinstance(comment, Comment):
            self.comments.add( comment )
        else:
            raise DomainError("Non-Comment object passed to addComment")
    
    