from setuptools import setup, find_packages

setup(
    name="predx",
    version="0.1.0",
    packages=find_packages(include=["predx", "predx.*"]),  
    package_dir={"predx": "predx"}, 
    install_requires=["requests"],
)
