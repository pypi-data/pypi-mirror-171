import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdk-budget-notifier",
    "version": "0.3.22",
    "description": "A simple AWS budget notifier.",
    "license": "Apache-2.0",
    "url": "https://github.com/stefanfreitag/cdk-budget-notifier.git",
    "long_description_content_type": "text/markdown",
    "author": "Stefan Freitag<stefan.freitag@udo.edu>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/stefanfreitag/cdk-budget-notifier.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_budget_notifier",
        "cdk_budget_notifier._jsii"
    ],
    "package_data": {
        "cdk_budget_notifier._jsii": [
            "aws_budget_notifier@0.3.22.jsii.tgz"
        ],
        "cdk_budget_notifier": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk-lib>=2.42.0, <3.0.0",
        "constructs>=10.0.5, <11.0.0",
        "jsii>=1.69.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
