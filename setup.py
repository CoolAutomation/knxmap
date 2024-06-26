from setuptools import setup

install_require = []

setup(
    name='KNXmap',
    version='0.10.0',
    packages=['knxmap',
              'knxmap.bus',
              'knxmap.usb',
              'knxmap.data',
              'knxmap.messages'],
    entry_points={
        'console_scripts': ['knxmap=knxmap.main:main']},
    install_requires=install_require,
    url='https://github.com/takeshixx/knxmap',
    license='GNU GPLv3',
    author='takeshix',
    author_email='knxmap@adversec.com',
    description='KNXnet/IP library and utility',
    python_requires='>=3.4',
)
