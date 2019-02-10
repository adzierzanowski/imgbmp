from setuptools import setup

setup(
    name='imgbmp',
    version='0.1',
    description='Convert images to 8-byte bitmaps compatible \
       with popular LCD/LED display controllers.',
    url='https://github.com/adzierzanowski/imgbmp',
    author='Aleksander Dzierżanowski',
    author_email='a.dzierzanowski1@gmail.com',
    license='MIT',
    packages=['imgbmp'],
    include_package_data=True,
    install_requires=['pillow'],
    scripts=['bin/imgbmp'],
    zip_safe=False
)
