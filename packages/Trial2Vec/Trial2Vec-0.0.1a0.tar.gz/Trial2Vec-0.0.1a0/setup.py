import os
import setuptools

this_directory = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r") as f:
    long_description = f.read()

# read the contents of requirements.txt
with open(os.path.join(this_directory, 'requirements.txt'),
          encoding='utf-8') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name = 'Trial2Vec',
    version = '0.0.1a',
    author = 'Zifeng Wang',
    author_email = 'zifengw2@illinois.edu',
    description = 'Pretrained BERT models for encoding clinical trial documents to compact embeddings.',
    url = 'https://github.com/RyanWangZf/Trial2Vec',
    keywords=['clinical trial', 'machine learning', 'data mining', 'information retrieval'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(exclude=['test']),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)