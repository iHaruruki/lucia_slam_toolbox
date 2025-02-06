#slam_toolboxの起動オプション設定
slam_params_file = LaunchConfiguration('slam_params_file')
declare_slam_params_file_cmd = DeclareLaunchArgument(
    'slam_params_file',
    default_value=os.path.join(get_package_share_directory("nav_dev"),
                               'params', 'slam_param.yaml'),
    description='Full path to the ROS2 parameters file to use for the slam_toolbox node')

#slam_toolboxの起動設定
start_async_slam_toolbox_node = Node(
    parameters=[
      slam_params_file,
      {'use_sim_time': use_sim_time}
    ],
    package='slam_toolbox',
    executable='async_slam_toolbox_node',
    name='slam_toolbox',
    output='screen')
