# Jinja Automation tools

Software and templates to automatically generate test cases for different vendors.

The purpose of this tool is automate the generation of the RPCs based on template that will be defined by Telefonica for the certification of NETCONF / YANG interfaces.

## How to use RPCGenerator

```bash
python RPCGenerator.py <testcase.yaml> <ip/optics> <Vendor>
```

Example:

```bash
python RPCGenerator.py testcase.yaml ip Juniper
```

## How to use RPCAutomator

```bash
python RPCAutomator.py <testcase.yaml> <ip/optics> <Vendor>
```

Example:

```bash
python RPCAutomator.py oc-testcases.yaml optical Huawei
```

For the example test case, folder _/tests_ shows the output for the given YAML.

## Dependencies

This software depends on Jinja2 and Pyyaml.