from setuptools import find_packages, setup

package_name = 'robot_v1_controller'

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
    maintainer='madeby',
    maintainer_email='ta.aydin01@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node_1 = robot_v1_controller.first_node:main",
            "circle_node_t = robot_v1_controller.draw_circle:main",
            # SAKIN - , - VIRGULU UNUTMA
            "pose_sub = robot_v1_controller.pose_sub:main",
            "turtle_controller = robot_v1_controller.Turtle_controller:main",
            "turtle_controller_srv = robot_v1_controller.turtle_controller_with_services:main"
        ],
    },
)
