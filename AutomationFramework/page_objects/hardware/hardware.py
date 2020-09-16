from AutomationFramework.page_objects.base.base_page_object import BasePageObject


class Hardware(BasePageObject):
    variables_paths = {
        'hw_cpu_avg': [
            {
                'name': 'components/component/name',
                'avg': 'components/component/cpu/utilization/state/avg',
            }
        ],
        'hw_cpu_instant': [
            {
                'name': 'components/component/name',
                'instant': 'components/component/cpu/utilization/state/instant',
            }
        ],
        'hw_cpu_interval': [
            {
                'name': 'components/component/name',
                'interval': 'components/component/cpu/utilization/state/interval',
            }
        ],
        'hw_cpu_max': [
            {
                'name': 'components/component/name',
                'max': 'components/component/cpu/utilization/state/max',
            }
        ],
        'hw_cpu_max_time': [
            {
                'name': 'components/component/name',
                'max_time': 'components/component/cpu/utilization/state/max-time',
            }
        ],
        'hw_cpu_min': [
            {
                'name': 'components/component/name',
                'min': 'components/component/cpu/utilization/state/min',
            }
        ],
        'hw_cpu_min_time': [
            {
                'name': 'components/component/name',
                'min_time': 'components/component/cpu/utilization/state/min-time',
            }
        ],
        'hw_psu_enabled': [
            {
                'name': 'components/component/name',
                'enabled': 'components/component/power-supply/config/enabled',
            }
        ],
        'hw_psu_capacity': [
            {
                'name': 'components/component/name',
                'capacity': 'components/component/power-supply/state/capacity',
            }
        ],
        'hw_psu_enabled_state': [
            {
                'name': 'components/component/name',
                'enabled': 'components/component/power-supply/state/enabled',
            }
        ],
        'hw_psu_input_voltage': [
            {
                'name': 'components/component/name',
                'input_voltage': 'components/component/power-supply/state/input-voltage',
            }
        ],
        'hw_psu_output_current': [
            {
                'name': 'components/component/name',
                'output_current': 'components/component/power-supply/state/output-current',
            }
        ],
        'hw_psu_output_power': [
            {
                'name': 'components/component/name',
                'output_power': 'components/component/power-supply/state/output-power',
            }
        ],
        'hw_psu_output_voltage': [
            {
                'name': 'components/component/name',
                'output_voltage': 'components/component/power-supply/state/output-voltage',
            }
        ],
        'hw_psu_input_current': [
            {
                'name': 'components/component/name',
                'input_current': 'components/component/power-supply/state/input-current',
            }
        ],
        'hw_component_description': [
            {
                'name': 'components/component/name',
                'description': 'components/component/state/description',
            }
        ],
        'hw_component_hardware_version': [
            {
                'name': 'components/component/name',
                'hardware_version': 'components/component/state/hardware-version',
            }
        ],
        'hw_component_id': [
            {
                'name': 'components/component/name',
                'id': 'components/component/state/id',
            }
        ],
        'hw_component_location': [
            {
                'name': 'components/component/name',
                'location': 'components/component/state/location',
            }
        ],
        'hw_component_mfg_date': [
            {
                'name': 'components/component/name',
                'mfg_date': 'components/component/state/mfg-date',
            }
        ],
        'hw_component_oper_status': [
            {
                'name': 'components/component/name',
                'oper_status': 'components/component/state/oper-status',
            }
        ],
        'hw_component_parent': [
            {
                'name': 'components/component/name',
                'parent': 'components/component/state/parent',
            }
        ],
        'hw_component_serial_no': [
            {
                'name': 'components/component/name',
                'serial_no': 'components/component/state/serial-no',
            }
        ],
        'hw_component_type': [
            {
                'name': 'components/component/name',
                'type': 'components/component/state/type',
            }
        ],
        'hw_subcomponent_name': [
            {
                'name': 'components/component/name',
            },
            {
                'name': 'components/component/name',
            },
            {
                'name': 'components/component/name',
                'subcomponent_name': 'components/component/subcomponents/subcomponent/name',
            }
        ],
        'hw_subcomponent_name_state': [
            {
                'name': 'components/component/name',
            },
            {
                'name': 'components/component/name',
            },
            {
                'name': 'components/component/name',
                'subcomponent_name': 'components/component/subcomponents/subcomponent/name',
            },
            {
                'name': 'components/component/name',
                'subcomponent_name': 'components/component/subcomponents/subcomponent/name',
                'empty_name': 'components/component/subcomponents/subcomponent/state/name',
            }
        ],
        'hw_properties_name': [
            {
                'name': 'components/component/name',
                'empty_name': 'components/component/properties/property/state/name',
            }
        ],
        'hw_properties_value': [
            {
                'name': 'components/component/name',
                'value': 'components/component/properties/property/state/value',
            }
        ],
        'hw_transceiver_enabled': [
            {
                'name': 'components/component/name',
                'enabled': 'components/component/transceiver/config/enabled',
            }
        ],
        'hw_transceiver_slot_id': [
            {
                'name': 'components/component/name',
                'slot_id': 'components/component/linecard/state/slot-id',
            }
        ],
        'hw_transceiver_enabled_state': [
            {
                'name': 'components/component/name',
                'enabled': 'components/component/transceiver/state/enabled',
            }
        ],
        'hw_linecard_power_admin': [
            {
                'name': 'components/component/name',
                'power_admin_state': 'components/component/linecard/config/power-admin-state',
            }
        ],
        'hw_linecard_power_admin_state': [
            {
                'name': 'components/component/name',
                'power_admin_state': 'components/component/linecard/state/power-admin-state',
            }
        ],
        'hw_fan_speed': [
            {
                'name': 'components/component/name',
                'speed': 'components/component/fan/state/speed',
            }
        ],
        'hw_config_name': [
            {
                'name': 'components/component/name',
            }
        ],
        'hw_port_channel_speed': [
            {
                'name': 'components/component/name',
                'channel_speed': 'components/component/port/breakout-mode/config/channel-speed',
            }
        ],
        'hw_port_channel_speed_state': [
            {
                'name': 'components/component/name',
                'channel_speed': 'components/component/port/breakout-mode/config/channel-speed',
            },
            {
                'name': 'components/component/name',
                'channel_speed': 'components/component/port/breakout-mode/state/channel-speed',
            }
        ],
        'hw_port_num_channels': [
            {
                'name': 'components/component/name',
                'num_channels': 'components/component/port/breakout-mode/config/num-channels',
            }
        ],
        'hw_port_num_channels_state': [
            {
                'name': 'components/component/name',
                'num_channels': 'components/component/port/breakout-mode/config/num-channels',
            },
            {
                'name': 'components/component/name',
                'num_channels': 'components/component/port/breakout-mode/state/num-channels',
            }
        ],
    }

    def execute_hardware_component_edit_config_test_case(self):
        filter_to_use = """
                    <filter>
                        <components xmlns="http://openconfig.net/yang/platform">
                            <component>
                              <name>{}</name>
                            </component>
                          </components>
                    </filter>
                    """
        interface_name = self.get_variable_value_for_rpc_in_test_case(rpc_index=self.rpc_idx_in_test_case, variable='name')
        self.set_filter(filter_to_use.format(interface_name))
        self.execute_generic_edit_config_test_case()

    def execute_hardware_rpc(self):
        if self.rpcs_list[self.rpc_idx_in_test_case]['operation'] == 'edit-config':
            self.execute_hardware_component_edit_config_test_case()
        elif self.rpcs_list[self.rpc_idx_in_test_case]['operation'] == 'get':
            self.execute_get_test_case_with_dispatch()

    def execute_rpc(self):
        self.execute_hardware_rpc()
