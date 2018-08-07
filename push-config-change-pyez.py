from jnpr.junos import Device
dev = Device('192.168.0.1')
from jnpr.junos.utils.config import Config
cu = Config(dev)
dev.open()
rsp = cu.load( path="config-example.conf" )
cu.commit()

