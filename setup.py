from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='linkedin-jobs-pyscraper',
    version='1.0.0',
    author='Shahrukh Khan',
    author_email='sk28671@gmail.com',
    description='Scrape public jobs postings from LinkedIn in native python without selenium or any headless browser.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/shahrukhx01/linkedin-jobs-pyscraper',
    packages=[
        'linkedin_jobs_pyscraper',
        'linkedin_jobs_pyscraper.extract',
        'linkedin_jobs_pyscraper.search',
        'linkedin_jobs_pyscraper.models',
        'linkedin_jobs_pyscraper.utils',
        'linkedin_jobs_pyscraper.models.extract',
        'linkedin_jobs_pyscraper.models.job',
        'linkedin_jobs_pyscraper.models.search',
        'linkedin_jobs_pyscraper.models.filters',
    ],
    install_requires=[
        'beautifulsoup4',
        'bs4',
        'certifi',
        'pandas',
        'requests',
        'urllib3',
        'python-dateutil',
        'pydantic'
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