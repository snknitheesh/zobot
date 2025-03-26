from launch import LaunchDescription
from launch.actions import ExecuteProcess


def generate_launch_description():
    return LaunchDescription(
        [ExecuteProcess(cmd=["ros2", "run", "zobot", "run_sim"], output="screen")]
    )
