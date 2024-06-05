import os
import subprocess

def merge_wav_files(folder_path):
    # 在文件夹中找到所有的.wav文件
    wav_files = [f for f in os.listdir(folder_path) if f.endswith('.wav')]
    wav_files = [os.path.join(folder_path, f) for f in wav_files]

    # 创建一个新的文本文件，并将.wav文件的路径写入其中
    with open('files.txt', 'w', encoding='utf-8') as f:
        for wav_file in wav_files:
            f.write(f"file '{wav_file}'\n")

    # 调用ffmpeg合并.wav文件
    subprocess.call('ffmpeg -f concat -safe 0 -i files.txt -c copy output.wav', shell=True)

folder_path = r'E:\gal\解包\魔女的夜宴\voice\５－和奏'  # 用文件夹路径替换
merge_wav_files(folder_path)