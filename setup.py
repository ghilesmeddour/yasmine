import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yasmine",
    version="1.0.0",
    author="Ghiles Meddour",
    author_email="ghiles.meddour@munic.io",
    description="POÈME POUR YASMINE",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ghilesmeddour/yasmine",
    project_urls={
        "Bug Tracker": "https://github.com/ghilesmeddour/yasmine/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    package_data={'yasmine': ['*.mp3', 'texte/*']},
    python_requires=">=3.8",
    install_requires=[
        "pygame",
    ],
)
