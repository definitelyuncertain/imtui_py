_Highly_ WIP Python bindings for (ImTui)[https://github.com/ggerganov/imtui] based on (deargui)[https://github.com/cammm/deargui].

## Build

```bash
cmake -B build
cmake --build build -- -j <#threads_you_want>
```

Don't forget to initialize submodules!

```bash
git submodule update --init --recursive
```


## Run

```bash
PYTHONPATH=build/:$PYTHONPATH python test_imtui.py
```

If all has gone well, you should see a window with an exit button.

## Credits

* (ImTui)[https://github.com/ggerganov/imtui] : TUI backend for Dear ImGui.
* (deargui)[https://github.com/cammm/deargui] : Pybind11 bindings Dear for ImGui.
* (Dear ImGui)[https://github.com/ocornut/imgui] : Immediate mode GUI library.
