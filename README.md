<p align="center">
    <a href="https://github.com/qqracha/youtube-downloader">
        <img src="https://github.com/qqracha/youtube-downloader/blob/main/resources/icon.png" alt="YouTube Downloader" title="YouTube Downloader" width="480" /><br/>
    </a><br/>
    <b>Simple YouTube Video Downloader</b>
    <br>
    Fast and minimalist tool for downloading YouTube videos
    <br><br>
    <a href="#features">features</a>
    &nbsp;•&nbsp;
    <a href="#installation">installation</a>
    &nbsp;•&nbsp;
    <a href="#usage">usage</a>
    &nbsp;•&nbsp;
    <a href="#screenshots">screenshots</a>
    <br/><br/>
    <img src="https://img.shields.io/github/license/qqracha/youtube-downloader" alt="License" />
    <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python Version" />
</p>

---


## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — Core download functionality
- [PyQt6](https://www.riverbankcomputing.com/software/pyqt/) — GUI framework
## Features

- ⚡ **Fast & Efficient** - Powered by yt-dlp for reliable downloads
- 📦 **Ready-to-use** — Pre-compiled executable for Windows (no Python installation needed)
- 🌐 **Cross-platform** - Works on Windows, Linux, and macOS
- 🎨 **Modern GUI** - Minimalist dark theme interface built with PyQt6
- 🖥️ **CLI Version** - Command-line interface for automation and scripting

## Installation

### Requirements

- Python 3.8 or higher


## Usage

### GUI Version

Run the graphical interface:


1. Paste a YouTube video URL
2. Select download folder (optional)
3. Click "Download"
4. Wait for completion

### CLI Version

Run the command-line version:


Follow the prompts to paste video URLs. Type `exit` or press Enter to quit.


**Issue:** "PyQt6 not found"

**Issue:** Download fails with error
- Try updating yt-dlp: `pip install --upgrade yt-dlp`
- Check your internet connection
- Verify the video URL is valid

## Building Executables

### Windows

pyinstaller --onefile --windowed --icon=resources/icon.ico yt_download_gui.py


### Linux

pyinstaller --onefile --windowed yt_download_gui.py


## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**qqracha**
- GitHub: [@qqracha](https://github.com/qqracha)


---

<p align="center">peace 🌸</p>
