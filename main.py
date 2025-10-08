import yt_dlp
import os

# Ссылка на YouTube-видео
save_folder = "videos"

if not os.path.exists(save_folder):
    os.makedirs(save_folder)
    print(f"> Папка {save_folder} создана.")

url = input("> Paste video link: ")

# Настройки скачивания
ydl_opts = {
    'format': 'best',               # скачать лучшее качество видео+аудио
    'outtmpl': os.path.join(save_folder, '%(title)s.%(ext)s'), # имя файла: название видео + расширение
    'noplaylist': True,             # не скачивать весь плейлист, только одно видео
    'progress_hooks': [],            # можно добавить хук для прогресса
    'concurrent_fragment_downloads': 5,  # скачиваем 5 частей одновременно
}

# Функция для отображения прогресса
def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"Скачивание: {d['_percent_str']} Скорость: {d['_speed_str']} Осталось: {d['_eta_str']}")
    elif d['status'] == 'finished':
        print(f"Скачивание завершено: {d['filename']}")

ydl_opts['progress_hooks'].append(progress_hook)

# Скачиваем видео
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
