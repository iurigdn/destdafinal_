from login import login
import destda
from helpers import waiters

login()
path = waiters.getPath(title = 'auto-destda')
print(path)
destda.run(path)