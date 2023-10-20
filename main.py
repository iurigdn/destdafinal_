# from login import login
import destda_new
from helpers import waiters

# login()
path = waiters.getPath(title = 'auto-destda')
print(path)
destda_new.run(path)