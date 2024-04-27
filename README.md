# Website QR Code Generator

## Description
This Python script allows users to generate QR codes for website links. It provides a simple and user-friendly interface for generating QR codes with customizable colors.

## Features
- Input validation for website links to ensure only valid URLs are accepted.
- Customizable QR code colors: Users can choose between black or white QR codes.
- Unique filename generation for each QR code image to avoid overwriting existing files.
- User interaction loop for generating multiple QR codes in a single session.

## Requirements
- Python 3.x
- qrcode library (`pip install qrcode`)
- validators library (`pip install validators`)

## Usage
1. Run the script (`python qr_generator.py`).
2. Enter the website link when prompted.
3. Choose the color of the QR code (black or white).
4. The generated QR code image will be saved in the same directory as the script with a unique filename.
5. Repeat steps 2-4 to generate additional QR codes.
6. To exit, type "no" when prompted to generate another QR code.
