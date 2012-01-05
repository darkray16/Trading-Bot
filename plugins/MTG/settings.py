#this object will hold all global settings for the application
#ERRORHANDLERAPP = How the app will output errors, possible values: Notepad

#DBTYPE = what kind of database will you use for product information, 
#will be used with inventory adapter.  valid strings: "txt", "mysql"

#RECORD_OUTPUT_FORMAT = how you want your customer records to be recorded, valid strings: "txt", "mysql", "excel"

#USERNAME = Your Magic Online username

#PASSWORD = Your Magic Online password

#NETWORK = Whether you have other bots that you wish this bot to interact with for chores like farming and juggling products

#DEFAULTMODE = the mode that the bot will automatically go into when a trade is opened.  Valid strings: "buy", "sell"

#CARD_BUYING = Whether the bot will search for specific cards in searchfield or just skim through the collection
#by category.  Search is better if your card buy list is small(less than a dozen or so), all is better if there
#are many cards listed in the card_buy pricelist, meaning there are many cards you would buy.  Valid strings: "bulk", "search"

#BUY_FOIL = The bot will search for and buy foil cards, currently not working.

#MAX_PRODUCTS_PER_TRADE = maximum number of products that the Magic Online app will allow you to trade, currently it is 75

#BULK_BUY_OPTIONS = the settings(max amt to buy, and price) for the bot to buy cards in bulk according to rarity

#these are the settings for bot to use when buying cards in bulk, i.e. when not searching for specific cards,
#but rather when it's buying all cards the customer has available
#Any setting set to yes means the bot will buy cards from that category
#hint: use the find/replace feature in your editor to replace the yes/no text to save time

settings = {
            "DBTYPE":"txt",
            "mysql": { "host": "localhost",
                      "port": "3306",
                      "db": "mtg",
                      "username": "root",
                      "password": None
                      },
            "ERRORHANDLERAPP":"Notepad", 
            "RECORD_OUTPUT_FORMAT":"txt",
            "LOGIN_WAIT":45, 
            "USERNAME": "yourmagiconlineusername", 
            "PASSWORD":"yourpasswordhere", 
            "DEFAULTMODE":"buy",
            "CARD_BUYING":"search",
            "BUY_FOIL": "no",
            "MAX_PRODUCTS_PER_TRADE": 75,
            "bulk_buymax_amount": 8,
            "bulk_buy_prices": {"mythic": 1,
                                "rare": 0.5,
                                "uncommon": 0.02,
                                "common": 0.001},
            "bulk_buy_rarity":{"mythic": "yes",
                               "rare": "no",
                               "uncommon": "no",
                               "common": "no",
                               "any": "no"},
            "bulk_buy_set": [{"Standard": "no"},
                             {"Extended": "no"},
                             {"Classic": "no"},
                             {"Legacy": "no"},
                             {"Scars of Mirrodin": "yes"},
                             {"Mirrodin Besieged": "no"},
                             {"Zendikar": "no"},
                             {"Worldwake": "yes"},
                             {"Rise of the Eldrazi": "yes"},
                             {"Shards of Alara": "no"},
                             {"Conflux": "no"},
                             {"Alara Reborn": "no"},
                             {"Lorwyn": "no"},
                             {"Morningtide": "no"},
                             {"Shadowmoor": "no"},
                             {"Eventide": "no"},
                             {"Time Spiral": "no"},
                             {"Timeshifted": "no"},
                             {"Planar Chaos": "no"},
                             {"Future Sight": "no"},
                             {"Ice Age": "no"},
                             {"Alliance": "no"},
                             {"Coldsnap": "no"},
                             {"Ravnica": "no"},
                             {"Guildpact": "no"},
                             {"Dissension": "no"},
                             {"Champions of Kamigawa": "no"},
                             {"Betrayers of Kamigawa": "no"},
                             {"Saviors of Kamigawa": "no"},
                             {"Mirrodin": "no"},
                             {"Darksteel": "no"},
                             {"Fifth Dawn": "no"},
                             {"Onslaught": "no"},
                             {"Legion": "no"},
                             {"Scourge": "no"},
                             {"Odyssey": "no"},
                             {"Torment": "no"},
                             {"Judgment": "no"},
                             {"Invasion": "no"},
                             {"Planeshift": "no"},
                             {"Apocalypse": "no"},
                             {"Urza's Saga": "no"},
                             {"Urza's Legacy": "no"},
                             {"Urza's Destiny": "no"},
                             {"Tempest": "no"},
                             {"Stronghold": "no"},
                             {"Exodus": "no"},
                             {"Mirage": "no"},
                             {"Visions": "no"},
                             {"Weatherlight": "no"},
                             {"Seventh Edition": "no"},
                             {"Eighth Edition": "no"},
                             {"Ninth Edition": "no"},
                             {"Tenth Edition": "no"},
                             {"Magic 2010": "no"},
                             {"Magic 2011": "no"},
                             {"Magic 2012": "no"},
                             {"Masters Edition": "no"},
                             {"Masters Edition II": "no"},
                             {"Masters Edition III": "no"},
                             {"Masters Edition IV":"no"}]}