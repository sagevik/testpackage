import setuptools

# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="testpackage",  # should match the package folder
    packages=["testpackage"],  # should match the package folder
    version="0.0.3",  # important for updates
    license="MIT",  # should match your chosen license
    description="Testing installation of Package",
    long_description=long_description,  # loads your README.md
    long_description_content_type="text/markdown",  # README.md is of type 'markdown'
    author="Rune",
    author_email="rsagevik@gmail.com",
    url="https://github.com/sagevik/testpackage",
    project_urls={"Bug Tracker": "https://github.com/sagevik/testpackage/issues"},  # Optional
    install_requires=[],  # list all packages that your package uses
    keywords=["pypi", "testpackage", "tutorial"],  # descriptive meta-data
    classifiers=[  # https://pypi.org/classifiers
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Documentation",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
