# Label Automation v2.0

Label Automation v2.0 is a modern, user-friendly desktop application for scanning folders and analyzing the sensitivity of files based on their content. With a sleek drag-and-drop interface, it helps organizations and individuals quickly identify confidential, PII, and public information in documents, images, and more.

## Features
- **Drag-and-drop or browse to select folders**
- **Automatic recursive scanning** of all files in the selected directory
- **Content analysis** using customizable rules (JSON-based)
- **Supports multiple file types:**
  - Text files (.txt)
  - Word documents (.docx)
  - PDFs (including scanned/image-based PDFs)
  - Images (OCR via Tesseract)
- **Modern, minimal, dark-themed GUI**
- **Progress bar and real-time results display**
- **Easy packaging as a standalone .exe**

## How It Works
1. **Select or drag-and-drop a folder** into the app.
2. The app scans all files in the folder and subfolders.
3. Each file is analyzed for sensitivity using rules defined in `config/rules.json`.
4. Results are displayed in the app, showing the sensitivity level for each file.

## Installation
1. **Clone or download this repository.**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install customtkinter tkinterdnd2 pytesseract pillow python-docx pypdf
   ```
   - You must also [install Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) and add it to your PATH for image/PDF OCR support.
3. **Run the app:**
   ```bash
   python src/gui.py
   ```

## Packaging as an Executable
To create a standalone `.exe`:
```bash
pip install pyinstaller
pyinstaller --noconsole --onefile --add-data "config;config" src/gui.py
```
The executable will be in the `dist/` folder.

## Customizing Sensitivity Rules
Edit `config/rules.json` to add or change keywords for each sensitivity category. The app will use these rules for all future scans.

## Screenshots
![alt text](<Screenshot 2025-06-17 091848-1.png>)

## License
MIT License

## Credits
- Built with [customtkinter](https://github.com/TomSchimansky/CustomTkinter), [tkinterdnd2](https://github.com/pmgagne/tkinterdnd2), [PyInstaller](https://pyinstaller.org/), and [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).

---

**Label Automation v2.0** makes file sensitivity analysis fast, easy, and visually appealing. Perfect for compliance, audits, or personal data management!