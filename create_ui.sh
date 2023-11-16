folder=$1
ui=$(ls $folder | grep .ui)

path=$folder$ui
echo $path

pyside6-uic $path -o ${folder}ui_mainwindow.py

ret=$(echo $?)
if [ "$ret" -eq "0" ]; then
   echo "Success";
   exit;
else
   echo "Failed to generate UI"
   exit;
fi
