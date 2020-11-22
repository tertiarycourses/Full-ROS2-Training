from setuptools import setup

package_name = 'my_robotics'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='alfred',
    maintainer_email='alfred@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'my_first_node = my_robotics.py_test:main',
        'my_second_node = my_robotics.py_test2:main',
        'my_third_node = my_robotics.py_test3:main',
        'my_fourth_node = my_robotics.py_test4:main',
        'my_fifth_node = my_robotics.py_test5:main',
        ],
    },
)
