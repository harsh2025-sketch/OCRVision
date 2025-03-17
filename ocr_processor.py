import pytesseract
import cv2
import numpy as np

# Set the correct path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'D:\AI models\teceract\tesseract.exe'

def perform_ocr(frames):
    """
    Perform OCR on a list of frames.
    
    Args:
    frames (list): List of numpy arrays representing images.
    
    Returns:
    str: Extracted text from all frames.
    """
    text = ""
    for frame in frames:
        # Convert BGR to RGB if necessary
        if len(frame.shape) == 3 and frame.shape[2] == 3:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        else:
            rgb_frame = frame
        
        # Use pytesseract to do OCR on the frame
        try:
            frame_text = pytesseract.image_to_string(rgb_frame)
            text += frame_text + "\n"
        except Exception as e:
            print(f"Error processing frame: {str(e)}")
    
    return text

def test_ocr():
    """
    Test the OCR functionality with a sample image.
    """
    try:
        # Load a sample image (replace 'sample_frame.jpg' with your actual image file)
        sample_image = cv2.imread('sample_frame.jpg')
        
        if sample_image is None:
            raise FileNotFoundError("Sample image not found")
        
        # Perform OCR on the sample image
        extracted_text = perform_ocr([sample_image])
        
        print("OCR Test Result:")
        print(extracted_text)
        
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    print("Tesseract path:", pytesseract.pytesseract.tesseract_cmd)
    print("Tesseract version:", pytesseract.get_tesseract_version())
    test_ocr()
