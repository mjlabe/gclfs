from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='gclfs',
    version='0.1.0',
    description='Git LFS for large files that need cloud storage.',
    long_description=readme(),
    license='MIT',
    url='https://github.com/mjlabe/gclfs',
    author='Marc LaBelle',
    keywords=['GIT', 'LFS', 'CLOUD', 'STORAGE', 'AWS', 'S3', ],
    py_modules=['gclfs'],
    install_requires=[
        'boto3 >= 1, <= 2',
        'click >= 8, <= 9'
    ],
    python_requires='>=3.6, <4',
    entry_points={
        'console_scripts': [
            'gcl = src.main:cli',
            'gclfs = src.main:cli',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9'
    ],
)
