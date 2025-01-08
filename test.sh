for file in $2/* ; do
base=$(basename $file);
name=${base%.tsp};
echo -e "$base";
python main.py $1 $file;
echo "";
done
