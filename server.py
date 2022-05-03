import yadisk
from config import DISKTOKEN 
import os 

disk = yadisk.YaDisk(token=DISKTOKEN)

def namecheck(message: str):
    for audio in list(disk.listdir('/englishfile')):
        if audio['name'] == message:
            return True

os.remove('cache/10.06.mp3')
