from distutils.core import setup


setup(
    name = "geonode-user-messages",
    version = "0.1.1",
    author = "Eldarion",
    author_email = "development@eldarion.com",
    description = "Fork of user-messages: a reusable private user messages application for Django",
    long_description = open("README.rst").read(),
    license = "BSD",
    url = "http://github.com/GeoNode/user_messages",
    packages = [
        "user_messages",
        "user_messages.tests",
        "user_messages.templatetags",
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
