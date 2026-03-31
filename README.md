# 🔲 QRCodeGenerator

A lightweight Python tool to generate custom QR codes from any text or URL, exported as a `.png` file.

---

## 📋 Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`

---

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/raultejada24/QRCodeGenerator.git
   cd QRCodeGenerator
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

1. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate           # Windows
   ```

2. **Run the script:**
   ```bash
   python main.py
   ```

3. **Follow the prompts:**
   - **URL / Text**: The link or text to encode into the QR code.
   - **Output name**: The name of the output file (`.png` is added automatically).

---

## 📁 Project Structure

```
QRCodeGenerator/
├── main.py              # Main generation script
├── requirements.txt     # Project dependencies
└── .gitignore           # Excludes venv and test images from Git
```

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
