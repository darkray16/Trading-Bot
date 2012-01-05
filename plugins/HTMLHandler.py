import HTMLParser

class HTMLHandler(HTMLParser.HTMLParser):
    def handle_data(self, data):
        pass
    def handle_charref(self, name):
        pass
    def handle_starttag(self, tag, attrs):
        pass
    def handle_endtag(self, tag):
        pass
