import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.conditions import UnlessCondition
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from nav2_common.launch import HasNodeParams


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')
    params_file = LaunchConfiguration('params_file')
    default_params_file = os.path.join(get_package_share_directory("lucia_slam_toolbox"), 'config', 'mapper_params_online_async.yaml')
    rviz_config_dir = os.path.join(get_package_share_directory('lucia_cartographer'), 'rviz', 'lucia_cartographer.rviz')

    declare_use_sim_time_argument = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false',
        description='Use simulation (Gazebo) clock if true'
    )
    declare_params_file_cmd = DeclareLaunchArgument(
        'params_file',
        default_value=default_params_file,
        description='Full path to the ROS2 parameters file to use for the slam_toolbox node')

    has_node_params = HasNodeParams(source_file=params_file,
                                      node_name='slam_toolbox',)

    actual_params_file = PythonExpression([
        '"', params_file, '" if ', has_node_params, ' else "', default_params_file, '"'
    ])

    log_params_file = LogInfo(msg=['provid params_file:', params_file,
                                   'does not contain slam_toolbox paramerters. Using default:',
                                   default_params_file],
                              condition=UnlessCondition(has_node_params))

    start_async_slam_toolbox_node = Node(
        parameters=[
            actual_params_file,
            {'use_sim_time': use_sim_time}
        ],
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        output='screen')

    rviz2 = Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_dir],
            parameters=[{'use_sim_time': use_sim_time}],
            output='screen')

    ld = LaunchDescription()

    ld.add_action(declare_use_sim_time_argument)
    ld.add_action(declare_params_file_cmd)
    ld.add_action(log_params_file)
    ld.add_action(start_async_slam_toolbox_node)
    ld.add_action(rviz2)

    return ld
