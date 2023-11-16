folder=$1
ui=$(ls $folder | grep .ui)
echo $ui
path=$folder$ui
echo $path
pyside6-uic $path -o ${folder}ui_mainwindow.py
echo $?