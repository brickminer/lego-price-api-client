from distutils.core import setup
setup(
  name = 'client',
  packages = ['client'],
  version = '0.1.1',
  license='GNU',
  description = 'Client for Lego Price API',
  author = 'Luis Fernando do Nascimento',
  author_email = 'luisfn@gmail.com',
  url = 'https://github.com/luisfn/lego-price-api-client',
  download_url = 'https://github.com/luisfn/lego-price-api-client/archive/v0.1.1.tar.gz',
  keywords = ['Lego', 'API', 'Client'],
  install_requires=[
          'requests',
          'json',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)