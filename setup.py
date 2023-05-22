import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="legoclient",  # Replace with your own username
  version="0.1.5",
  author="Luis Fernando do Nascimento",
  author_email="luisfn@gmail.com",
  description="Client for Lego Price API",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/brickminer/lego-price-api-client",
  download_url = 'https://github.com/brickminer/lego-price-api-client/archive/v0.1.5.tar.gz',
  keywords = ['Lego', 'Price', 'API', 'Client'],
  packages=setuptools.find_packages(),
  install_requires=[
    'requests==2.31.0',
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Crawlers',
    'License :: OSI Approved :: GNU License',
    'Programming Language :: Python :: 3.7',
  ],
  python_requires='>=3.7',
)