#!/usr/bin/env python

from setuptools import setup

with open("README.md", "rt") as fh:
    long_description = fh.read()

dependencies = [
    "clvm>=0.9.2",
    "chik_clvm_tools_rs>=0.1.25"
]

dev_dependencies = [
    "pytest",
]

setup(
    name="chik_clvm_tools",
    packages=["ir", "chik_clvm_tools", "chik_clvm_tools.setuptools", "stages", "stages.stage_2",],
    author="Chik Network, Inc.",
    entry_points={
        "console_scripts": [
            "read_ir = chik_clvm_tools.cmds:read_ir",
            "opc = chik_clvm_tools.cmds:opc",
            "opd = chik_clvm_tools.cmds:opd",
            "run = chik_clvm_tools.cmds:run",
            "brun = chik_clvm_tools.cmds:brun",
        ],
    },
    package_data={
        "": ["py.typed"],
    },
    author_email="kiss@chiknetwork.com",
    install_requires=dependencies,
    url="https://github.com/Chik-Network",
    license="https://opensource.org/licenses/Apache-2.0",
    description="CLVM compiler.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Security :: Cryptography",
    ],
    extras_require=dict(dev=dev_dependencies,),
    project_urls={
        "Bug Reports": "https://github.com/Chik-Network/chik_clvm_tools",
        "Source": "https://github.com/Chik-Network/chik_clvm_tools",
    },
)
