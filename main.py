import yt_dlp
import os

def download_video():
    # Создаём папку для видео
    save_folder = "videos"
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
        print(f"✓ Папка '{save_folder}' создана")
    
    # Запрашиваем ссылку
    url = input("Вставьте ссылку на видео: ").strip()
    
    # Функция для отображения прогресса
    def progress_hook(d):
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', 'N/A')
            speed = d.get('_speed_str', 'N/A')
            eta = d.get('_eta_str', 'N/A')
            print(f"\rСкачивание: {percent} | Скорость: {speed} | Осталось: {eta}", end='')
        elif d['status'] == 'finished':
            print(f"\n✓ Скачивание завершено!")
            print(f"  Обработка файла...")
    
    # Настройки скачивания
    ydl_opts = {
        # Универсальный формат - берёт лучшее доступное
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        
        # Объединять видео и аудио в MP4
        'merge_output_format': 'mp4',
        
        # Путь и имя файла
        'outtmpl': os.path.join(save_folder, '%(title)s.%(ext)s'),
        
        # Не скачивать плейлисты
        'noplaylist': True,
        
        # Показывать прогресс
        'progress_hooks': [progress_hook],
        
        # Настройки для обхода ограничений YouTube
        'extractor_args': {
            'youtube': {
                'player_client': ['android', 'web'],
            }
        },
        
        # Тихий режим (убирает лишние сообщения)
        'quiet': False,
        'no_warnings': False,
    }
    
    # Скачиваем видео
    try:
        print("\nНачинаю скачивание...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            print(f"\n✓ Видео сохранено: {filename}")
            print(f"✓ Название: {info.get('title', 'Неизвестно')}")
            print(f"✓ Длительность: {info.get('duration', 0) // 60} мин")
            
    except yt_dlp.utils.DownloadError as e:
        print(f"\n✗ Ошибка скачивания: {e}")
        print("\nПопытка с упрощённым форматом...")
        
        # Запасной вариант - просто лучшее доступное
        ydl_opts['format'] = 'best'
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                print("\n✓ Скачано с упрощённым форматом!")
        except Exception as e2:
            print(f"\n✗ Не удалось скачать: {e2}")
            
    except Exception as e:
        print(f"\n✗ Неожиданная ошибка: {e}")

if __name__ == "__main__":
    print("=" * 50)
    print("  YouTube Video Downloader (yt-dlp)")
    print("=" * 50)
    download_video()
    print("\nГотово!")
