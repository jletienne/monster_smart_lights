import yaml
'''import tinytuya

device_id = 'device-id'
addy = '192.168.1.xxx'

d = tinytuya.OutletDevice(device_id, addy,'')
d.set_version(3.3)
data = d.status() 
print('Device status: %r' % data)'''

def hello():
    devices = yaml.safe_load(open('/Users/jletienne/monster/config.yaml'))['devices']['living_room']
    for device in devices: 
        print(device)
    return 'Done'

if __name__ == "__main__":
    print(hello())