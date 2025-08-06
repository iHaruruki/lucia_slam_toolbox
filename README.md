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
