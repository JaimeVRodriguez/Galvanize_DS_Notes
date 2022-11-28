## UNIX Exploration
***
### Assignment 1
Find specific elements of a file and sort them into a specific file. Then run .py file with created file.

Multi-Line Command
`less 2015_sp100.csv | grep GOOG > 2015_goog.csv`
`sort 2015_goog.csv > 2015_goog_sorted.csv`
`python plot_stock_prices.py < 2015_goog_sorted.csv`

Single Line Command
`cat 2015_sp100.csv | grep GOOG | sort > 2015_goog_sorted2.csv | python plot_stock_prices.py < 2015_goog_sorted2.csv`
