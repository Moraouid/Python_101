import time
import datetime

seconds = time.time()

x = "{:.2e}".format(seconds)
z = datetime.datetime.now()

print(f"Seconds since January 1, 1970: {seconds:,.4f} or {x} in scientific notation")	
print(z.strftime("%b %d %Y"))
