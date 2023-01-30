from devices import Device
from typing import List, Optional


class Room:

    def __init__(self, area: float, name: str = None):
        self.area = area
        self.name = name

    def __repr__(self):
        return f"{self.name} ({self.area} m^2)"


class Floor:

    def __init__(self, floor_no: int):
        self.floor_no = floor_no
        self.rooms = []


class SmartHouse:

    def __init__(self):
        self.floors = []

    def create_floor(self) -> Floor:
        return NotImplemented

    def create_room(self, floor_no: int, area: float, name: str = None) -> Room:
        return NotImplemented

    def get_no_of_rooms(self) -> int:
        return NotImplemented

    def get_all_devices(self) -> List[Device]:
        return NotImplemented

    def get_all_rooms(self) -> List[Room]:
        return NotImplemented

    def get_total_area(self) -> float:
        return NotImplemented

    def register_device(self, device: Device, room: Room):
        return NotImplemented

    def get_no_of_devices(self):
        return NotImplemented

    def get_no_of_sensors(self):
        return NotImplemented

    def get_no_of_actuators(self):
        return NotImplemented

    def move_device(self, device: Device, from_room: Room, to_room: Room):
        return NotImplemented

    def find_device_by_serial_no(self, serial_no: str) -> Device:
        return NotImplemented

    def get_room_with_device(self, device: Device):
        return NotImplemented

    def get_all_devices_in_room(self, room: Room) -> List[Device]:
        return NotImplemented

    def turn_on_lights_in_room(self, room: Room):
        return NotImplemented

    def turn_of_lights_in_room(self, room: Room):
        return NotImplemented

    def get_temperature_in_room(self, room: Room) -> float:
        return NotImplemented

    def set_temperature_in_room(self, room: Room, temperature: float):
        return NotImplemented
