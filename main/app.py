from utils import *
from pages.login import login
application.register_blueprint(login)
if __name__=='__main__':
    application.run('192.168.68.28',80,debug=True)