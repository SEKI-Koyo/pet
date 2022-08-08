#%%
import cv2
import numpy as np
import pydicom
import os
import pathlib
#%%
root_dir = r"C:\Users\shink\seki\PETdicomデータ\WB^1__WB1__20190416__Cardiac-Default\[DetailWB_CTAC_2mm_i3s12p]-FDG-WB-Constant_180sec__WHOLE-BODY__20190416__192203"
file_kazu=len(os.listdir(root_dir))
dirname = "tif"
if not os.path.exists(dirname):
    os.mkdir(dirname)
dcm_path=pathlib.Path(root_dir)
basyo=[]
dcms = []
for d,s,fl in os.walk(root_dir):
    for fn in fl:
        dcms.append(os.path.join(d,fn))
for file_number in range(file_kazu):
    ds=list(dcm_path.iterdir())[file_number]
    da=pydicom.dcmread(ds)
    dm=da.SliceLocation
    basyo.append(dm)
zisyo=dict(zip(basyo,dcms))
zisyo2 =sorted(zisyo.items(),key=lambda x:x[0])
zisyo3=dict(zisyo2)
zisyo4=zisyo3.values()
list_1=list(zisyo4)
cou = 0
for dcm in list_1:
    cou+=1
    ds=dcm
    da=pydicom.dcmread(ds)
    cv2.imwrite(os.path.join(dirname,"out_TIFF"+str(cou)+".tif"),da.pixel_array)
# %%
