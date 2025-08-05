import pytesseract
from PIL import Image

# Set the path to tesseract.exe if not in PATH
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def ocr_from_local(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

def check_ocr_accuracy(text, expected_text):
    if not expected_text:
        return 0.0
    words_in_text = set(text.lower().split())
    words_in_expected = set(expected_text.lower().split())
    matched = len(words_in_text & words_in_expected)
    total_expected = len(words_in_expected)
    return (matched / total_expected) * 100 if total_expected > 0 else 0.0


if __name__ == "__main__":
    image_path = "images/picture1.png" # relative path
    expected_text = "This is the sample text that should be in the image"

    ocr_text = ocr_from_local(image_path)
    print("Extracted Text:\n", ocr_text)

    accuracy = check_ocr_accuracy(ocr_text, expected_text)
    print(f"OCR Accuracy: {accuracy:.2f}%")

    if accuracy < 80:
        print("OCR accuracy too low.")
        exit(1)
