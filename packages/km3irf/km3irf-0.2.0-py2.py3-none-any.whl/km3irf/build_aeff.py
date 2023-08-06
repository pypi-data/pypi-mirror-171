#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import awkward as ak
import pandas as pd
import uproot as ur
from km3io import OfflineReader

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

from astropy.io import fits
import astropy.units as u

# from gammapy.irf import EnergyDispersion2D

from scipy.stats import binned_statistic

# from scipy.ndimage import gaussian_filter1d, gaussian_filter


# from collections import defaultdict

# import sys
# sys.path.append('../')
# from python_scripts.irf_utils import aeff_2D, psf_3D
# from python_scripts.func import get_cut_mask
# from python_scripts.func import WriteAeff
# from python_scripts.func import WritePSF


def build_aeff(
    input=(file_nu, file_nubar), 
    no_bdt=False, 
    cuts=True, 
    weight_factor=-2.5
):
    """
    Create Aeff .fits from dist files

    input: a tuple with pathes to nu_dst file and nubar_dst file

    no_bdt: include or exclude bdt, default False

    cuts: apply cuts, default True

    weight_factor: re-weight data, default value  -2.5

    """

    # Read data files using km3io
    f_nu_km3io = OfflineReader(input[0])
    f_nubar_km3io = OfflineReader(input[1])

    # Read data files using uproot
    f_nu_uproot = ur.open(input[0])
    f_nubar_uproot = ur.open(input[1])

    df_nu = unpack_data(no_bdt, "nu", f_nu_km3io, f_nu_uproot)
    df_nubar = unpack_data(no_bdt, "nubar", f_nubar_km3io, f_nubar_uproot)

    alpha_value = f_nu_km3io.header.spectrum.alpha

    if cuts:
        mask_nu = get_cut_mask(df_nu.bdt0, df_nu.bdt1, df_nu.dir_z)
        df_nu_cut = df_nu[mask_nu].copy()
        mask_nubar = get_cut_mask(df_nubar.bdt0, df_nubar.bdt1, df_nubar.dir_z)
        df_nubar_cut = df_nubar[mask_nubar].copy()

        # calculate the normalized weight factor for each event
        weights = dict()
        for l, df in zip(['nu', 'nubar'], [df_nu_cut, df_nubar_cut]):
            weights[l] = (df.energy_mc**(weight_factor - alpha_value)).to_numpy()
            weights[l] *= len(df) / weights[l].sum()

    


def unpack_data(no_bdt, type, km3io_file, uproot_file):
    """
    retrieve information from data and pack it to DataFrame

    type: "nu" or "nubar"

    km3io_file: input km3io file

    uproot_file: input uproot file 

    return pandas data frame for specific type
    """
    # Access data arrays
    data_km3io = dict()

    # for l, f in zip(["nu", "nubar"], [f_nu_km3io, f_nubar_km3io]):
    data_km3io[type] = dict()

    data_km3io[type]["E"] = km3io_file.tracks.E[:, 0]
    data_km3io[type]["dir_x"] = km3io_file.tracks.dir_x[:, 0]
    data_km3io[type]["dir_y"] = km3io_file.tracks.dir_y[:, 0]
    data_km3io[type]["dir_z"] = km3io_file.tracks.dir_z[:, 0]

    data_km3io[type]["energy_mc"] = km3io_file.mc_tracks.E[:, 0]
    data_km3io[type]["dir_x_mc"] = km3io_file.mc_tracks.dir_x[:, 0]
    data_km3io[type]["dir_y_mc"] = km3io_file.mc_tracks.dir_y[:, 0]
    data_km3io[type]["dir_z_mc"] = km3io_file.mc_tracks.dir_z[:, 0]

    data_km3io[type]["weight_w2"] = km3io_file.w[:, 1]

    # extracting bdt information
    if not no_bdt:
        # for l, f in zip(["nu", "nubar"], [f_nu_uproot, f_nubar_uproot]):
        T = uproot_file["T;1"]
        bdt = T["bdt"].array()
        data_km3io[type]["bdt0"] = bdt[:, 0]
        data_km3io[type]["bdt1"] = bdt[:, 1]

    # create Data Frames
    df_data = pd.DataFrame(data_km3io[type])
    # df_nubar = pd.DataFrame(data_km3io["nubar"])

    # data_tuple = (df_nu, df_nubar)

    return df_data

def get_cut_mask(bdt0, bdt1, dir_z):
    """
    
    bdt0: to determine groups to which BDT cut should be applied (upgoing/horizontal/downgoing)

    bdt1: BDT score in the range [-1, 1]. Closer to 1 means more signal-like

    dir_z: is the reconstructed z-direction of the event

    return a mask for set cuts
    """

    mask_down = bdt0 >= 11  # remove downgoing events
    clear_signal = bdt0 == 12 # very clear signal
    loose_up = (np.arccos(dir_z)*180/np.pi < 80) & (bdt1 > 0.) # apply loose cut on upgoing events
    strong_horizontal = (np.arccos(dir_z)*180/np.pi > 80) & (bdt1 > 0.7) # apply strong cut on horizontal events
    
    return mask_down & ( clear_signal | loose_up | strong_horizontal )
