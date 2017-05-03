from setuptools import setup, find_packages


setup(name='persimmon',
      version='0.7',
      description='A visual dataflow language for sklearn',
      url='http://github.com/alvarber/Persimmon',
      author='Álvaro Bermejo',
      author_email='alvaro.garcia95@hotmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=['Kivy', 'scikit-learn', 'pandas', 'numpy',
                        'scipy', 'coloredlogs']
      zip_safe=False)
