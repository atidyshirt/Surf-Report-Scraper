""" surf report - setup.py"""
import setuptools

setuptools.setup(
    name="Surf Report Scraper",
    author="Jordan Pyott",
    author_email="jordanpyott@gmail.com",
    description="To generate the Surf report of a local beach",
    keywords="Surf Report Web Scraping Amazon Echo",
    license="",
    url="https://github.com/atidyshirt/Surf-Report-Scraper",
    packages=["selenium"],
    entry_points={"console_scripts": ["srs=surf-report-scraper.__main__:main"]},
    python_requires=">=3.x",
    test_suite="tests"
)
