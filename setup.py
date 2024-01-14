from setuptools import setup, find_packages
import os

# Read the contents of your README file
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

metadata = {
    'name': 'your_package_name',
    'version': '0.1',
    'description': 'A short description of your package',
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',
    'author': 'Your Name',
    'author_email': 'your_email@example.com',
    'url': 'https://github.com/your_username/your_package_name',
    'packages': find_packages(),
    'classifiers': [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    'install_requires': [
        # List your package dependencies here
    ],
}

setup(**metadata)
