# lucia_slam_toolbox
[![ROS 2 Distro - Humble](https://img.shields.io/badge/ros2-Humble-blue)](https://docs.ros.org/en/humble/)
[![ROS2 Distro - Jazzy](https://img.shields.io/badge/ros2-Jazzy-blue)](https://docs.ros.org/en/jazzy/)

## 🚀 Overview

## 🛠️ Setup
```bash
sudo apt install ros-humble-slam-toolbox
```
```bash
cd ~/ros2_ws/src  #Go to ros workspace
git clone https://github.com/iHaruruki/lucia_slam_toolbox.git #clone this package
cd ~/ros2_ws
colcon build --symlink-install --packages-select lucia_slam_toolbox
source install/setup.bash
```
## 🎮 Usage
### Launch Lucia's motor and LiDAR
```bash
ros2 launch lucia_controller bringup.launch.py
```
### Run slam_toolbox
```bash
ros2 launch lucia_slam_toolbox online_async_launch.py
```
### Run Teleportation Node
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
**When you move Lucia, the map will update.**
![making map](media/slam_toolbox.gif)
### Save map
```bash
# Once the entire map is complete, save it
ros2 run nav2_map_server map_saver_cli -f ~/map
```
## 📜 License
## 👤 Authors
- **[iHaruruki](https://github.com/iHaruruki)** — Main author & maintainer
## 📚 References
