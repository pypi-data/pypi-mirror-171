from setuptools import setup
# EJECUTA ESTO CON: py -m build
# and upload with:  twine upload dist/*


from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()



setup(
    name = 'ConvTool',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages = ['ConvTool'],
    version = '0.2.2.3',
    license = 'MIT',
    description = 'Convert your video files, or an ENTIRE folder with video files to a different format! 🥵',
    author = 'ElHaban3ro',
    author_email = 'habanferd@gmail.com',
    url = 'https://github.com/ElHaban3ro/ConvTool',
    keywords = 'python converter video-processing video-converter image-processing image-converter',
    classifiers = [
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ]
)