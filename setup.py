from setuptools import setup, find_packages

setup(
    name="pynamer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "astunparse",
    ],
    entry_points={
        "console_scripts": [
            "pynamer = main:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
