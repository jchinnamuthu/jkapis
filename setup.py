from setuptools import setup, find_packages

setup(
    name="jkapis",
    version="0.0.2",
    packages=find_packages(),
    install_requires=[],  # Add dependencies here
    author="Jeyakumar Chinnamuthu",
    author_email="jchinnamuthu@gmail.com",
    description="A sample Python package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jchinnamuthu/jkapis",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)