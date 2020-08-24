from AutomationFramework.page_objects.base.base_page_object import BasePageObject


class QOS(BasePageObject):
    variables_paths = {
        'qos_queue_name': [
            {
                'name': 'qos/queues/queue/name',
            }
        ],
        'qos_queue_minth': [
            {
                'name': 'qos/queues/queue/name',
                'queue_type': 'qos/queues/queue/config/queue-type',
                'minth': 'qos/queues/queue/red/config/minth',
            }
        ],
        'qos_queue_maxth': [
            {
                'name': 'qos/queues/queue/name',
                'queue_type': 'qos/queues/queue/config/queue-type',
                'maxth': 'qos/queues/queue/red/config/maxth',
            }
        ],
    }

    def execute_qos_queue_edit_config_test_case(self):
        filter_to_use = """
                    <filter>
                        <qos xmlns="http://openconfig.net/yang/qos">
                        <queues>
                            <queue>
                                <name>{}</name>
                            </queue>
                        </queues>
                      </qos>
                    </filter>
                    """
        interface_name = self.get_variable_value_for_rpc_in_test_case(rpc_index=0, variable='name')
        self.set_filter(filter_to_use.format(interface_name))
        self.execute_generic_edit_config_test_case()
