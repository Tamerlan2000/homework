class JSONParser:
    def __init__(self, data):
        self.data = data

    def parse(self):
        message = self.data.get('message', 'no message')
        return message
