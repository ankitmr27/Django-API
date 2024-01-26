from setuptools import setup, find_packages

setup(
    name='your_package_name',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'flask',
        'requests',
        'lxml',
        'nltk',
        'sequenceMatcher',
        'torch',
        'beautifulsoup4',
        'bert-extractive-summarizer',
    ],
    entry_points={
        
    },
    author='Ankit Maurya',
    author_email='am5099951@gmail.com',
    description='Get review and summary of any gadget',
    url='https://github.com/ankitmr27/Ankit_Maurya_Assignment',
)
