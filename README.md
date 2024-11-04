![StandardRL Components Logo](https://assets.standardrl.com/general/components/icon-full.png)
# Really Simple Measurement

Simple script to measure the performance of a an application on Raspberry Pi in one line. Measures memory usage (in %), CPU utilisation (in %) and CPU temperature (in C). Works in Python, requires only `psutil`.

## Usage

`python3 measure.py`

Press Control+C to stop execution. While the script is running, measurements are made every 0.5 seconds. When finished, results are output to `results.csv`.
