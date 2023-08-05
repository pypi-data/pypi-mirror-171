import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdk-serverless-clamscan",
    "version": "2.4.46",
    "description": "Serverless architecture to virus scan objects in Amazon S3.",
    "license": "Apache-2.0",
    "url": "https://github.com/awslabs/cdk-serverless-clamscan",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services<donti@amazon.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/awslabs/cdk-serverless-clamscan"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_serverless_clamscan",
        "cdk_serverless_clamscan._jsii"
    ],
    "package_data": {
        "cdk_serverless_clamscan._jsii": [
            "cdk-serverless-clamscan@2.4.46.jsii.tgz"
        ],
        "cdk_serverless_clamscan": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk-lib>=2.11.0, <3.0.0",
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
    "scripts": [
        "src/cdk_serverless_clamscan/_jsii/bin/0"
    ]
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
