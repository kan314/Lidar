from setuptools import setup

package_name = 'my_python_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=scan,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kan314',
    maintainer_email='kangood23626@gmail.com,
    description='My ROS 2 Python package',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'my_node = my_python_pkg.my_node:main',
        ],
    },
)