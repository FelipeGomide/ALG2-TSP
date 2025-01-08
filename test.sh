for file in data/giant/* ; do
base=$(basename $file);
name=${base%.tsp};
echo -e "$base";
python main.py -t $file;
echo "";
done