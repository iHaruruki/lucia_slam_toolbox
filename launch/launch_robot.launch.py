import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command
from launch_ros.actions import RegisterEventHandler
from launch.event_handlers import OnProcessExit

from launch_ros.actions import Node

def generate_launch_description():

    # Include the robot state publisher launch file, provided by our own package. Force sim time to be enabled
    # !!! MAKE SURE YOU SET THE PACKAGE NAME CORRECTLY !!!

    package_name='lucia_slam_toolbox'

    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'true', 'use_ros2_control': 'true'}.items()
    )

    # この行では、robot_state_publisher ノードから robot_description パラメータ（通常は URDF の XML 文字列）を取得するために、ros2 param get コマンドを実行しています。→ 得られた値は、後で controller_manager に渡すためのパラメータとして利用されます。
    robot_description = Command(['ros2 param get --hide-type /robot_state_publisher robot_description'])

    # この行では、controller_manager パッケージの my_controllers.yaml ファイルのパスを取得しています
    controller_params_file = os.path.join(get_package_share_directory(package_name),'config','my_controllers.yaml')

    # controller_manager ノード→ controller_manager パッケージの ros2_control_node を起動します。→ パラメータとして、先ほどの robot_description（コマンドで取得した URDF 情報）と、コントローラー設定の YAML ファイルを渡します。
    controller_manger = Node(
        package='controller_manager',
        executable='ros2_control_node',
        parameters=[{'robot_description': robot_description},
                    controller_params_file]
    )

    # TimerAction を利用して、controller_manager の起動を 3 秒遅らせています。
    delayed_controller_manager = TimerAction(period=3.0, actions=[controller_manger])

    # Launch them all
    return LaunchDescription([
        rsp,
        delayed_controller_manager
    ])
