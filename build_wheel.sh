build_dir=${BUILD_DIR:-"build/"}

cmake -B ${build_dir}
cmake --build ${build_dir}


mkdir -p $build_dir/wheel
cp -r imtui_py $build_dir/wheel/
cp $build_dir/*.so $build_dir/wheel/
cp setup.py $build_dir/wheel/

pushd ${build_dir}/wheel
PYTHONPATH="`pwd`:$PYTHONPATH" pybind11-stubgen --ignore-all-errors -o . _imtui_py
PYTHONPATH="`pwd`:$PYTHONPATH" pybind11-stubgen -o . imtui_py
popd

pip wheel $build_dir/wheel -w $build_dir/
