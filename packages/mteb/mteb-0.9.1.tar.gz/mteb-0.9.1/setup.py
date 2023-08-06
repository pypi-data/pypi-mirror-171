from setuptools import find_packages, setup


with open("README.md", mode="r", encoding="utf-8") as readme_file:
    readme = readme_file.read()


extras = {}
extras["beir"] = ["beir"]


setup(
    name="mteb",
    version="0.9.1",
    description="Massive Text Embedding Benchmark",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords="deep learning, text embeddings, benchmark",
    license="Apache",
    author="MTEB Contributors (https://github.com/embeddings-benchmark/mteb/graphs/contributors)",
    author_email="niklas@huggingface.co, nouamane@huggingface.co, info@nils-reimers.de",
    url="https://github.com/embeddings-benchmark/mteb",
    project_urls={
        "Huggingface Organization": "https://huggingface.co/mteb",
        "Source Code": "https://github.com/embeddings-benchmark/mteb",
    },
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "mteb=mteb.cmd:main",
        ]
    },
    python_requires=">=3.7.0",
    install_requires=[
        "datasets>=2.2.0",
        "jsonlines",
        "numpy",
        "requests>=2.26.0",
        "scikit_learn>=1.0.2",
        "scipy",
        "sentence_transformers>=2.2.0",
        "torch",
        "tqdm",
        "rich",
    ],
    extras_require=extras,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)
