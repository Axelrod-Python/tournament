#! /bin/bash

processes="$1"
repetitions="$2"

# Update the noisy tournaments
echo "-- Regenerating noisy tournament figures"
# Run the noisy tournament
#python3.5 run_axelrod --noise 0.05 -p $processes -o assets -r $repetitions --xc
python3.5 run_axelrod --noise 0.05 -o assets -r $repetitions -t 20
# Copy these figures over, renaming as appropriate
mv assets/strategies_payoff.svg assets/strategies_payoff_noise_5.svg
mv assets/strategies_boxplot.svg assets/strategies_boxplot_noise_5.svg
mv assets/strategies_winplot.svg assets/strategies_winplot_noise_5.svg
mv assets/strategies_sdvplot.svg assets/strategies_sdvplot_noise_5.svg
mv assets/strategies_pdplot.svg assets/strategies_pdplot_noise_5.svg

# Running noiseless tournament
echo "-- Running Axelrod, regenerating cache, results, and figures"
# Also Copy the results and figures over to assets
#python3.5 run_axelrod -p $processes -o assets -r $repetitions --xc
python3.5 run_axelrod -o assets -r $repetitions -t 20

# Running prob end tournament with p_end=0.1
echo "-- Running Prob End Axelrod, regenerating cache, results, and figures"
# Also Copy the results and figures over to assets
#python3.5 run_axelrod -pe 0.1 -p $processes -o assets -r $repetitions --xc
python3.5 run_axelrod -pe 0.1 -o assets -r $repetitions

echo "Be sure to git commit changes to update the docs!"
