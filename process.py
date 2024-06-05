import json
import os
import re


def process_json_folder(json_folder_path, wav_path, character_name):
    with open('output.list', 'w', encoding='utf-8') as output_file, open('audio_files.txt', 'w',
                                                                         encoding='utf-8') as audio_file:
        for filename in os.listdir(json_folder_path):
            if filename.endswith('.json'):
                json_path = os.path.join(json_folder_path, filename)
                print(f'Processing {json_path}')
                parse_json(json_path, wav_path, character_name, output_file, audio_file)


def get_wav_files(wav_path):
    wav_files = [f for f in os.listdir(wav_path) if f.endswith('.wav')]
    return wav_files


def parse_json(json_path, wav_path, character_name, output_file, audio_file):
    wav_files = get_wav_files(wav_path)

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    scenes = data['scenes']

    for scene in scenes:
        if scene and 'texts' in scene:
            texts = scene.get('texts')

            for text in texts:
                if text:
                    if text[3]:
                        if text[3][0]['name'] == character_name:

                            dialogue = text[2][0][1]

                            dialogue = re.sub(r'　', '', dialogue)
                            dialogue = re.sub(r'\\\\n', '', dialogue)
                            dialogue = re.sub(r'\[.+?\]', '', dialogue)
                            dialogue = re.sub(r'「|」', '', dialogue)
                            dialogue = re.sub(r'（|）', '', dialogue)
                            dialogue = re.sub(r'%.+;+', '', dialogue)
                            dialogue = re.sub(r'♪', '', dialogue)   # 用于删除特殊符号,此段代码来自bfloat大佬
                            dialogue = re.sub(r'●', '', dialogue)   # https://github.com/bfloat16/Audio_Tools/blob/main/python/TextCleaner_Kirikiri_scn.py
                            dialogue = re.sub(r'。\\n', '。', dialogue)
                            dialogue = re.sub(r'\\n', '。', dialogue)

                            if f'{text[3][0]["voice"]}.wav' in wav_files:
                                file_pos = f'{text[3][0]["voice"]}.wav'
                                wav_files.remove(file_pos)
                                line = f'{wav_path}\\{file_pos}|{character_name}|JA|{dialogue}'
                                output_file.write(line + '\n')
                                audio_file.write(f'{file_pos}\n')


json_folder_path = r'E:\gal\解包\魔女的夜宴\scn'
wav_path = r'E:\gal\解包\魔女的夜宴\voice\寧々'
character_name = '寧々'

process_json_folder(json_folder_path, wav_path, character_name)
