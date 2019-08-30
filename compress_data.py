from nilearn.input_data import NiftiMasker
from glob import glob
import numpy as np
import os

mask = "embedding/cortex_mask_25um.nii.gz"
func = glob("embedding/orig/*MEDISO*EPI*.nii.gz")
print(func)

masker = NiftiMasker(mask_img=mask, standardize=True)

for f in func:
    func_compressed = masker.fit_transform(f)
    np.save('embedding/compressed/%s.npy'
            % os.path.basename(f).split(".")[0], func_compressed)

    print(f)
