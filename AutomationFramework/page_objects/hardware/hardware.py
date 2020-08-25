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
    }
