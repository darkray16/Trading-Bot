from java.lang import *
from java.sql import *

#these needs to be explicitly imported
from java.lang import Class
from java.sql import DriverManager

def connect(dburl="jdbc:mysql://localhost:3306/mtgo", dbuser="root", dbpass=None):
    try:
        try:
            Class.forName("com.mysql.jdbc.Driver").newInstance()
        except NameError:
            raise ErrorHandler("Internal MySQL error")
        conn = DriverManager.getConnection(dburl, dbuser, dbpass)
    except SQLException, error:
        raise ErrorHandler("MySQL error: %s" % str(error))
    else:
        return conn
        
def close(conn):
    conn.close()
    
def query(query, conn):
    """
    Returns None if you haven't establed a connection yet.
    Use for select queries only, no inserts, updates, etc.
    """
    data = {}
    stmnt = conn.createStatement()
    sql = query
    results = stmnt.executeQuery(sql)

    product_dict = {}
    while results.next():
            name = results.getString("name").strip()
            set = results.getString("block").strip()
            foil = results.getString("foil").strip()
            sell = float(results.getString("sell_price").strip())
            buy = float(results.getString("buy_price").strip())
            stock = int(results.getString("in_stock").strip())
            min = int(results.getString("minimum_stock").strip())
            max = int(results.getString("maximum_stock").strip())
            
            product_dict[name] = {"set": set, "foil": foil, "sell": sell, "buy": buy, "stock": stock, "min": min, "max": max}
    results.close()
    stmnt.close()
    
    return product_dict
    
def get_product_info(product):
    """
    @product: string
    will call query with select statement
    @return: dict
    """
    db_url = "jdbc:mysql://" + ApplicationHelper.get("mysql")["host"] + ":" + ApplicationHelper.get("mysql")["port"] + "/" + ApplicationHelper.get("mysql")["db"]
    conn = connect(db_url, ApplicationHelper.get("mysql")["username"], ApplicationHelper.get("mysql")["password"])
    sql_stmnt = "SELECT * FROM " + str(product) + ";"
    product_request = query(sql_stmnt, conn)
    if product_request == None:
        raise ErrorHandler("MySQL DB query returned None or there was an error")
    close(conn)
    return product_request
    
def set_product_info(product, product_info):
    """
    @product: string, @update_info: dict
    will call select query with to see if product exists,
    if yes, it will call query with update statement,
    otherwise it will use insert statement.
    @return: boolean
    """
    conn = connect()
    sql_stmnt = ""
    
    results = query(sql_stmnt, conn)
    
    close(conn)