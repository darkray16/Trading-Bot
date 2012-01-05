
def get_mapper(adapter, table, dsn):
    adapters = {
        "mysql": get_mysql_mapper,
        "txt": get_txt_mapper,
        "http": get_http_mapper
    }
    table = strtolower(table)
    mapper = adapters[adapter](table)(dsn)
    
def get_mysql_mapper(table):
    mysql_mappers = {
        "transaction": TransactionMySQLMapper,
        "customer": CustomerMySQLMapper,
        "inventory": InventoryMySQLMapper
    }
    mapper_name = str(table) + "MySQLMapper"
    mapper = mysql_mappers[mapper_name](dsn)
    
def get_txt_mapper(file):
    txt_mappers = {
        "transaction": TransactionTxtMapper,
        "customer": CustomerTxtMapper,
        "inventory": InventoryTxtMapper
    }
    mapper_name = table + "TxtMapper"
    mapper = txt_mappers[mapper_name](dsn)