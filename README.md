_Highly_ WIP Python bindings for [ImTui](https://github.com/ggerganov/imtui) based on [deargui](https://github.com/cammm/deargui).

It is highly recommended to build and run in a Virtual or Conda Environment.

## Build and Run

Don't forget to initialize submodules!

```bash
git submodule update --init --recursive
```

Install build requirements:

```bash
pip install -r requirements.txt

```

### Wheel Build

```bash
BUILD_DIR=/path/to/build/dir bash build_wheel.sh

```

Default build path if `BUILD_DIR` is not set is `build/`.

The wheel will be present in the build path. It can be installed with e.g.

```bash
pip install build/imtui_py-0.0.1-py3-none-any.whl
```

Run with

```bash
python test_imtui.py
```

If all has gone well, you should see a window with an exit button.

### Manual Build (Not recommended)

```bash
cmake -B build
cmake --build build -- -j <#threads_you_want>
```

Run

```bash
PYTHONPATH=build/:$PYTHONPATH python test_imtui.py
```



## Credits

* [ImTui](https://github.com/ggerganov/imtui) : TUI backend for Dear ImGui.
* [deargui](https://github.com/cammm/deargui) : Pybind11 bindings Dear for ImGui.
* [Dear ImGui](https://github.com/ocornut/imgui) : Immediate mode GUI library.
