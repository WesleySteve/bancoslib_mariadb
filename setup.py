from setuptools import find_packages, setup


def ler(filename):
    return [req.strip() for req in open(filename).readlines()]


setup(
    name="bancoslib_mariadb",
    version="0.1.0",
    author="Wesley Steve",
    author_email="wesley.silva23@hotmail.com",
    maintainer="Wesley Steve",
    maintainer_email="wesley.silva23@hotmail.com",
    license="GPL",
    description="Biblioteca de suporte para projetos que utilizaram banco de dados",
    packages=find_packages(),
    include_package_data=True,
    install_requires=ler("requirements.txt"),
    
)
