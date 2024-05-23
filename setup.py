# setup.py

from setuptools import setup, find_packages

setup(
    name="curelyai",
    version="0.1.0",
    author="Curely Ai",
    author_email="curelyai@gmail.com",
    description="A Python client for Curely AI API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/curelyai/curelyai_python_package",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
