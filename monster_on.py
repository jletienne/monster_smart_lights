import tinytuya
import yaml


def monster_turn_on():
    devices = yaml.safe_load(open('/Users/jletienne/monster/config.yaml'))['devices']['living_room']

    for device in devices: 
        device_id = devices[device]['device_id']
        addy = devices[device]['address']

        d = tinytuya.OutletDevice(device_id, addy,'')
        d.set_version(3.3)


        d.turn_on(switch=20, nowait=False)
        print(f'Monster {device} On')
    return 'Monster Vibes'

if __name__ == "__main__":
    print(monster_turn_on())