# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:40:33 2020

@author: Mani Chalasani
"""

import pandas as pd
import numpy as np
import os
import pyedflib
import mne

# read the file names into a list

files = os.listdir('C:/Users/Mani Chalasani/Documents/6250/Project/sleep-edf-database-expanded-1.0.0/sleep-telemetry')
to_add = 'C:/Users/Mani Chalasani/Documents/6250/Project/sleep-edf-database-expanded-1.0.0/sleep-telemetry/'
psg_files = sorted([to_add + file for file in files if 'PSG' in file])
hyp_files = sorted([to_add + file for file in files if 'Hypnogram' in file])
pairs = list(zip(psg_files,hyp_files))

L_edf=[]
L_hyp=[]

# converting EDF to csv using mne for psg files and pyedflib to access annotations from Hypnogram
for edf,hyp in pairs:
    try:
        pat_data = mne.io.read_raw_edf(edf)
        pat_data1 = pat_data.to_data_frame()
        label_data = pyedflib.EdfReader(hyp)
        ant_data = label_data.readAnnotations()
        sleep_stage = ant_data[2]
        sleep_stage = np.where((sleep_stage == 'Movement time') | (sleep_stage == 'Sleep stage ?'), 'Sleep stage W', sleep_stage)
        time_marks = ant_data[0]*1000 #balancing frequencies
        
        #Function to identify which time mark is accurate from PSG data point to integrate with annotations
        def time_index(time_list, time_marks, sleep_stage):
            label_list = []
            for time in time_list:
                index = -1
                for time_mark in time_marks:
                    if time >= time_mark:
                        index += 1
                    else:
                        break
                label_list.append(sleep_stage[index])
            return label_list

        time_list = list(pat_data1["time"])
        final_list = time_index(time_list, time_marks, sleep_stage)
        pat_data1['label'] = final_list
        pat_data1=pat_data1.rename(columns={'EEG Fpz-Cz':"val1","EEG Pz-Oz":"val2","EOG horizontal":"val3","EMG submental":"val4"})
        x=edf.split("/")[-1].split(".")[0]
        print(x)
        #saving the data to a csv
        pat_data1.to_csv(x+".csv")
    except:
        print("excepted")
        L_edf=L_edf+[edf]
        L_hyp=L_hyp+[hyp]
        pass
