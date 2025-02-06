#!/usr/bin/env python3
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share = get_package_share_directory('lucia_slam_toolbox')
    # slam_toolbox のパラメータファイルと RViz2 の設定ファイルのパスを取得
    slam_config_file = os.path.join(pkg_share, 'config', 'mapper_params_online_sync.yaml')
    rviz_config_file = os.path.join(pkg_share, 'config', 'rviz2_config.rviz')

    # slam_toolbox ノードの起動設定
    slam_toolbox_node = Node(
        package='slam_toolbox',
        executable='sync_slam_toolbox_node',  # 同期モードノード（環境に合わせて非同期版も検討）
        name='slam_toolbox',
        output='screen',
        parameters=[slam_config_file]
    )

    # RViz2 の起動（コマンド実行）
    rviz2_process = ExecuteProcess(
        cmd=['rviz2', '-d', rviz_config_file],
        output='screen'
    )

    return LaunchDescription([
        slam_toolbox_node,
        rviz2_process
    ])
