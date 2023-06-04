from setuptools import setup

setup(
    name='pyfinviz',
    packages=['pyfinviz'],
    version='0.12',
    license='apache-2.0',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Scrape data from finviz.com',
    author='Oscar R. Torres',
    author_email='oscar0812torres@gmail.com',
    url='https://github.com/oscar0812/pyfinviz',
    download_url='https://github.com/oscar0812/pyfinviz/archive/refs/tags/v_12.tar.gz',
    keywords=['FINVIZ', 'STOCKS', 'SCRAPER', 'BITTLE'],  # Keywords that define your package best
    install_requires=[
        'validators',
        'beautifulsoup4',
        'free-proxy',
        'pandas',
        'numpy',
        'lxml',
        'requests'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which python versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
