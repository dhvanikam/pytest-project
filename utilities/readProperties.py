import configparser

config=configparser.RawConfigParser()
config.read(".//Configuration/config.ini")

class ReadConfig():
    @staticmethod
    def getBaseUrl():
        BaseUrl = config.get('URL', 'baseurl')
        return BaseUrl
    
    @staticmethod
    def getLoginUrl():
        LoginUrl = config.get('URL', 'loginurl')
        return LoginUrl

    @staticmethod
    def getAddElementUrl():
        AddElementUrl = config.get('URL', 'addelementurl')
        return AddElementUrl

    @staticmethod
    def getusername():
        username = config.get('Login Page objects', 'username_textbox_id')
        return username

    @staticmethod
    def getpassword():
        password = config.get('Login Page objects', 'password_textbox_id')
        return password