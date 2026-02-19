from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="devdash",
    version="1.0.0",
    author="Horace",
    author_email="horace@example.com",
    description="Ultimate local-first developer dashboard",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HoraceDong31415-bit/devdash",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "devdash=devdash:main",
        ],
    },
    keywords="cli developer-tools productivity clipboard notes snippets time-tracking",
    project_urls={
        "Bug Reports": "https://github.com/HoraceDong31415-bit/devdash/issues",
        "Source": "https://github.com/HoraceDong31415-bit/devdash",
    },
)
