from setuptools import setup
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()


setup(
    name="reader-miha-193",
    version="2.4.0",
    description="Read the latest news for Realpython",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Miha",
    author_email="neki@neki.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    include_package_data=True,
    packages=["reader"],
    install_requires=["feedparser", "html2text"],
    entry_points={
        "console_scripts": [
            "realpython=reader.__main__:main",
        ]
    },
)
