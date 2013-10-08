mkdir -p build
cd build
cmake ../
pwd
echo Running make in $PWD
make
cd ../bindings
python setup.py config
python setup.py build
cd ..
cp bindings/damascene.so .
