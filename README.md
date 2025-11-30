![OCRVision Header](readme_header.png)

# 🎥 OCRVision

## 📋 Overview

**OCRVision** is a Python-based tool that extracts, processes, and summarizes textual information from YouTube videos. It combines video frame extraction, Optical Character Recognition (OCR), and AI-powered text summarization to transform video content into concise, readable summaries.

## ✨ Features

- 🎬 **YouTube Video Processing**: Extract frames from any YouTube video URL
- 🔍 **OCR Technology**: Extract text from video frames using Tesseract OCR
- 🤖 **AI Summarization**: Generate concise summaries using transformer models
- 🔄 **Batch Processing**: Process multiple videos in a single session
- 📊 **Frame Sampling**: Intelligent frame extraction at configurable intervals

## 🏗️ Project Structure

```
OCRVision/
├── main.py                 # Main application entry point
├── video_extractor.py      # YouTube video frame extraction
├── ocr_processor.py         # OCR processing with Tesseract
├── text_summarizer.py       # AI-powered text summarization
├── requirements.txt         # Project dependencies
└── .gitignore              # Git ignore rules
```

## 🔧 Prerequisites

Before running this project, ensure you have:

1. **Python 3.8+** installed
2. **Tesseract OCR** installed on your system
   - Windows: Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
   - Linux: `sudo apt-get install tesseract-ocr`
   - macOS: `brew install tesseract`

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/harsh2025-sketch/OCRVision.git
cd OCRVision
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure Tesseract path**
   - Open `ocr_processor.py`
   - Update line 6 with your Tesseract installation path:
```python
pytesseract.pytesseract.tesseract_cmd = r'YOUR_TESSERACT_PATH'
```

## 🚀 Usage

Run the main application:
```bash
python main.py
```

The program will prompt you to enter a YouTube URL. Example workflow:
```
Enter YouTube URL (or 'quit'): https://www.youtube.com/watch?v=example
Extracting frames...
Performing OCR...
Summarizing text...

Summary:
[Your summarized content will appear here]
```

## 📚 How It Works

1. **Frame Extraction** (`video_extractor.py`)
   - Accepts YouTube URL and extracts video ID
   - Downloads video stream using yt-dlp
   - Extracts frames at regular intervals (default: every 10th frame, max 100 frames)

2. **OCR Processing** (`ocr_processor.py`)
   - Processes extracted frames using Tesseract OCR
   - Converts images from BGR to RGB format
   - Extracts text content from each frame

3. **Text Summarization** (`text_summarizer.py`)
   - Uses Hugging Face transformers pipeline
   - Chunks large text into manageable segments
   - Generates concise summaries with configurable length

## ⚙️ Configuration

Customize extraction parameters in `video_extractor.py`:
- `frame_interval`: Number of frames to skip between extractions (default: 10)
- `max_frames`: Maximum number of frames to extract (default: 100)

Adjust summarization in `text_summarizer.py`:
- `max_length`: Maximum summary length (default: 150)
- `min_length`: Minimum summary length (default: 50)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is open-source and available under the MIT License.


---
⭐ If you find this project useful, please consider giving it a star!
