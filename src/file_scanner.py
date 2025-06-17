#Contains logic for recursively scanning directory
#Manages file operations
import os
import pytesseract
from PIL import Image
import docx
import pypdf
import logging
from typing import Optional # Type hint for optional parameters

class FileScanner:
    def __init__(self):
        """
        Initializes the FileScanner class.
        This class is responsible for scanning directories and reading files.
        """
        self.supported_images = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp')  # Supported image file extensions
        self.logger = logging.getLogger(__name__)  # Logger for logging messages

    '''
        def scan_directory(self, path):
            """
            Recursively scans the directory for files.
            
            Args:
                path (str): The path to the directory to scan.
            
            Returns:
                list: A list of file paths found in the directory.
            """
            files = []
            for root, _, filenames in os.walk(path): # Walk through the directory tree
                for filename in filenames: # Check each file in the directory
                    file_path = os.path.join(root, filename) # Construct the full file path
                    content = self.read_file(file_path)  # Read the file content
                    if content:
                        files.append({
                            'path': file_path,  # Store the file path
                            'content': content  # Store the file content
                        })
            return files  # Return the list of files found
        '''
                    

    def read_file(self, file_path) -> Optional[str]:
        """
        Reads the content of a file.
        
        Args:
            file_path (str): The path to the file to read.
    
        Returns:
            str: The content of the file, or None if the file is empty or could not be read.
        """
        extension = os.path.splitext(file_path)[1].lower()  # Get the file extension in lowercase
        try:
            if extension == '.txt':
                return self._read_txt(file_path)  # Read text files
            elif extension == '.pdf':
                return self._read_pdf(file_path)  # Read PDF files
            elif extension == ".docx": 
                return self._read_docx(file_path) # Read DOCX files
            elif extension in self.supported_images:
                return self._read_image(file_path)  # Read image files
            else:
                self.logger.warning(f"Unsupported file type: {extension}")
                return None
        except Exception as e:
            self.logger.error(f"Error reading file {file_path}: {str(e)}") # Log the error
            return None
        
    def _read_txt(self, file_path) -> str:
        """
        Reads the content of a text file.
        
        Args:
            file_path (str): The path to the text file.
        
        Returns:
            str: The content of the text file.
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().strip()  # Read and return the content of the text file
        
    def _read_pdf(self, file_path) -> str:
        """
        Reads the content of a PDF file.
        
        Args:
            file_path (str): The path to the PDF file.
        
        Returns:
            str: The content of the PDF file.
        """
        text = []
        images = []
        try:
            with open(file_path, 'rb') as file:
                reader = pypdf.PdfReader(file)  # Create a PDF reader object
                for page in reader.pages:  # Iterate through each page
                    # Extract text from the page
                    extracted_text = page.extract_text()
                    if extracted_text:
                        text.append(extracted_text)
                    # Extract images from the page using pypdf's .images property if available
                    if hasattr(page, "images"):
                        for img in page.images:
                            images.append(img)
    #                else:
    #                    # Fallback for older pypdf versions: extract from /XObject
    #                    if "/XObject" in page.resources:
    #                        xObject = page.resources["/XObject"]
    #                        for obj_name in xObject:
    #                            obj = xObject[obj_name]
    #                            if obj.get("/Subtype") == "/Image":
    #                                images.append(obj)
            if images:
                for img in images:
                    try:
                        text.append(pytesseract.image_to_string(img.image))  # Use Tesseract to extract text from the image (img.image object and property from pypdf)
                    except Exception as e:
                        self.logger.error(f"Error extracting text from image in PDF {file_path}: {str(e)}")
            return '\n'.join(text).strip()  # Join and return the extracted text
        except Exception as e:
            self.logger.error(f"Error reading PDF file {file_path}: {str(e)}")  # Log the error
            return ""
        
    def _read_docx(self, file_path) -> str:
        """
        Reads the content of a DOCX file.
        
        Args:
            file_path (str): The path to the DOCX file.
        
        Returns:
            str: The content of the DOCX file.
        """
        try:
            doc = docx.Document(file_path)  # Open the DOCX file
            return '\n'.join([para.text for para in doc.paragraphs]).strip()  # Join and return the text from paragraphs
        except Exception as e:
            self.logger.error(f"Error reading DOCX file {file_path}: {str(e)}")  # Log the error
            return ""
        


    def _read_image(self, file_path) -> str:
        """
        Reads the content of an image file using OCR.
        
        Args:
            file_path (str): The path to the image file.
        
        Returns:
            str: The text extracted from the image.
        """
        try:
            image = Image.open(file_path)  # Open the image fil
            text = pytesseract.image_to_string(image)  # Use Tesseract to extract text from the image
            return text.strip()  # Return the extracted text
        except Exception as e:
            self.logger.error(f"Error reading image file {file_path}: {str(e)}")  # Log the error
            return ""