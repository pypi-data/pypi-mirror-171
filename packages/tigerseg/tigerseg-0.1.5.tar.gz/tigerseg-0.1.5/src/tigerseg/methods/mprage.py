import glob
from os.path import join, basename, isdir
import os
import numpy as np
from scipy.io import savemat
import nibabel as nib
import onnxruntime as ort
from scipy.special import softmax
from skimage import transform
from nilearn.image import reorder_img, resample_to_img, resample_img

labels = (2,3,4,5,7,8,10,11,12,13,14,15,16,17,18,24,26,28,30,31,41,42,43,44,46,47,49,50,51,52,53,54,58,60,62,63,77,85,251,252,253,254,255)
nib.Nifti1Header.quaternion_threshold = -100


def get_affine(mat_size=256):

    target_shape = np.array((mat_size, mat_size, mat_size))
    new_resolution = [256/mat_size, ]*3
    new_affine = np.zeros((4, 4))
    new_affine[:3, :3] = np.diag(new_resolution)
    # putting point 0,0,0 in the middle of the new volume - this could be refined in the future
    new_affine[:3, 3] = target_shape*new_resolution/2.*-1
    new_affine[3, 3] = 1.
    #print(model_ff, target_shape)
    return new_affine, target_shape
'''
def get_resample(input_file, matrix=128):

    target_affine = [  [  1,  0,  0,  -94], [  0,  1,  0, -111],
                [  0,  0,  1, -147], [  0,  0,  0,    1]]
    
    target_affine = np.array(target_affine)
    target_shape = [192, 256, 256]

    return target_affine, target_shape
'''
def run_SingleModel(model_ff, input_data, GPU):

    seg_mode, model_str = basename(model_ff).split('_')[2:4] #aseg43, bet  

    data = input_data.copy()

    if 'r128' in model_str:
        data = transform.resize(data, (128, 128, 128),
                                preserve_range=True)
    elif 'r256' in model_str:
        pass

    image = data[None, ...][None, ...]
    image = image/np.max(image)

    logits = predict(model_ff, image, GPU)[0, ...]

    label_num = dict()
    label_num['bet'] = 2
    label_num['aseg43'] = 44

    if label_num[seg_mode] > logits.shape[0]:
        #sigmoid mode
        mask_pred = np.argmax(logits, axis=0) + 1
        mask_pred[np.max(logits, axis=0) < 0.5] = 0
        prob = logits
    else:
        #softmax mode
        mask_pred = np.argmax(logits, axis=0)
        prob = softmax(logits, axis=0)

    if seg_mode == 'aseg43':

        mask_pred_relabel = mask_pred * 0
        for ii in range(len(labels)):
            mask_pred_relabel[mask_pred == (ii + 1)] = labels[ii]

        mask_pred = mask_pred_relabel

    mask_pred = transform.resize(mask_pred, input_data.shape,
                                    order=0, preserve_range=True)

   
    return mask_pred.astype(np.uint8), prob


def read_file(model_ff, input_file):

    affine, shape = get_affine(mat_size=256)
    vol = resample_img(nib.load(input_file), target_affine=affine, target_shape=shape).get_fdata()
    #vol = resample_to_img(nib.load(input_file), nib.load(r"C:\expdata\nchu_cine\template256.nii.gz")).get_fdata()
    return vol 


def write_file(model_ff, input_file, output_dir, mask):

    if not isdir(output_dir):
        print('Output dir does not exist.')
        return 0

    output_file = basename(input_file).replace('.nii.gz', '').replace('.nii', '') 
    output_file = output_file + '_pred.nii.gz'
    output_file = join(output_dir, output_file)
    print('Writing output file: ', output_file)

    input_nib = nib.load(input_file)
    affine = input_nib.affine
    zoom = input_nib.header.get_zooms()
    
    target_affine, _ = get_affine(mat_size=256)
    #result = nib.Nifti1Image(mask.astype(np.uint8), reorder_img(input_nib, resample='linear').affine)
    result = nib.Nifti1Image(mask.astype(np.uint8), target_affine)

    
    result = resample_to_img(result, input_nib, interpolation="nearest")
    result.header.set_zooms(zoom)

    nib.save(result, output_file)

    return output_file


def predict(model, data, GPU):

    so = ort.SessionOptions()
    so.intra_op_num_threads = 4
    so.inter_op_num_threads = 4

    if GPU and (ort.get_device() == "GPU"):
        #ort.InferenceSession(model_file, providers=['CPUExecutionProvider'])
        session = ort.InferenceSession(model,
                                       providers=['CUDAExecutionProvider'],
                                       sess_options=so)
    else:
        session = ort.InferenceSession(model,
                                       providers=['CPUExecutionProvider'],
                                       sess_options=so)
    data_type = 'float64'
    if session.get_inputs()[0].type == 'tensor(float)':
        data_type = 'float32'  

    return session.run(None, {session.get_inputs()[0].name: data.astype(data_type)}, )[0]




