import setuptools

if __name__ == "__main__":
    with open("README.md") as f:
        long_description = f.read()

    setuptools.setup(
        name="nn-module",
        version="0.0.5",
        author="Nguyen Ngoc Khanh",
        author_email="khanh.nguyen.contact@gmail.com",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/khanh-nguyen-code/nn-module",
        packages=setuptools.find_packages(),
    )
