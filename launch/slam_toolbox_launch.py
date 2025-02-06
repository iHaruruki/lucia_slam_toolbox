#!/usr/bin/env python3
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # パッケージ内のconfigディレクトリにある設定ファイルのパスを取得
    config_file = os.path.join(
        get_package_share_directory('lucia_slam_toolbox'),
        'config',
        'mapper_params_online_sync.yaml'
    )

    slam_toolbox_node = Node(
        package='slam_toolbox',
        executable='sync_slam_toolbox_node',
        name='slam_toolbox',
        output='screen',
        parameters=[config_file]
    )

    return LaunchDescription([slam_toolbox_node])
