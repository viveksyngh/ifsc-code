from distutils.core import setup

setup(
      name = 'ifsccode',
      packages = ['ifsccode'], # this must be the same as the name above
      version = '0.1',
      description = 'Command line tool for downloading ifsc code',
      author = 'Vivek Singh',
      author_email = 'vivekkmr45@yahoo.in',
      url = 'https://github.com/viveksyngh/ifsc-code',
      download_url='https://github.com/viveksyngh/ifsc-code/archive/0.1.tar.gz',
      keywords = ['Bank IFSC code', 'IFSC Code', 'IFSC'],
      classifiers = [],
      platforms = ['Any'],
      provides = ['ifsc_code'],
      requires = ["BeautifulSoup (==3.2.1)", 
                  "beautifulsoup4 (==4.5.1)",
                  "requests (==2.12.4)",
                  "xlrd (==1.0.0)"]
)
