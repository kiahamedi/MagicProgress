from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.3'
DESCRIPTION = 'Python Magic Progressbar'
LONG_DESCRIPTION = 'A package that allows to implement and draw various examples of progress bar.'

PROJECT_URLS = {
  'Homepage': 'https://github.com/kiahamedi/MagicProgress',
  'Website': 'https://kiahamedi.ir/magic-progress/'
}

# Setting up
setup(
    name="MagicProgress",
    version=VERSION,
    author="Kia Hamedi",
    author_email="<kia.arta9793@gmail.com>",
    description=DESCRIPTION,
    project_urls=PROJECT_URLS,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'progress', 'progressbar', 'magic progress', 'kia hamedi'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
