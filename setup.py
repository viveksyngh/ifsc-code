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
                  'appnope (==0.1.0)',
                 'backports.shutil-get-terminal-size (==1.0.0)',
                 'BeautifulSoup (==3.2.1)',
                 'beautifulsoup4 (==4.5.1)',
                 'decorator (==4.0.10)',
                 'enum34 (==1.1.6)',
                 'ipython (==5.1.0)',
                 'ipython-genutils (==0.1.0)',
                 'pathlib2 (==2.1.0)',
                 'pexpect (==4.2.1)',
                 'pickleshare (==0.7.4)',
                 'prompt-toolkit (==1.0.9)',
                 'ptyprocess (==0.5.1)',
                 'Pygments (==2.1.3)',
                 'pyOpenSSL (==16.2.0)',
                 'requests (==2.12.4)',
                 'simplegeneric (==0.8.1)',
                 'six (==1.10.0)',
                 'traitlets (==4.3.1)'
                 'wcwidth (==0.1.7)',
                 'xlrd (==1.0.0)']
)
