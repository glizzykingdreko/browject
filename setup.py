from setuptools import setup, find_packages

setup(
    name='browject',
    version='0.1.3',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        line.strip() for line in open("requirements.txt", "r").readlines()
    ],
    author='glizzykingdreko',
    author_email='glizzykingdreko@protonmail.com',
    description='A Python library to seamlessly access and emulate browser attributes. Ideal for reverse engineering antibots. Powered by TakionAPI for up-to-date browser data.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/glizzykingdreko/browject',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)