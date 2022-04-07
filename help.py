import os

for i in range(1,10):
    if os.path.exists(f'content/EF4e_Elementary_SB_10.0{i}.mp3') is True:
        os.rename(f'content/EF4e_Elementary_SB_10.0{i}.mp3', f'content/10.0{i}.mp3')
