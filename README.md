# lucia_slam_toolbox
### Node and Topic
```mermaid
flowchart LR
    A(["/"]) ==> B["/"] ==> C(["/"])
```
## Dependency
```shell
$ sudo apt install ros-humble-slam-toolbox
$ sudo apt install ros-humble-gazebo-ros
$ sudo apt install ros-humble-twist-mux
$ sudo apt install ros-humble-ros2-control
$ sudo apt install ros-humble-ros2-controllers
$ sudo apt install ros-humble-gazebo-ros2-control
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
$ ros2 launch lucia_slam_toolbox
```
## License
## Authors
## References
