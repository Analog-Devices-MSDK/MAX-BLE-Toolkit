
class UtilsBLE:

    @staticmethod
    def convert_uuid_to_array_str(uuid):
        n = 2
        uuid = uuid.replace('-', '')
        split_string = ["0x"+uuid[i:i + n] for i in range(0, len(uuid), n)]
        split_string.reverse()
        return ', '.join(split_string)

    @staticmethod
    def convert_ble_type_to_primitive_c(ble_type):
        if ble_type == "bool" or ble_type == "uint8":
            return "uint8_t"
        elif ble_type == "uint16":
            return "uint16_t"
        elif ble_type == "uint32":
            return "uint32_t"
        return "spec_" + ble_type.lower()

    @staticmethod
    def convert_ble_type_to_primitive_dart(ble_type):
        if ble_type == "bool":
            return "Bool"
        elif ble_type == "uint8" or ble_type == "Blob":
            return "Uint8"
        elif ble_type == "uint16" or ble_type == "temperature":
            return "Uint16"
        elif ble_type == "uint32" or ble_type == "date_time":
            return "Uint32"
        return "spec" + ble_type.lower()

    @staticmethod
    def is_array(size):
        return size > 1

    @staticmethod
    def is_configurable(permission):
        return UtilsBLE.get_simple_permission(permission) == "R/W"

    @staticmethod
    def get_simple_permission(permission):
        if 'R/W' in permission:
            return 'R/W'
        else:
            return 'R'
