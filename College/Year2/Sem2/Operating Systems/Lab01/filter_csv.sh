input=$1
output=$2

if [ ! -f $input ]; then
  echo "Input file doesn't exist"
  exit 1
fi

if [ $output == "" ]; then
  echo "Output file not provided!"
  exit 1
fi

if [ -f $output ]; then
  echo "Output file already exists!"
  exit 1
fi
i=1
while IFS=, read -r ID time temp pressure; do
  # ignore the first line
  if (( i == 1 )); then
    ((i++))
  else
  if (( $(echo "$temp < 50" | bc -l) )); then
    echo "ID: $ID, Time: $(date -d @$time), Temp: $temp, Pressure: $pressure" >> $output
  fi
  fi
done < $input
