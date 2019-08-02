

class Gcode:

    def __init__(self):
        super().__init__()

        self.file_fullname: str
        self.origin_data: str
        self.data: str
        self.properties = self.Properties()

    @staticmethod
    def get_value_by_command(command_name, value_name):
        pass

    @staticmethod
    def write(fullname, data):
        pass

    def load(self, fullname):
        pass

    def clean(self):
        pass

    class Properties:
        def __init__(self):
            self.min_layer_height: float  # [mm]
            self.max_layer_height: float  # [mm]

            self.x_axis = self.Axis()
            self.y_axis = self.Axis()
            self.z_axis = self.Axis()

            self.tool_heads = []

            self.weight: float
            self.length: float
            self.coast: float
            self.time: float

        class Axis:
            def __init__(self):
                self.max_acceleration: float  # [mm]
                self.max_velocity: float  # [mm]
                self.min_pos: float  # [mm]
                self.max_pos: float  # [mm]
                self.size: float  # [mm]

        class ToolHead:
            def __init__(self):
                self.max_acceleration: float  # [mm]
                self.max_velocity: float  # [mm]

                self.nozzle_diameter: float  # [mm]
                self.max_temperature: float  # [degrees]

