# creating a separate config file so that instances of app can be easily created for testing and other purposes as well
import os

# putting into class to be able to do other things like inheritance 
class Config:
	# we can also provide default values for environment variables in case if they are not set
	# but here we assume they are set properly
	SECRET_KEY = os.environ.get('SECRET_KEY')
	# specifying the uri (Unique resource identifier) for our database i.e where the database is located
	# SQLite database will simply be a file in our file system
	# can specify the relative path with three forward slashes
	# will create site.db file
	# 'sqlite:///site.db'
	SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
	
	# setting up a mail server
	MAIL_SERVER = 'smtp.gmail.com'
	# setting up a  mail port
	MAIL_PORT = 465
	# tls- transport layer security designed to provide communication security over a comp network
	MAIL_USE_TLS = False
	MAIL_USE_SSL = True
	# environ is basically a dictionary so we can access the value by using get keyword
	# EMAIL_USER and EMAIL_PASS are defined in bash file
	MAIL_USERNAME = os.environ.get('EMAIL_USER')

	MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

	MAIL_DEFAULT_SENDER = os.environ.get('EMAIL_USER')

