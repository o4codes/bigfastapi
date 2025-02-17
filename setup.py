import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bigfastapi",
    version="0.0.1",
    author="Nwokoye Chigozie Gregory",
    author_email="gregoflash05@gmail.com.com",
    description="An Authentication Package built on Fast API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rijentech/bigfastapi",
    packages=["bigfastapi"],
    install_requires=[
        "aioredis",
        "aiosmtplib>=1.1.6",
        "anyio>=3.3.4",
        "asgiref>=3.4.1",
        "async-timeout>=4.0.1",
        "bcrypt>=3.2.0",
        "blinker>=1.4",
        "certifi>=2021.10.8",
        "cffi>=1.15.0",
        "charset-normalizer>=2.0.8",
        "click>=8.0.3",
        "dnspython>=2.1.0",
        "email-validator>=1.1.3",
        "fastapi>=0.70.0",
        "fastapi-mail>=1.0.2",
        "fastapi-utils>=0.2.1",
        "greenlet>=1.1.2",
        "h11>=0.12.0",
        "idna>=3.3",
        "Jinja2>=3.0.3",
        "MarkupSafe>=2.0.1",
        "packaging>=21.3",
        "passlib>=1.7.4",
        "psycopg2-binary>=2.9.2",
        "pycparser>=2.21",
        "pydantic>=1.8.2",
        "PyJWT>=2.3.0",
        "pyparsing>=3.0.6",
        "python-decouple>=3.5",
        "python-dotenv>=0.19.2",
        "python-multipart>=0.0.5",
        "PyYAML>=6.0",
        "rfc3986>=1.5.0",
        "six>=1.16.0",
        "sniffio>=1.2.0",
        "sortedcontainers>=2.4.0",
        "SQLAlchemy>=1.4.27",
        "starlette==0.16.0",
        "typing-extensions>=4.0.0",
        "uvicorn>=0.15.0",
        "uvloop>=0.16.0",
        "watchgod>=0.7",
        "websockets>=10.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
