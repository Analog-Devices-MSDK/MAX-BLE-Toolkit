from ble_renderer import execute_ble_renderer

if __name__ == '__main__':
    execute_ble_renderer("../../resources/services_sample.xlsx",
                         output_path_c="C:/Repo/max66900/fw/src/Peripherals/BLE/Services",
                         output_path_h="C:/Repo/max66900/fw/include/Peripherals/BLE/Services",
                         include_relative_path="Peripherals/BLE/Services/")
