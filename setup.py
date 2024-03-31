from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


REPO_NAME = "Book-Recommendation-System"
AUTHOR_NAME = "Shimul-Baidya"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy', 'scikit-learn']


setup(
    name=SRC_REPO,
    version="1.0.0",
    author=AUTHOR_NAME,
    description="This is a small simple Book Recommendation System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    author_email="shimul.cse31@gmail.com",
    packages=[SRC_REPO],
    python_requires=">=3.10",
    install_requires=LIST_OF_REQUIREMENTS
)

