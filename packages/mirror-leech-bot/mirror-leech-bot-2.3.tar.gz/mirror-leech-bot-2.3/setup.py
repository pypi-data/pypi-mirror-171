from setuptools import setup, find_packages
import pathlib

CWD = pathlib.Path(__file__).parent

README = (CWD / "README.md").read_text()

setup(
    name='mirror-leech-bot',
    version='2.3',
    packages=find_packages(),
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/gautam1834/mirror-leech-telegram-bot',
    license='GPL3.0',
    author='https://github.com/gautam1834',
    author_email='gautam@gautam1834.gq',
    include_package_data=True,
    description='Mirror-Leech Telegram Bot',
    platforms="any",
    install_requires=[
        "anytree",
        "appdirs",
        "aria2p",
        "asyncio",
        "attrdict",
        "beautifulsoup4",
        "bencoding",
        "cloudscraper",
        "cfscrape",
        "dnspython"
        "flask",
        "google-api-python-client",
        "google-auth-httplib2",
        "google-auth-oauthlib",
        "gunicorn",
        "heroku3",
        "lk21",
        "lxml",
        "megasdkrestclient",
        "pillow",
        "psutil",
        "psycopg2-binary",
        "pybase64",
        "pymongo",
        "pyrogram",
        "python-dotenv",
        "python-magic",
        "python-telegram-bot",
        "qbittorrent-api",
        "requests",
        "speedtest-cli",
        "telegraph",
        "tenacity",
        "tgCrypto",
        "urllib3",
        "xattr",
        "yt-dlp"     
    ],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 5 - Production/Stable"
    ],
    python_requires=">=3.10",
)
