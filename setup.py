from setuptools import setup

setup(
    name='gclfs',
    version='0.0.1',
    py_modules=['gclfs'],
    install_requires=[
        'boto3 >= 1, <= 2',
        'click >= 8, <= 9'
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'gclfs = gclfs:gclfs',
        ],
    },
)
