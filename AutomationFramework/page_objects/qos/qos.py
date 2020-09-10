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
        'qos_scheduler_policy_name': [
            {
                'name': 'qos/scheduler-policies/scheduler-policy/name',
            }
        ],
        'qos_scheduler_sequence': [
            {
                'name': 'qos/scheduler-policies/scheduler-policy/name',
                'sequence': 'qos/scheduler-policies/scheduler-policy/schedulers/scheduler/sequence',
            }
        ],
        'qos_scheduler_id': [
            {
                'name': 'qos/scheduler-policies/scheduler-policy/name',
                'sequence': 'qos/scheduler-policies/scheduler-policy/schedulers/scheduler/sequence',
                'id': 'qos/scheduler-policies/scheduler-policy/schedulers/scheduler/inputs/input/id',
            }
        ],
        'qos_scheduler_queue': [
            {
                'name': 'qos/queues/queue/name',
            },
            {
                'name': 'qos/scheduler-policies/scheduler-policy/name',
                'sequence': 'qos/scheduler-policies/scheduler-policy/schedulers/scheduler/sequence',
                'id': 'qos/scheduler-policies/scheduler-policy/schedulers/scheduler/inputs/input/id',
                'input_type': 'qos/scheduler-policies/scheduler-policy/schedulers/scheduler/inputs/input/config/input-type',
                'queue_name': 'qos/scheduler-policies/scheduler-policy/schedulers/scheduler/inputs/input/config/queue',
            },
        ],
        'qos_scheduler_weight': [
            {
                'name': 'qos/scheduler-policies/scheduler-policy/name',
                'sequence': 'qos/scheduler-policies/scheduler-policy/schedulers/scheduler/sequence',
                'id': 'qos/scheduler-policies/scheduler-policy/schedulers/scheduler/inputs/input/id',
                'weight': 'qos/scheduler-policies/scheduler-policy/schedulers/scheduler/inputs/input/config/weight',
            }
        ],
        'qos_scheduler_cir': [
            {
                'name': 'qos/scheduler-policies/scheduler-policy/name',
                'sequence': 'qos/scheduler-policies/scheduler-policy/schedulers/scheduler/sequence',
                'cir': 'qos/scheduler-policies/scheduler-policy/schedulers/scheduler/one-rate-two-color/config/cir',
            }
        ],
        'qos_scheduler_bc': [
            {
                'name': 'qos/scheduler-policies/scheduler-policy/name',
                'sequence': 'qos/scheduler-policies/scheduler-policy/schedulers/scheduler/sequence',
                'bc': 'qos/scheduler-policies/scheduler-policy/schedulers/scheduler/one-rate-two-color/config/bc',
            }
        ],
        'qos_scheduler_max_queue_depth_bytes': [
            {
                'name': 'qos/scheduler-policies/scheduler-policy/name',
                'sequence': 'qos/scheduler-policies/scheduler-policy/schedulers/scheduler/sequence',
                'max_queue_depth_bytes': 'qos/scheduler-policies/scheduler-policy/schedulers/scheduler/one-rate-two-color/config/max-queue-depth-bytes',
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
        interface_name = self.get_variable_value_for_rpc_in_test_case(rpc_index=self.rpc_idx_in_test_case, variable='name')
        self.set_filter(filter_to_use.format(interface_name))
        self.execute_generic_edit_config_test_case()

    def execute_qos_scheduler_edit_config_test_case(self):
        filter_to_use = """
                    <filter>
                        <qos xmlns="http://openconfig.net/yang/qos">
                        <scheduler-policies>
                            <scheduler-policy>
                                <name>{}</name>
                            </scheduler-policy>
                        </scheduler-policies>
                      </qos>
                    </filter>
                    """
        interface_name = self.get_variable_value_for_rpc_in_test_case(rpc_index=self.rpc_idx_in_test_case, variable='name')
        self.set_filter(filter_to_use.format(interface_name))
        self.execute_generic_edit_config_test_case()
