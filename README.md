# go-suez-optimizer-2025

A small CLI-tool to help the French Suez employees pick the best amounts to subscribe to *Classic* or *Multiple*. 

The [Go Suez](https://go.suez.com) operation runs from July 1st to July 15th.

## How to use?

The script must be run with *python*. It will display a proposal of amounts to distribute between the two plans as well as some additionnal information regarding the corresponding interest rate and the total gain in 5 years.

You can use the following options to customise the behaviour of the tool:

- `-s`, `--salary`: This is your raw yearly income before tax (default: 25000)
- `-i`, `--investment`: Specify the amount of money you want to invest (default: 2000)
- `-p`, `--price`: Indicate the bond price estimated in 5 years (default: 1.4)

Consult the help (option is `-h` or `--help`) for more details.


## Examples

1. You are a Junior developer earning 25k€ per year, you want to invest at most 2k€, and you believe the share price will rise to reach 1.45€ in 5 years.

You case use the following command:

```
python .\script.py -i 2000 -s 25000 -p 1.45
```

Which will output the following information:

```
~=< Suez Go Optimizer >=~
You should invest as follows:
- Classic: 1513.00€
        result: 2684.86€ (12.15%)
- Multiple: 487.00€
        result: 981.85€ (15.05%)
- Total: 3666.71€ (+1666.71€ @ 12.89%)
```

2. You are a manager of marketing earning 100k€ per year, you want to invest at most 8k€, and you believe the share price will rise to reach 1.32€ in 5 years.

You case use the following command:

```
python .\script.py -i 8000 -s 100000 -p 1.32
```

Which will output the following information:

```
~=< Suez Go Optimizer >=~
You should invest as follows:
- Classic: 6051.00€
        result: 8434.31€ (6.87%)
- Multiple: 1949.00€
        result: 2703.45€ (6.76%)
- Total: 11137.76€ (+3137.76€ @ 6.84%)
```

3. You are a VP of customer relations earning 300k€ per year, you want to invest at most 15k€, and you believe the share price will rise to reach 1.1€ in 5 years.

You case use the following command:

```
python .\script.py -i 15000 -s 300000 -p 1.1
```

Which will output the following information:

```
~=< Suez Go Optimizer >=~
You should invest as follows:
- Classic: 15000.00€
        result: 16872.49€ (2.38%)
- Multiple: 0.00€
        result: 0.00€ (nan%)
- Total: 16872.49€ (+1872.49€ @ 2.38%)
```