<p align="center">
    <a href="https://github.com/qqracha/youtube-downloader">
        <img src="https://github.com/qqracha/youtube-downloader/blob/main/resources/icon.png" alt="YouTube Downloader" title="YouTube Downloader" width="280" />
    </a>
    <br><br>
    <h2>Youtube Downloader</h2>
    <br>
    <a>Fast and minimalist tool for downloading YouTube videos</a>
    <br>
    <a href="#features">features</a>
    &nbsp;•&nbsp;
    <a href="#issues">issues</a>
    &nbsp;•&nbsp;
    <a href="#build">build</a>
    <br/><br/>
    <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python Version" />
    <img src="https://img.shields.io/github/v/release/qqracha/youtube-downloader" alt="Release" />
</p>



## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — Core download functionality
- [PyQt6](https://www.riverbankcomputing.com/software/pyqt/) — GUI framework


## Features

- ⚡ **Fast & Efficient** - Powered by yt-dlp for reliable downloads
- 📦 **Ready-to-use** — Pre-compiled executable for Windows (no Python installation needed)
- 🌐 **Cross-platform** - Works on Windows, Linux, and macOS
- 🎨 **Modern GUI** - Minimalist dark theme interface built with PyQt6
- 🖥️ **CLI Version** - Command-line interface for automation and scripting


## Issues

Download fails with error:

- Try install requirements: `pip install -r requirements.txt`
- Check your internet connection
- Verify the video URL is valid

## Build

### Windows

pyinstaller --onefile --windowed --icon=resources/icon.ico yt_download_gui.py


### Linux

pyinstaller --onefile --windowed yt_download_gui.py


## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## Author

**qqracha**
- GitHub: [@qqracha](https://github.com/qqracha)


---

<p align="center">peace 🌸</p>
