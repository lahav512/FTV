class DataStructures:
    class Users:
        account = {
            "username": str,
            "password": str,
            "first_name": str,
            "last_name": str
        }  # user name

        workshop = {
            "username": str,
            "workshop_name": str,
            "next_ids": {
                "station": 0,
                "controller": 0,
                "printer": 0,
                "filament_changer": 0,
                "filament": 0
            },
            "stations": [],
            "controllers": [],
            "printers": [],
            "filament_changers": [],
            "filaments": []
        }  # workshop name

    class Workshops:
        station = {
            "username": str,
            "workshop_name": str,  # id
            "station_name": str,
            "machine_id": str,  # str(int)
            "machine_version": str,
            "firmware_version": str,
            "capacity": None,  # str(int)  # max amount of controllers
            "filament_changers": []  # ids of the filament changers
        }  # station name

        controller = {
            "machine_id": str,  # str(int)
            "printer": None,  # str(int)  # printer id
            "bed": None,  # str(int)
            "filament_link": [str(int), str(int), str(int)]  # [id of the filament changer, id of the channel, id of the filament]
        }

        printer = {
            "id": None,  # str(int)
            "name": str,
            "manufacturer": str,
            "firmware": str,
            "bitrate": None,  # str(int)
            "build_size": [
                None,  # str(float)
                None,  # str(float)
                str(float)
            ],
            "nozzle_diameter": None,  # str(float)
            "head_max_temp": None,  # str(int)
            "bed_max_temp": None,  # str(int)  # None/0 if there is no bed
            "min_layer_height": None,  # str(float)  # mm
            "max_layer_height": None,  # str(float)  # mm
            "max_velocity": [
                None,  # str(float)
                None,  # str(float)
                str(float)
            ],
            "max_print_velocity": [
                None,  # str(float)
                None,  # str(float)
                str(float)
            ],  # recommended
            "max_acceleration": [
                None,  # str(float)
                None,  # str(float)
                str(float)
            ],
            "statistics": {
                "entire_life": None,  # str(float)  # hours
                "print_life_total": None,  # str(float)  # hours
                "print_life_success": None,  # str(float)  # hours
                "print_life_failure": None,  # str(float)  # hours
                "prints_total": None,  # str(int)
                "prints_success": None,  # str(int)
                "prints_failure": str(int)
            }
        }

        filament_changer = {
            "id": None,  # str(int)
            "capacity": None,  # str(int)  # max amount of channels
            "min_temp": None,  # str(int)
            "max_temp": None,  # str(int)
            "channels": {}
        }  # ids of the channels: ids of the filaments

        filament = {
            "id": None,  # str(int)
            "material": str,
            "color": str,  # color
            "min_temp": None,  # str(int)
            "max_temp": None,  # str(int)
            "opacity": None,  # str(float)  # 0 < x < 100
            "diameter": None,  # str(float)  # mm
            "density": None,  # str(float)  # g/cm^3
            "initial_weight": None,  # str(float)  # g
            "initial_length": None,  # str(float)  # mm
            "spool_weight": None,  # str(float)  # g
            "current_weight": None,  # str(float)  # g
            "current_length": None,  # str(float)  # mm
            "currency": str(float)  # $/g
        }
