from b64 import *
from hashlib import md5
import re
import uuid

codeMac = (':'.join(re.findall('..', '%012x' % uuid.getnode())))
password = 'batata'

md5edKey = (f'{md5(password.encode()).hexdigest()}||{codeMac}')
encodedKey = b64encode(md5edKey)

print(encodedKey)
print(b64decode(encodedKey).split('||')[1]) #get mac adress again

with open("encriptedKey.py", "w") as f:
  f.write(f'secretKey = "{encodedKey}"')