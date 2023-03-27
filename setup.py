from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='gclfs',
    version='0.1.1',
    description='Git LFS for large files that need cloud storage.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/mjlabe/gclfs',
    author='Marc LaBelle',
    keywords=['GIT', 'LFS', 'CLOUD', 'STORAGE', 'AWS', 'S3', ],
    packages=find_packages(),
    install_requires=[
        'boto3 >= 1, <= 2',
        'click >= 8, <= 9'
    ],
    python_requires='>=3.6, <4',
    entry_points={
        'console_scripts': [
            'gcl = src.gclfs.main:cli',
            'gclfs = src.gclfs.main:cli',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9'
    ],
)
