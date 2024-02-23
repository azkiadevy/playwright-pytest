import json
import os

class Config:

    config_file = os.path.abspath('../config.json')
    with open(config_file, 'r') as configuration:
        config = json.load(configuration)    

    def web_url(self):
        return self.config['WEB_URL']
    
    def account_username(self):
        return self.config['USERNAME']
    
    def account_password(self):
        return self.config['PASSWORD']
