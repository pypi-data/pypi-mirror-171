# py-machineid

Get the unique machine ID of any host (without admin privileges).

Sponsored by:

[![Keygen logo](https://user-images.githubusercontent.com/6979737/175406169-bd8bf064-7343-4bd1-94b7-a773ecec07b8.png)](https://keygen.sh)

_A software licensing and distribution API built for developers._

## Usage

To obtain the raw GUID of the device, use `id() -> str`:

```python
import machineid

print(machineid.id())
```

To obtain an anonymized (hashed) version of the GUID, see below. The
`hashed_id(str) -> str` function takes an optional application ID,
which will ensure a unique ID per-app for the same device.

```python
import machineid

print(machine.hashed_id('myappid'))
print(machine.hashed_id())
```
