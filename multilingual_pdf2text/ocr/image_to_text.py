import logging
import pytesseract
logging.basicConfig(level=logging.INFO)

class Image2Text:
    """
    Extracts relevant information from HTML markdown for Job Ids and Job detail.
    """
    def __init__(self, images):
        self.logger = logging.getLogger(__name__)
        self.images = images
    
    def get_text_content(self) -> list[str]:
        """
        Converts the list of Images to list of strings.
        """
        self.logger.info('Extracting text from images via OCR')
        ## Parse all images and extract text
        content = []
        try:
            for image_idx, image in enumerate(self.images):
                text = pytesseract.image_to_string(image)
                content.append({
                    'page_number': image_idx + 1,
                    'text': text
                })
        except Exception as exception:
           self.logger.info(f"{exception}")
           
        return content
