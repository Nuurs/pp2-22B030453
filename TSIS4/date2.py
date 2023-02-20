from datetime import datetime, timedelta
today = datetime.now()
print(today)
yesterday = datetime.now() - timedelta(1)
print( yesterday)
tomorrow = datetime.now() + timedelta(1)
print( tomorrow)