import uuid
import re
from geradorDeChave.encriptedKey import secretKey
from helpers import *
from geradorDeChave.b64 import *
import PySimpleGUI as sg
import time

[payerPasswordmd5, payerMacAdress] = b64decode(secretKey).split('||')

userMacAdress = (':'.join(re.findall('..', '%012x' % uuid.getnode())))


if payerMacAdress != userMacAdress:
    waiters.wrong('este não é o computador correto')
else:
    while True:
        waiters.password(title='login',correctHash=payerPasswordmd5)
        waiters.ok(title='acertou')
        break
