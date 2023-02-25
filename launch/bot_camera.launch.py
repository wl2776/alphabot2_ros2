import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
   config = os.path.join(
      get_package_share_directory('alphabot2_ros2'),
      'camera.yaml'
      )

   return LaunchDescription([
       Node(
           package='camera_ros',
           executable='camera_node',
           namespace='alphabot2',
           name='raspicam',
           parameters=[config]
           ),
       Node(
           package='alphabot2_ros2',
           executable='alphabot2',
           namespace='alphabot2',
           name='bot'
           )
       ])

