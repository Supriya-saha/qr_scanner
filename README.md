# QR Scanner Application

A Python-based QR code scanner that detects QR codes from your webcam and automatically opens URLs encoded within them.

## System Requirements (Windows)

- **Operating System**: Windows 7 or later
- **Python**: 3.7 or higher
- **Webcam**: Required for scanning QR codes

## Installation

### 1. Clone or Download the Repository
```bash
cd e:\Stethaim\qr_scanner
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
```

### 3. Activate Virtual Environment
```bash
# For Windows PowerShell
.\venv\Scripts\Activate.ps1

# For Windows Command Prompt
.\venv\Scripts\activate.bat
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install opencv-python
```

## Running the Application

### Start the QR Scanner
```bash
python main.py
```

### Exit the Scanner
Press `q` to quit the scanner while it's running.

## Project Structure

```
qr_scanner/
├── main.py          # Entry point of the application
├── scanner.py       # QR code detection and scanning logic
├── parser.py        # URL parsing and data extraction
├── display.html     # HTML page for displaying query parameters
├── requirements.txt # Python dependencies
└── README.md        # This file
```

## Features

- Real-time QR code detection using webcam
- Automatic URL opening when QR code is detected
- Visual feedback with animated boundary detection
- Clean exit functionality

## How It Works

1. The application opens your default webcam
2. It continuously scans for QR codes in the video feed
3. When a QR code is detected, it:
   - Displays a green bounding box around the code
   - Shows an animation effect
   - Automatically opens the embedded URL in your default browser
   - Closes the scanner

## Dependencies

- **opencv-python**: Computer vision library for QR code detection and image processing
- **Python standard library**: `webbrowser`, `time`

## Troubleshooting

### Camera Not Found
- Ensure your webcam is connected and not in use by another application
- Check if your antivirus software is blocking camera access

### QR Code Not Detected
- Ensure the QR code is clearly visible and well-lit
- Try moving the QR code closer to the camera
- Ensure the QR code is not too small or too blurry

### Module Not Found Errors
Make sure all dependencies are installed in your virtual environment:
```bash
pip install -r requirements.txt
```

## Development Notes

The application uses OpenCV's built-in `QRCodeDetector` which doesn't require additional DLL dependencies on Windows, ensuring cross-platform compatibility.

## License

For personal use only.
