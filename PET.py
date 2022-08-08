#%%
import cv2
import numpy as np
import pydicom
import math
import copy
import matplotlib.pyplot as plt
import os
import pathlib
import glob
import dicom
from PIL import Image, ImageFilter
import pandas as pd
#%%
root_dir = r"C:\Users\shink\seki\PETdicomデータ\WB^1__WB1__20190416__Cardiac-Default\[DetailWB_CTAC_2mm_i3s12p]-FDG-WB-Constant_180sec__WHOLE-BODY__20190416__192203"
dcms = []
for d,s,fl in os.walk(root_dir):
    for fn in fl:
        dcms.append(os.path.join(d,fn))
ref_dicom=pydicom.dcmread(dcms[0])
d_array = np.zeros((ref_dicom.Rows, ref_dicom.Columns, len(dcms)), dtype=ref_dicom.pixel_array.dtype)
file_kazu=len(os.listdir(root_dir))
d=pathlib.Path(root_dir)
basyo=[]
for file_number in range(file_kazu):
    ds=list(d.iterdir())[file_number]
    da=pydicom.dcmread(ds)
    dm=da.SliceLocation
    basyo.append(dm)
zisyo=dict(zip(basyo,dcms))
zisyo2 =sorted(zisyo.items(),key=lambda x:x[0])
zisyo3=dict(zisyo2)
zisyo4=zisyo3.values()
list_1=list(zisyo4)



for dcm in list_1:
    d = pydicom.dcmread(dcm)
    Resslo=d.RescaleSlope
    Resint=d.RescaleIntercept

    d_array[:,:,list_1.index(dcm)] = d.pixel_array*Resslo+Resint
    

max0 = np.nanmax(d_array, axis=0)
max1=np.rot90(max0)
img=plt.figure(figsize=(8,8))