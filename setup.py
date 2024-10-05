import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quick-i18n",  # Replace with your own package name
    version="0.1.0",
    author="Iu Bell",
    author_email="uran.ds@gmail.com",
    description="A quick and easy internationalization library for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/urands/quick-i18n",
    packages=setuptools.find_packages(),
    install_requires=[
        "python-slugify>=4.0.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)