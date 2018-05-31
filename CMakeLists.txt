cmake_minimum_required(VERSION 2.8.3)
project(asv_navigation)

find_package(catkin REQUIRED COMPONENTS
  move_base
  asv_controls
  asv_localization
  asv_description
  teb_local_planner
)

catkin_package(
  CATKIN_DEPENDS move_base teb_local_planner
)