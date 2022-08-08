#%%
import numpy as np
import pydicom
# %%
root_dir = r"C:\Users\shink\seki\PETdicomデータ\WB^1__WB1__20190416__Cardiac-Default\[DetailWB_CTAC_2mm_i3s12p]-FDG-WB-Constant_180sec__WHOLE-BODY__20190416__192203\1.3.46.670589.50.2.7309261776349761.290761756312982890"
d = pydicom.dcmread(root_dir)
dcm_arr=d.pixel_array
dcm_arr = np.max(dcm_arr)
wei=d.PatientWeight*1000
rad=d[0x54,0x16].value[0][0x18,0x1074].value
hosei=rad*((1/2)**((3599/d[0x54,0x16].value[0][0x18,0x1075].value)))
suv=dcm_arr/(hosei/wei)
print(suv)