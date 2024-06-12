# imbuere_scraper_package/setup.py
from setuptools import setup, find_packages

setup(
    name='imbuere_scraper_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'scrape=imbuere_scraper.scraper:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A package to fetch and save URL content using Crawlbase API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/imbuere_scraper_package',  # Replace with your actual URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
