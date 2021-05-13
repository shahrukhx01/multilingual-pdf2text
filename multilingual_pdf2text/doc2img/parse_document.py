import logging
from pdf2image import convert_from_path, convert_from_bytes
from multilingual_pdf2text.models.document_model.document import Document
from PIL.PpmImagePlugin import PpmImageFile
logging.basicConfig(level=logging.INFO)

class PDF2Images:
    """
    Extracts relevant information from HTML markdown for Job Ids and Job detail.
    """
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def convert_document_to_images(self, document: Document) -> list[PpmImageFile]:
        """
        Converts the Document object to 
        Keyword arguments:
        document -- Document
        """
        self.logger.info('Parsing document from pdf to image')
        ## Parse all pages of PDF document to images.
        images = []
        try:
            images = convert_from_path(document.document_path)
        except Exception as exception:
           self.logger.info(f"{exception}")
        return images
