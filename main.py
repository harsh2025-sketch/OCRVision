from video_extractor import get_video_frames
from ocr_processor import perform_ocr
from text_summarizer import summarize_text

def process_video(video_url):
    print("Extracting frames...")
    frames = get_video_frames(video_url)
    print("Performing OCR...")
    text = perform_ocr(frames)
    print("Summarizing text...")
    summary = summarize_text(text)
    return summary

def main():
    while True:
        url = input("Enter YouTube URL (or 'quit'): ")
        if url.lower() == 'quit':
            break
        try:
            summary = process_video(url)
            print("\nSummary:")
            print(summary)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
