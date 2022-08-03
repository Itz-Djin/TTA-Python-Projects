import datetime
from xmlrpc.client import DateTime
import pytz

dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))

print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'August 02, 2022'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)
