from setuptools import setup, find_packages

setup(
    name="satosacontrib.perun",
    python_requires=">=3.9",
    url="https://github.com/CESNET/satosacontrib.perun.git",
    description="Module with satosa micro_services",
    packages=find_packages(),
    install_requires=[
        "setuptools",
        "SATOSA==8.1.1",
        "pysaml2>=7.1.2,<8",
        "requests>=2.28.1,<3",
        "perun.connector>=3.1.0,<4",
        "pycurl>=7.45.1,<8",
        "PyYAML>=6.0,<7",
        "SQLAlchemy>=1.4.39,<2",
        "jwcrypto>=1.3.1,<2",
        "natsort~=8.2.0",
    ],
)
