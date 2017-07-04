from setuptools import setup, find_packages


setup(name='persimmon',
      description='A visual dataflow language for sklearn',
      author='Álvaro Bermejo',
      author_email='alvaro.garcia95@hotmail.com',
      version='0.9.1-2',
      url='http://github.com/AlvarBer/Persimmon',
      download_url='https://github.com/AlvarBer/Persimmon/archive/v0.9.1.tar.gz',
      license='MIT',
      packages=find_packages(),
      package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.kv', '*.png', '*.ini'],
      },
      include_package_data=True,
      python_requires='>=3.5',
      setup_requires=['Cython'],
      install_requires=['Cython', 'Kivy', 'scipy', 'scikit-learn', 'pandas',
                        'fuzzywuzzy', 'pymitter'],
      zip_safe=False,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6'],
      entry_points={
          'console_scripts': [
              'persimmon = persimmon.__main__:main'
          ]
      })
