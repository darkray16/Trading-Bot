import urllib, urllib2


def setup_auth(auth_info=""):
    """
    This function is to be run once and will at that time set the 
    auth info for all subsequent urlopen function calls
    Arguments:
        auth_info
            a list containing containing a dict for each set of auth info to set.
            dict contains the following auth info:
                
                top_level_url : a string containing the top level url to use, 
                                defaults to admin of hotlist
                username : username to log in
                password : password for provided username
    """
    
    if auth_info == "":
        auth_info = [{top_level_url: "http://www.mtgotraders.com/hotlist/admin", 
                      username: "root",
                      password: ""
                      }]

    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, top_level_url, username, password)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)

    opener = urllib2.build_opener(handler)
    opener.open("http://www.mtgotraders.com/hotlist/admin")

    urllib2.install_opener(opener)

def request(url, raw_data=None, headers=None):
    """
    Arguments:
        
        url
            a string that contains the url of mtgotraders admin
            page.
            
        raw_data
            a dict object containing all POST data to send
        
        headers
            a dict object containing all headers to send
    """
    if raw_data is not None:
        encoded_data = urllib.encode(raw_data)
        
    req = urllib2.Request(url, data, headers)
    
    try:
        response = urllib2.urlopen(req)
    except urllib2.URLError, error:
        raise ErrorHandler( "Error opening url to mtgo traders:\n" + str(error) )
        
    else:
        html = response.read()
        return html

def process_response(html=None):
    """
    Arguments:
        html
            string containing response returned from request function
    """
    if html is None:
        return False

def create_headers():
    headers = {"user-agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}
    
    return headers
        
def create_get_request(**kwargs):
    get_vars = {"update_status": "?status=" + status,
                "update_price": "?price=" + str(price) + 
                "&sku=" + str(sku) + "&quantity=" + str(quantity)}
    return get_vars[request_type]

def update(id, action, **kwargs):
    """
    Arguments:
        id
            product id to be used with the mysql db
        
        action
            type of action update to do.  you can pass either
            "status" or "price".  if you pass "status", then you 
            must supply status_info kwarg.  if you pass "price", then
            you must supply price, sku and quantity kwargs.
            
        status_info
            new status to set the product to.
            valid strings you can use are:
            "pending", "completed", "declined".
        
        price
            price to set product to, must be a float
        sku
            item sku identifier, must be a string
        quantity
            amount of product to set to, must be an int
    """
    
    if action is not "status" or action is not "price":
        raise ErrorHandler("""update called 
                            but action var doesn't contain valid data.
                            action contents:""" + str(action))
    
    if action == "status" and status_info is None or not instanceof(status_info, str):
        raise ErrorHandler("status update called but incorrect status info passed")
    
    if action == "price" 
        if price is None or not instanceof(price, float) or sku is None or not instanceof(sku, str) or quantity is None or not intanceof(quantity, int):
            raise ErrorHandler("price update called but incorrect price info passed")

    get_string = create_query(request_type=action, **kwargs)

    response_html = request()
