from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="solaira",
    version="0.1.0",
    author="Solaira",
    author_email="admin@solaira.dev",
    description="AI-Powered Intelligence for the Solana Ecosystem and Beyond",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/solairaai/solaira",
    packages=find_packages(),
    install_requires=[
        "requests>=2.26.0",
        "aiohttp>=3.8.0",
        "pydantic>=1.10.0",
        "solana>=0.25.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)