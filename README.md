# Multilingual PDF to Text.

## Install Package from Pypi
1. Install it using pip.
```bash
pip install linkedin-jobs-pyscraper
```
The library uses Tesseract which can be installed by following instructions:
 
[Tesseract Installation](https://tesseract-ocr.github.io/tessdoc/Installation.html)

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

Tesseract supports the following languages:
Code	Language
* afr	Afrikaans	
* amh	Amharic	
* ara	Arabic	
* asm	Assamese	
* aze	Azerbaijani	
* aze_cyrl	Azerbaijani - Cyrillic	aze_
* bel	Belarusian	
* ben	Bengali	
* bod	Tibetan	
* bos	Bosnian	
* bul	Bulgarian	
* cat	Catalan; Valencian	
* ceb	Cebuano	
* ces	Czech	
* chi_sim	Chinese - Simplified	chi_
* chi_tra	Chinese - Traditional	chi_
* chr	Cherokee	
* cym	Welsh	
* dan	Danish	
* deu	German	
* dzo	Dzongkha	
* ell	Greek, Modern (1453-)	
* eng	English	
* enm	English, Middle (1100-1500)	
* epo	Esperanto	
* est	Estonian	
* eus	Basque	
* fas	Persian	
* fin	Finnish	
* fra	French	
* frk	German Fraktur	
* frm	French, Middle (ca. 1400-1600)	
* gle	Irish	
* glg	Galician	
* grc	Greek, Ancient (-1453)	
* guj	Gujarati	
* hat	Haitian; Haitian Creole	
* heb	Hebrew	
* hin	Hindi	
* hrv	Croatian	
* hun	Hungarian	
* iku	Inuktitut	
* ind	Indonesian	
* isl	Icelandic	
* ita	Italian	
* ita_old	Italian - Old	ita_
* jav	Javanese	
* jpn	Japanese	
* kan	Kannada	
* kat	Georgian	
* kat_old	Georgian - Old	kat_
* kaz	Kazakh	
* khm	Central Khmer	
* kir	Kirghiz; Kyrgyz	
* kor	Korean	
* kur	Kurdish	
* lao	Lao	
* lat	Latin	
* lav	Latvian	
* lit	Lithuanian	
* mal	Malayalam	
* mar	Marathi	
* mkd	Macedonian	
* mlt	Maltese	
* msa	Malay	
* mya	Burmese	
* nep	Nepali	
* nld	Dutch; Flemish	
* nor	Norwegian	
* ori	Oriya	
* pan	Panjabi; Punjabi	
* pol	Polish	
* por	Portuguese	
* pus	Pushto; Pashto	
* ron	Romanian; Moldavian; Moldovan	
* rus	Russian	
* san	Sanskrit	
* sin	Sinhala; Sinhalese	
* slk	Slovak	
* slv	Slovenian	
* spa	Spanish; Castilian	
* spa_old	Spanish; Castilian - Old	spa_
* sqi	Albanian	
* srp	Serbian	
* srp_latn	Serbian - Latin	srp_
* swa	Swahili	
* swe	Swedish	
* syr	Syriac	
* tam	Tamil	
* tel	Telugu	
* tgk	Tajik	
* tgl	Tagalog	
* tha	Thai	
* tir	Tigrinya	
* tur	Turkish	
* uig	Uighur; Uyghur	
* ukr	Ukrainian	
* urd	Urdu	
* uzb	Uzbek	
* uzb_cyrl	Uzbek - Cyrillic	uzb_
* vie	Vietnamese	
* yid	Yiddish