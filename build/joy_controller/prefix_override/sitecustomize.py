import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/keisoku/ros2_ws/src/joy_controller/install/joy_controller'
