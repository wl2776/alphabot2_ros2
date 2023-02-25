import os
from glob import glob
from setuptools import setup

package_name = 'alphabot2_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*') + 
                                              glob('config/*.yaml'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='wl2776',
    maintainer_email='wl2776@gmail.com',
    description='Alphabot2 ROS2 node',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['alphabot2 = alphabot2_ros2.alphabot2_node:main',],
    },
)
