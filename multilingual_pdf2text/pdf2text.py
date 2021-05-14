from multilingual_pdf2text.models.document_model.document import Document
from multilingual_pdf2text.doc2img.parse_document import PDF2Images
from multilingual_pdf2text.ocr.image_to_text import Image2Text
import logging

logging.basicConfig(level=logging.INFO)

class PDF2Text:
    """
    Extracts text content from pdf documents by keeping the format intact.
    """
    def __init__(self, document: Document):
        """
        Initializes extractors's configurations
        """
        self.document = document
        self.logger = logging.getLogger(__name__) ## get logger for logging system state

    def pdf2images(self):
        """
        Starts extracting text content from pdf file by first converting pdf to images
        then performing OCR on each image to keep formatting in tact.
        """
        pdf2image_converter = PDF2Images()
        images = pdf2image_converter.convert_document_to_images(self.document) ## create search instance
        return images
    
    def images2text(self, images):
        """
        Extract text content by performing OCR
        """
        pdf2image_converter = Image2Text(images=images, language=self.document.language)
        content = pdf2image_converter.get_text_content() ## extract text content from images
        return content
    
    def extract(self) -> list[str]:
        """
        Extract text content by performing OCR
        """
        images = self.pdf2images()
        content = self.images2text(images)
        return content
    
