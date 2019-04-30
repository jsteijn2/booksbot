from setuptools import setup, find_packages

setup(
    name='books',
    version='1.0',
    packages=find_packages(),
    package_data={
        'books': ['resources/urls.txt']
    },
    entry_points={
        'scrapy': ['settings = books.settings']
    },
    zip_safe=False,
)