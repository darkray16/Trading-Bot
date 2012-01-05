Collection = {
    "Customer": CustomerCollection(),
    "Transaction": TransactionCollection()
}

def get_collection(type):
    collection_instance = CollectionFactory.Collection[type]
    return collection_instance.copy()