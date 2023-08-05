# races_report

[![PyPI - Version](https://img.shields.io/pypi/v/races_report.svg)](https://pypi.org/project/races_report)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/races_report.svg)](https://pypi.org/project/races_report)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)
- [Running races_report with CLI](#running_with_cli)

## Installation

```console
pip install races_report
```

## License

`races_report` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## Running races_report with CLI

usage: ```main.py [-h] -p PATH [-d DRIVER] [--asc | --desc]```

optional arguments:

  ```-h, --help```            show this help message and exit

  ```-p PATH, --path PATH```  path to start and end data files

  ```-d DRIVER, --driver DRIVER```  driver's full name

  ```--asc```                 shows list of drivers in asc order

  ```--desc```                shows list of drivers in desc order

for example:
```console
 python main.py -p "results" --desc
```
or

```console
 python main.py -p "results" -d "Sebastian Vettel"
```

```
# main.py

from races_report import main


if __name__ == '__main__':
    main.main()


```

The directory `results` should contain the following files of a certain structure (for example):

```
# abbreviations.txt

DRR_Daniel Ricciardo_RED BULL RACING TAG HEUER
SVF_Sebastian Vettel_FERRARI
LHM_Lewis Hamilton_MERCEDES
KRF_Kimi Räikkönen_FERRARI
VBM_Valtteri Bottas_MERCEDES
EOF_Esteban Ocon_FORCE INDIA MERCEDES
FAM_Fernando Alonso_MCLAREN RENAULT
CSR_Carlos Sainz_RENAULT
SPF_Sergio Perez_FORCE INDIA MERCEDES
PGS_Pierre Gasly_SCUDERIA TORO ROSSO HONDA
NHR_Nico Hulkenberg_RENAULT
SVM_Stoffel Vandoorne_MCLAREN RENAULT
SSW_Sergey Sirotkin_WILLIAMS MERCEDES
CLS_Charles Leclerc_SAUBER FERRARI
RGH_Romain Grosjean_HAAS FERRARI
BHS_Brendon Hartley_SCUDERIA TORO ROSSO HONDA
MES_Marcus Ericsson_SAUBER FERRARI
LSW_Lance Stroll_WILLIAMS MERCEDES
KMH_Kevin Magnussen_HAAS FERRARI

```

```
# start.log

SVF2018-05-24_12:02:58.917
NHR2018-05-24_12:02:49.914
FAM2018-05-24_12:13:04.512
KRF2018-05-24_12:03:01.250
SVM2018-05-24_12:18:37.735
MES2018-05-24_12:04:45.513
LSW2018-05-24_12:06:13.511
BHS2018-05-24_12:14:51.985
EOF2018-05-24_12:17:58.810
RGH2018-05-24_12:05:14.511
SSW2018-05-24_12:16:11.648
KMH2018-05-24_12:02:51.003
PGS2018-05-24_12:07:23.645
CSR2018-05-24_12:03:15.145
SPF2018-05-24_12:12:01.035
DRR2018-05-24_12:14:12.054
LHM2018-05-24_12:18:20.125
CLS2018-05-24_12:09:41.921
VBM2018-05-24_12:00:00.000

```

```
# end.log

MES2018-05-24_12:05:58.778 
RGH2018-05-24_12:06:27.441
SPF2018-05-24_12:13:13.883
LSW2018-05-24_12:07:26.834
DRR2018-05-24_12:11:24.067
NHR2018-05-24_12:04:02.979
CSR2018-05-24_12:04:28.095
KMH2018-05-24_12:04:04.396
BHS2018-05-24_12:16:05.164
SVM2018-05-24_12:19:50.198
KRF2018-05-24_12:04:13.889
VBM2018-05-24_12:01:12.434
SVF2018-05-24_12:04:03.332
EOF2018-05-24_12:12:11.838
PGS2018-05-24_12:08:36.586
SSW2018-05-24_12:11:24.354
FAM2018-05-24_12:14:17.169
CLS2018-05-24_12:10:54.750
LHM2018-05-24_12:11:32.585

```