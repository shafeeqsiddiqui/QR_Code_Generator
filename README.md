# 🔳 QR Code Generator Project

This project demonstrates how to generate both standard black-and-white and colorful QR codes using Python. It leverages the `qrcode` library for QR code generation and the `PIL` (Python Imaging Library) for image manipulation and enhancement.

---

## 🎯 Project Overview

QR codes are widely used to encode URLs, text, or other data into a machine-readable format. This project includes:

- A **simple black-and-white QR code generator**
- A **customized colorful QR code generator**

Both implementations are beginner-friendly and demonstrate how to extend functionality using external Python libraries.

---

## 📦 Libraries Used

- [`qrcode`](https://pypi.org/project/qrcode/): To generate QR codes.
- [`PIL` (Pillow)](https://pillow.readthedocs.io/): For image customization and saving.

Install required packages (if not already installed):

```bash
pip install qrcode[pil]


📂 Functionality
✅ 1. Black & White QR Code (black_white_qr.py)
This script generates a standard QR code with default black foreground and white background.

Input: Text or URL

Output: PNG image file with QR code

🎨 2. Colorful QR Code (colorful_qr.py)
This script customizes the QR code using:

fill_color: Foreground color of the QR pattern

back_color: Background color of the QR image

Customize your QR code with your brand colors or design preferences!


