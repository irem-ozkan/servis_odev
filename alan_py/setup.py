from setuptools import find_packages, setup

package_name = 'alan_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='irem',
    maintainer_email='irem5455367714@gmail.com',
    description='Dikdortgen alan hesaplama servisi',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'server = alan_py.server:main',
            'client = alan_py.client:main',
        ],
    },
)
