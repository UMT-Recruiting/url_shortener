from constants import SECRET_KEY

class Shorten:
    def __init__(self, url, custom_path=None):
        self.url = url
        self.custom_path = custom_path
        
    def shorten(self):
        #  Call function to check that url does not already have a shortened url
        #  If it exists throw error
        if self.already_shortened(self.url):
            return
        
        if self.custom_path:
            # Check that custom path provided does not already exist
            # If it exists return error
            # Else, add url with custom path to the database
            pass
        
        # Call function to hash the url
        # Add the hash to the database
        # Returned shortened URL
        
    def is_already_shortened(url):
        # Check database for shortened url
        # If it exists return True
        # If it does not exist return False
        pass
    
    def verify_url():
        # verify url structure is valid
        # verify url can be reached
        pass
    
    def setup_redirect():
        # Call to Redirect class to set up redirect logic
        pass