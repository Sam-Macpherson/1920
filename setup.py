from setuptools import setup

setup(name='1920',
      version='0.1',
      description="Game about twirling pizzas and selling alcohol.",
      url='https://github.com/Sam-Macpherson/1920',
      author='Sam Macpherson',
      author_email='sam.macpherson15@gmail.com',
      license='LGPL',
      packages=[
            'constants',
            'controls',
            'managers',
            'scenes',
            'sprites',
            'utilities'
      ],
      install_requires=[
          'pygame', 'cx-Freeze',
      ],
      zip_safe=False)
