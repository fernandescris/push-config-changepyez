from jnpr.junos import Device
dev = Device(host = '172.19.64.26' ,  user='csim', password='Juniper123' )
from jnpr.junos.utils.config import Config
cu = Config(dev)
dev.open()
rsp = cu.load( path="config-example.conf" )
cu.commit()