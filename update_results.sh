#! /bin/bash

processes="$1"
repetitions="$2"


# Running noiseless tournament
echo "-- Running basic Axelrod, regenerating cache, results, and figures"
python run_axelrod -p $processes -o assets -r $repetitions --xc --xs --xa

# Running prob end tournament with p_end=0.1
echo "-- Running basic Prob End Axelrod, regenerating cache, results, and figures"
# Also Copy the results and figures over to assets
python run_axelrod -pe 0.1 -o assets -r $repetitions --xc --xs --xa

echo "Be sure to git commit changes to update the docs!"
