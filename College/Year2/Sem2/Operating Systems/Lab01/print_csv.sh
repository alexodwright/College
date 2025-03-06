input=$1

if [ ! -f $input ]; then
  echo "File does not exist"
  exit 1
fi

while IFS=, read -r ID time temp pressure; do
  date= date -d @$time
  echo "ID: $ID, Time: $date, Temp: $temp, Pressure: $pressure"
done < $input
