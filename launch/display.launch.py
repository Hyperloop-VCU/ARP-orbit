from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.substitutions import FindPackageShare

# This simple launch file starts one orbit node and rviz.

def generate_launch_description():

    # Declare the orbit speed launch argument
    revs_per_sec_arg = DeclareLaunchArgument(
        'revs_per_sec',
        default_value='0.5',
        description='Orbit speed in revolutions per second',
    )

    # Get rviz configuration file 
    rviz_config_file = PathJoinSubstitution([FindPackageShare('ARP-orbit'), "rviz_config.rviz"])

    # Start orbit node
    orbit_node = Node(
        package='ARP-orbit',
        executable='orbit_node',
        parameters=[{'revs_per_sec': ParameterValue(LaunchConfiguration('revs_per_sec'), value_type=float)}],
    )

    # Start rviz and pass in the config file
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        arguments=["-d", rviz_config_file, "--ros-args", "--log-level", "warn"],
    )
    return LaunchDescription([
        revs_per_sec_arg,
        orbit_node,
        rviz
    ])
