# Multilingual PDF to Text.

## Install Package from Pypi
1. Install it using pip.
```bash
pip install linkedin-jobs-pyscraper
```
## Example Usage
2. Use it in your code
```python
from multilingual_pdf2text.pdf2text import PDF2Text
from multilingual_pdf2text.models.document_model.document import Document
import logging
logging.basicConfig(level=logging.INFO)

def main():
    ## create document for extraction with configurations
    pdf_document = Document(
        document_path='/Users/shahrukh/Desktop/multilingual-pdf2text/example/python_intro.pdf',
        language='en'
        )
    pdf2text = PDF2Text(document=pdf_document)
    content = pdf2text.extract()
    print(content)

if __name__ == "__main__":
    main()
```

The library can crawl the following fields of data:
* _id	
* job_title	
* description	
* location	
* employer_name	
* date_posted	
* n_applicants	
* seniority level	
* employment type	
* job function	
* industries_0	
* industries_1	
* industries_2
