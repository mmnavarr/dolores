import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="dolores",
  version="0.2.0",
  author="Dolores Abernathy",
  author_email="malcolmcyber@gmail.com",
  description="Dolores is an python package that provides direct access to GPT-3 via dolores class instance. Instantiate dolores with your API key to create dolores with the proper configurations required to make requests to the OpenAI API.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/mmnavarr/dolores",
  download_url="https://pypi.org/project/dolores/",
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires=">=3.6",
)