from deta import Deta

KEY = 'project key' #Deta Key
BASE = 'realtime' # detaBase name

deta = Deta(KEY) # configure your Deta project
db = deta.Base(BASE)  # access your DB

BaseKey = 'generated id' # paste the detabase key generated by db_config.py

