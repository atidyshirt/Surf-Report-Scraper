""" surf report - setup.py"""
import setuptools

setuptools.setup(
    name="srs",
    author="Jordan Pyott",
    author_email="jordanpyott@gmail.com",
    description="Generate and change color-schemes on the fly",
    keywords="wal colorscheme terminal-emulators changing-colorschemes",
    license="MIT",
    url="",
    packages=["selenium"],
    entry_points={"console_scripts": ["srs=surf-report-scraper.__main__:main"]},
    python_requires=">=3.x",
    test_suite="tests"
)
