from setuptools import setup, find_packages


setup(name='persimmon',
      description='A visual dataflow language for sklearn',
      author='Álvaro Bermejo',
      author_email='alvaro.garcia95@hotmail.com',
      version='0.8.1',
      url='http://github.com/alvarber/Persimmon',
      download_url='https://github.com/AlvarBer/Persimmon/archive/v0.8-beta.tar.gz',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      python_requires='>=3.5',
      setup_requires=['Cython'],
      install_requires=['Cython', 'Kivy', 'scipy', 'scikit-learn', 'pandas',
                        'coloredlogs'],
      zip_safe=False)
