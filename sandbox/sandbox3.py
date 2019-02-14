# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.


def m3_trace_color_using_camera(self, speed, direction_speed):
    while True:
        blob = self.sensor_system.camera.get_biggest_blob()
        print(blob)

        if self.sensor_system.camera.get_biggest_blob().get_area() < 600:
            if blob.center.x > 140 and blob.center.x < 180:
                self.go(speed, speed)
            if blob.center.x < 150:
                self.left(direction_speed, direction_speed)
            elif blob.center.x > 170:
                self.right(direction_speed, direction_speed)
        elif self.sensor_system.camera.get_biggest_blob().get_area() > 1600:
            if blob.center.x > 140 and blob.center.x < 180:
                self.go(-speed, -speed)
            if blob.center.x < 150:
                self.left(direction_speed, direction_speed)
            elif blob.center.x > 170:
                self.right(direction_speed, direction_speed)
            if 1500 < self.sensor_system.camera.get_biggest_blob().get_area() < 1600:
                self.stop()
                break


