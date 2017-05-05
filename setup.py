from setuptools import setup, find_packages


setup(name='persimmon',
      description='A visual dataflow language for sklearn',
      author='Álvaro Bermejo',
      author_email='alvaro.garcia95@hotmail.com',
      version='0.8',
      url='http://github.com/alvarber/Persimmon',
      download_url='https://github.com/AlvarBer/Persimmon/archive/v0.7-beta.tar.gz',
      license='MIT',
      packages=find_packages(),
      install_requires=['Kivy', 'scikit-learn', 'pandas', 'numpy',
                        'scipy', 'coloredlogs']
      zip_safe=False)
