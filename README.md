# pyre-security-configs
A repository to contain source/sink definitions for Pyre to use

# Testing
A file (source.py) is included which should trigger on all flows that have been defined.

To run pyre-check with our defined sources/sinks make sure to include the following in your `.pyre_configuration`

```
"taint_models_path": "/home/nwalsh/PycharmProjects/pyre-security-configs/stubs/taint
```
