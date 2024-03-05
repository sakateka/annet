from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Any

from annet.annlib.netdev.views.hardware import HardwareView
from .common_models import Entity, DeviceType, DeviceIp, IpAddress, Label


@dataclass
class Interface(Entity):
    device: Entity
    enabled: bool
    display: str = ""
    ip_addresses: List[IpAddress] = field(default_factory=list)


@dataclass
class Device(Entity):
    display: str
    device_type: DeviceType
    device_role: Entity
    tenant: Optional[Entity]
    platform: Optional[Entity]
    serial: str
    asset_tag: Optional[str]
    site: Entity
    rack: Optional[Entity]
    position: Optional[float]
    face: Optional[Label]
    status: Label
    primary_ip: Optional[DeviceIp]
    primary_ip4: Optional[DeviceIp]
    primary_ip6: Optional[DeviceIp]
    tags: List[Entity]
    custom_fields: dict[str, Any]
    created: datetime
    last_updated: datetime

    fqdn: str
    hostname: str
    hw: Optional[HardwareView]
    breed: str

    interfaces: List[Interface]

    # compat
    def __hash__(self):
        return hash(self.id)

    def is_pc(self):
        return self.device_type.manufacturer.name == "Mellanox"
