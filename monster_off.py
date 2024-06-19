import tinytuya
import yaml

#devices = yaml.safe_load(open('monster/config.yaml'))['devices']['living_room']
def monster_turn_off():
    devices = yaml.safe_load(open('/Users/jletienne/monster/config.yaml'))['devices']['living_room']
   # print(devices)
    for device in devices: 
        device_id = devices[device]['device_id']
        addy = devices[device]['address']

        d = tinytuya.OutletDevice(device_id, addy,'')
        d.set_version(3.3)


        d.turn_off(switch=20, nowait=True)
        print(f'Monster {device} On')

    return 'Monster Off'

if __name__ == "__main__":
    print(monster_turn_off())