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
```shell
$ ros2 run lucia_controller lucia_controller_node
$ ros2 launch urg_node2 urg_node2.launch.py
$ ros2 launch lucia_description robot.launch.py
$ ros2 launch lucia_slam_toolbox online_async_launch.py
```
## License
## Authors
## References
