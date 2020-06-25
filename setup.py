import os
from setuptools import find_packages, setup

setup(
    name="weather",
    version="1.0",
    packages=find_packages(),
    license="Private",
    description="Weather Desktop wallpaper",
    author="sukhbinder",
    author_email="sukh2010@yahoo.com",
    entry_points={
        'console_scripts': ['wallpaper = weather.weather_desktop:main',],
    }
)
