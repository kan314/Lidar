import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import numpy as np

class Lidar8Direction(Node):
    def __init__(self):
        super().__init__('lidar_8_direction')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)
        self.sector_angles = 8  # 8 sectors
        self.sector_size = 360 / self.sector_angles

    def scan_callback(self, msg):
        ranges = np.array(msg.ranges)
        angle_min = msg.angle_min  # in radians
        angle_increment = msg.angle_increment  # in radians
        num_points = len(ranges)

        # Calculate angle for each point in degrees
        angles = np.degrees(angle_min + np.arange(num_points) * angle_increment) % 360

        # Divide points into 8 sectors
        sector_data = [[] for _ in range(self.sector_angles)]

        for i, angle in enumerate(angles):
            sector_idx = int(angle // self.sector_size)
            if np.isfinite(ranges[i]):
                sector_data[sector_idx].append(ranges[i])

        # Compute minimum distance in each sector
        min_distances = [min(sector) if sector else float('inf') for sector in sector_data]

        # Print or log sector distances
        for i, dist in enumerate(min_distances):
            print(f"Sector {i+1} ({i*self.sector_size:.1f}° to {(i+1)*self.sector_size:.1f}°): min distance = {dist:.2f} m")

def main(args=None):
    rclpy.init(args=args)
    node = Lidar8Direction()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()