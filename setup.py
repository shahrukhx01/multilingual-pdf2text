from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='multilingual-pdf2text',
    version='1.1.0',
    author='Shahrukh Khan',
    author_email='sk28671@gmail.com',
    description='A python library for extracting text from PDFs without losing the formatting of the PDF content.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/shahrukhx01/multilingual-pdf2text',
    packages=[
        'multilingual_pdf2text',
        'multilingual_pdf2text.doc2img',
        'multilingual_pdf2text.models',
        'multilingual_pdf2text.ocr',
        'multilingual_pdf2text.models.document_model'
    ],
    install_requires=[
        'pydantic',
        'pytesseract',
        'pdf2image',
        'pillow'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
