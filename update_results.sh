#! /bin/bash

processes="$1"
repetitions="$2"


# Update the noisy tournaments
echo "-- Regenerating noisy tournament figures"
# Run the noisy tournament
python run_axelrod --noise 0.05 -p $processes -o assets -r $repetitions --xc --xs --xa
# Copy these figures over, renaming as appropriate
mv assets/basic_strategies_payoff.svg assets/basic_strategies_payoff_noise_5.svg
mv assets/basic_strategies_boxplot.svg assets/basic_strategies_boxplot_noise_5.svg
mv assets/basic_strategies_winplot.svg assets/basic_strategies_winplot_noise_5.svg
mv assets/basic_strategies_sdvplot.svg assets/basic_strategies_sdvplot_noise_5.svg
mv assets/basic_strategies_pdplot.svg assets/basic_strategies_pdplot_noise_5.svg

# Running noiseless tournament
echo "-- Running basic Axelrod, regenerating cache, results, and figures"
python run_axelrod -p $processes -o assets -r $repetitions --xc --xs --xa

# Running prob end tournament with p_end=0.1
echo "-- Running basic Prob End Axelrod, regenerating cache, results, and figures"
# Also Copy the results and figures over to assets
python run_axelrod -pe 0.1 -o assets -r $repetitions --xc --xs --xa

echo "Be sure to git commit changes to update the docs!"
