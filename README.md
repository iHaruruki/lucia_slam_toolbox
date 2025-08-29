# lucia_slam_toolbox
### Node and Topic
![](rosgraph.png)
## Dependency
```shell
$ sudo apt install ros-humble-slam-toolbox
```
## Setup
```shell
$ cd ~/ros2_ws/src  #Go to ros workspace
$ git clone https://github.com/iHaruruki/lucia_slam_toolbox.git #clone this package
$ cd ~/ros2_ws
$ colcon build --symlink-install
$ source install/setup.bash
```
## Usage
### Launch Lucia's motor and LiDAR
```shell
ros2 launch lucia_controller bringup.launch.py
```
### Run slam_toolbox
```shell
ros2 launch lucia_slam_toolbox online_async_launch.py
```
### Run Teleportation Node
```shell
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
**When you move Lucia, the map will update.**
![making map](media/slam_toolbox.gif)
### Save map
```shell
# Once the entire map is complete, save it
ros2 run nav2_map_server map_saver_cli -f ~/map
```
## License
## Authors
## References
![SLAM (自己位置推定) のための Localization ~slam 設定調整~ (ROS2-Foxy)](https://nutritionfoodtech.com/2022/11/29/slam-%E8%87%AA%E5%B7%B1%E4%BD%8D%E7%BD%AE%E6%8E%A8%E5%AE%9A-%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE-localization-slam-%E8%A8%AD%E5%AE%9A%E8%AA%BF%E6%95%B4-ros2-foxy/)
