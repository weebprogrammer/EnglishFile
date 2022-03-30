import os

for i in range(10,22):
    if os.path.exists(f'content/EF4e_Elementary_SB_10.{i}.mp3') is True:
        os.rename(f'content/EF4e_Elementary_SB_10.{i}.mp3', f'content/10.{i}.mp3')
