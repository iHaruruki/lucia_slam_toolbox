cmake_minimum_required(VERSION 3.5)
project(lucia_slam_toolbox)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

# launch/ および config/ ディレクトリ内のファイルをインストール
install(
  DIRECTORY launch params
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
