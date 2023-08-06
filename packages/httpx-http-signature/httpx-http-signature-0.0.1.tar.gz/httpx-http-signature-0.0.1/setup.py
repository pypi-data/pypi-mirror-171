#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="httpx-http-signature",
    url="https://github.com/pyauth/httpx-http-signature",
    license="Apache Software License",
    author="Andrey Kislyuk",
    author_email="kislyuk@gmail.com",
    description="A httpx auth module for HTTP Message Signatures",
    long_description=open("README.rst").read(),
    use_scm_version={
        "write_to": "httpx_http_signature/version.py",
    },
    setup_requires=["setuptools_scm >= 3.4.3"],
    install_requires=["http-message-signatures >= 0.4.3", "http-sfv >= 0.9.3", "httpx"],
    extras_require={
        "tests": [
            "flake8",
            "coverage",
            "build",
            "wheel",
            "mypy",
        ]
    },
    packages=find_packages(exclude=["test"]),
    include_package_data=True,
    package_data={
        "http_message_signatures": ["py.typed"],
    },
    platforms=["MacOS X", "Posix"],
    test_suite="test",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
