import cv2
import pytesseract
import re

# Read and preprocess the image
img = cv2.imread('deo.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding to improve contrast
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY, 11, 2)

# Optional: Reduce noise using median blur
processed_img = cv2.medianBlur(thresh, 3)

# Extract text using pytesseract
extracted_text = pytesseract.image_to_string(processed_img)
print("Extracted Text:", extracted_text)

# Define regex patterns for extracting expiry date and MFG date
date_pattern = r'(\d{2}/\d{4}|\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}|\d{2}\.\d{2}\.\d{4})'
expiry_date_pattern = rf'(U\.B|EXP|Expiry|Exp|Best Before)\s*[:\-]?\s*{date_pattern}'
mfg_date_pattern = rf'(MFD|Mfg|Manufactured|Mfd|Manufacture Date)\s*[:\-]?\s*{date_pattern}'

# Search for expiry date
expiry_date_match = re.search(expiry_date_pattern, extracted_text, re.IGNORECASE)
expiry_date = expiry_date_match.group(2) if expiry_date_match else 'Not Found'

# Search for MFG date
mfg_date_match = re.search(mfg_date_pattern, extracted_text, re.IGNORECASE)
mfg_date = mfg_date_match.group(2) if mfg_date_match else 'Not Found'