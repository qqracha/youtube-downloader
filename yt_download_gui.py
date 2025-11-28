import sys
import os
import subprocess
import platform
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLineEdit, QPushButton, QTextEdit, 
                             QProgressBar, QFileDialog, QLabel)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtGui import QFont, QIcon
import yt_dlp


class DownloadThread(QThread):
    """Thread for downloading video in background"""
    progress = pyqtSignal(str, int)  # (text, percentage)
    finished = pyqtSignal(str)
    error = pyqtSignal(str)
    
    def __init__(self, url, save_folder):
        super().__init__()
        self.url = url
        self.save_folder = save_folder
        
    def progress_hook(self, d):
        if d['status'] == 'downloading':
            percent_str = d.get('_percent_str', '0%')
            speed = d.get('_speed_str', 'N/A')
            eta = d.get('_eta_str', 'N/A')
            
            # Extract percentage
            try:
                percent = float(percent_str.strip('%'))
            except:
                percent = 0
                
            text = f"Downloading: {percent_str} | Speed: {speed} | ETA: {eta}"
            self.progress.emit(text, int(percent))
            
        elif d['status'] == 'finished':
            self.progress.emit("Processing file...", 100)
    
    def run(self):
        try:
            # Create folder if it doesn't exist
            if not os.path.exists(self.save_folder):
                os.makedirs(self.save_folder)
            
            # Download settings
            ydl_opts = {
                'format': 'bestvideo[ext=mp4][height<=2160]+bestaudio[ext=m4a]/bestvideo+bestaudio/best',
                'merge_output_format': 'mp4',
                'outtmpl': os.path.join(self.save_folder, '%(title)s.%(ext)s'),
                'noplaylist': True,
                'progress_hooks': [self.progress_hook],
                'extractor_args': {
                    'youtube': {
                        'player_client': ['android', 'web'],
                    }
                },
                'quiet': True,
                'no_warnings': True,
                'color': 'no_color',
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(self.url, download=True)
                
                title = info.get('title', 'Unknown')
                width = info.get('width', 'N/A')
                height = info.get('height', 'N/A')
                duration = info.get('duration', 0)
                
                result = f"Video downloaded successfully!\n"
                result += f"Title: {title}\n"
                result += f"Resolution: {width}x{height}\n"
                result += f"Duration: {duration // 60} min {duration % 60} sec"
                
                self.finished.emit(result)
                
        except Exception as e:
            self.error.emit(f"Error: {str(e)}")


class YouTubeDownloader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.save_folder = "videos"
        self.download_thread = None
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle('YouTube Downloader')
        self.setGeometry(100, 100, 700, 500)
        self.setWindowIcon(QIcon('resources\icon.png'))
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Title
        title = QLabel('YouTube Video Downloader')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont('Segoe UI', 22, QFont.Weight.Bold))
        layout.addWidget(title)
        
        # URL input
        url_layout = QHBoxLayout()
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText('Paste video URL here...')
        self.url_input.setMinimumHeight(45)
        self.url_input.returnPressed.connect(self.start_download)
        url_layout.addWidget(self.url_input)
        layout.addLayout(url_layout)
        
        # Buttons
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(10)
        
        self.folder_btn = QPushButton('Select Folder')
        self.folder_btn.setMinimumHeight(45)
        self.folder_btn.clicked.connect(self.choose_folder)
        buttons_layout.addWidget(self.folder_btn)
        
        self.download_btn = QPushButton('Download')
        self.download_btn.setMinimumHeight(45)
        self.download_btn.clicked.connect(self.start_download)
        buttons_layout.addWidget(self.download_btn, 2)

        self.open_folder_btn = QPushButton('Open Folder')
        self.open_folder_btn.setMinimumHeight(45)
        self.open_folder_btn.clicked.connect(self.open_folder)
        buttons_layout.addWidget(self.open_folder_btn)
        
        
        layout.addLayout(buttons_layout)
        
        # Save path
        self.path_label = QLabel(f'Save folder: {os.path.abspath(self.save_folder)}')
        self.path_label.setWordWrap(True)
        layout.addWidget(self.path_label)
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimumHeight(8)
        self.progress_bar.setTextVisible(False)
        layout.addWidget(self.progress_bar)
        
        # Log
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setMinimumHeight(200)
        layout.addWidget(self.log_text)
        
        central_widget.setLayout(layout)
        
        # Apply style
        self.apply_style()
        
        # Welcome message
        self.log("Ready! ( ͡° ͜ʖ ͡°)")
        
    def apply_style(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e2e;
            }
            QWidget {
                background-color: #1e1e2e;
                color: #cdd6f4;
                font-family: 'Segoe UI', Arial;
                font-size: 13px;
            }
            QLabel {
                color: #cdd6f4;
            }
            QLineEdit {
                background-color: #313244;
                border: 2px solid #45475a;
                border-radius: 8px;
                padding: 10px 15px;
                color: #cdd6f4;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #89b4fa;
            }
            QPushButton {
                background-color: #89b4fa;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
                color: #1e1e2e;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #74c7ec;
            }
            QPushButton:pressed {
                background-color: #6c9bcf;
            }
            QPushButton:disabled {
                background-color: #45475a;
                color: #6c7086;
            }
            QTextEdit {
                background-color: #313244;
                border: 2px solid #45475a;
                border-radius: 8px;
                padding: 10px;
                color: #cdd6f4;
                font-family: 'Consolas', monospace;
                font-size: 12px;
            }
            QProgressBar {
                background-color: #313244;
                border: none;
                border-radius: 4px;
            }
            QProgressBar::chunk {
                background-color: #a6e3a1;
                border-radius: 4px;
            }
        """)
        
    def choose_folder(self):
        folder = QFileDialog.getExistingDirectory(self, 'Select save folder')
        if folder:
            self.save_folder = folder
            self.path_label.setText(f'Save folder: {self.save_folder}')
            self.log(f"Folder changed: {self.save_folder}")
    
    def open_folder(self):
        """Opens the video folder in file manager"""
        # Create folder if it doesn't exist yet
        if not os.path.exists(self.save_folder):
            os.makedirs(self.save_folder)
            
        folder_path = os.path.abspath(self.save_folder)
        
        try:
            system = platform.system()
            
            if system == 'Windows':
                os.startfile(folder_path)
            elif system == 'Darwin':
                subprocess.Popen(['open', folder_path])
            else:
                subprocess.Popen(['xdg-open', folder_path])
            
        except Exception as e:
            self.log(f"Failed to open folder: {e}")
    
    def start_download(self):
        url = self.url_input.text().strip()
        
        if not url:
            self.log("Please enter a video URL!")
            return
            
        if self.download_thread and self.download_thread.isRunning():
            self.log("Download already in progress!")
            return
        
        # Disable buttons
        self.download_btn.setEnabled(False)
        self.url_input.setEnabled(False)
        self.folder_btn.setEnabled(False)
        
        # Reset progress
        self.progress_bar.setValue(0)
        self.log(f"\nStarting download...")
        self.log(f"URL: {url}")
        
        # Start thread
        self.download_thread = DownloadThread(url, self.save_folder)
        self.download_thread.progress.connect(self.update_progress)
        self.download_thread.finished.connect(self.download_finished)
        self.download_thread.error.connect(self.download_error)
        self.download_thread.start()
    
    def update_progress(self, text, percentage):
        self.progress_bar.setValue(percentage)
        self.log(text)
    
    def download_finished(self, result):
        self.log(f"\n{result}")
        self.progress_bar.setValue(100)
        self.enable_controls()
    
    def download_error(self, error):
        self.log(f"\n{error}")
        self.progress_bar.setValue(0)
        self.enable_controls()
    
    def enable_controls(self):
        self.download_btn.setEnabled(True)
        self.url_input.setEnabled(True)
        self.folder_btn.setEnabled(True)
        self.url_input.clear()
        self.url_input.setFocus()
    
    def log(self, message):
        self.log_text.append(message)
        # Scroll to bottom
        self.log_text.verticalScrollBar().setValue(
            self.log_text.verticalScrollBar().maximum()
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YouTubeDownloader()
    window.show()
    sys.exit(app.exec())
