class DataStructures: 
    user = {
        "account": {
            "first_name": str,
            "last_name": str,
            "password": str
        },
        "workshops": {}
    }  # user name

    workshop = {
        "next_ids": {
            "station": 0,
            "controller": 0,
            "printer": 0,
            "filament_changer": 0,
            "filament": 0
        },
        "stations": {},
        "controllers": [],
        "printers": [],
        "filament_changers": [],
        "filaments": []
    }  # workshop name

    station = {
        "id": int,
        "capacity": int,  # max amount of controllers
        "filament_changers": []  # ids of the filament changers
    }  # station name

    controller = {
        "id": int,
        "printer": int,  # printer id
        "bed": int,
        "filament_link": [int, int, int]  # [id of the filament changer, id of the channel, id of the filament]
    }

    printer = {
        "id": int,
        "name": str,
        "manufacturer": str,
        "firmware": str,
        "bitrate": int,
        "build_size": [
            float,
            float,
            float
        ],
        "nozzle_diameter": float,
        "head_max_temp": int,
        "bed_max_temp": int,  # None/0 if there is no bed
        "min_layer_height": float,  # mm
        "max_layer_height": float,  # mm
        "max_velocity": [
            float,
            float,
            float
        ],
        "max_print_velocity": [
            float,
            float,
            float
        ],  # recommended
        "max_acceleration": [
            float,
            float,
            float
        ],
        "statistics": {
            "entire_life": float,  # hours
            "print_life_total": float,  # hours
            "print_life_success": float,  # hours
            "print_life_failure": float,  # hours
            "prints_total": int,
            "prints_success": int,
            "prints_failure": int
        }
    }

    filament_changer = {
        "id": int,
        "capacity": int,  # max amount of channels
        "min_temp": int,
        "max_temp": int,
        "channels": {}
    }  # ids of the channels: ids of the filaments

    filament = {
        "id": int,
        "material": str,
        "color": str,  # color
        "min_temp": int,
        "max_temp": int,
        "opacity": float,  # 0 < x < 100
        "diameter": float,  # mm
        "density": float,  # g/cm^3
        "initial_weight": float,  # g
        "initial_length": float,  # mm
        "spool_weight": float,  # g
        "current_weight": float,  # g
        "current_length": float,  # mm
        "currency": float  # $/g
    }
