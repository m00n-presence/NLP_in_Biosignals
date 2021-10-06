import wfdb
import numpy
import matplotlib, pandas
import neurokit2 as nk
from wfdb import plot
# File path
datafolder = r""
filename = ""
filepath = datafolder + filename

# Reading the record file and annotation
SAMPLES = 1000
annot = wfdb.rdann(filepath,"atr", sampto=SAMPLES)
record = wfdb.rdrecord(filepath, sampto=SAMPLES, channels = [0])
wave = record.__dict__["p_signal"][:,0]

SMLPRATE = record.fs
print(f"Sampling frequency is {SMLPRATE}")
# Plot wave
plot.plot_items(wave, ann_samp=[annot.sample], fs=SMLPRATE, time_units='seconds')

#Clean wave for R-peaks detection
cleanedwave = nk.ecg_clean(wave, SMLPRATE, "neurokit")

# Find R-peak
rs, info = nk.ecg_peaks(cleanedwave, SMLPRATE, "neurokit")

# Printing R-peaks coordinates in sec
print("Coordinates of R-peaks in second:")
for sample in info["ECG_R_Peaks"]:
    print(sample/SMLPRATE)
print("\n")
# Printing RR-intervals
print("Values of RR-intervals in second:")
prevsample = 0
for smpl in info["ECG_R_Peaks"]:
    nsmpl = smpl/SMLPRATE
    interval = nsmpl - prevsample
    print(interval)
    prevsample = nsmpl

