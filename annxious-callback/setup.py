import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="annxious-callback",
    version="0.1.2",
    author="Vicente Lizana",
    author_email="v.lizana.e@gmail.com",
    description="Keras callback to connect to ANNxious Telegram bot.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vlizanae/annxious-bot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)