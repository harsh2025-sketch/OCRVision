import yt_dlp
import cv2
import re

def extract_video_id(url):
    patterns = [
        r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?(?:shorts\/)?(?:embed\/)?(?:v\/)?(?:\.+\?v=)?([^&=%\?]{11})',
        r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:shorts\/)?([^&=%\?]{11})'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def get_video_frames(video_url, frame_interval=10, max_frames=100):
    video_id = extract_video_id(video_url)
    if not video_id:
        raise ValueError("Invalid YouTube URL")

    ydl_opts = {'format': 'best'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
        url = info['url']

    cap = cv2.VideoCapture(url)
    frames = []
    frame_count = 0
    while cap.isOpened() and len(frames) < max_frames:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % frame_interval == 0:
            frames.append(frame)
        frame_count += 1

    cap.release()
    return frames

if __name__ == "__main__":
    while True:
        video_url = input("Enter a YouTube video URL (or 'quit' to exit): ")
        if video_url.lower() == 'quit':
            break
        
        try:
            frames = get_video_frames(video_url)
            print(f"Successfully extracted {len(frames)} frames from the video.")
            
            # Optional: Save a sample frame as an image
            if frames:
                cv2.imwrite('sample_frame.jpg', frames[0])
                print("Saved the first frame as 'sample_frame.jpg'")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        
        print()  # Add a blank line for readability
