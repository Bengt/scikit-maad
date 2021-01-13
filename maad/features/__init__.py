# -*- coding: utf-8 -*-
""" 
Acoustic features
=================

The module ``features`` is an ensemble of functions to characterize audio signals using temporal and spectral features, and ecoacoustic indices.


Spectro-temporal features
-------------------------
.. autosummary::
    :toctree: generated/
    
    shape_features
    shape_features_raw
    opt_shape_presets
    filter_multires
    filter_bank_2d_nodc
    plot_shape
    overlay_centroid
    centroid_features
    all_shape_features

Alpha acoustic indices
----------------------
.. autosummary::
    :toctree: generated/
        
    audio_median
    audio_entropy
    acousticRichnessIndex
    audio_activity
    audio_events
    acousticComplexityIndex
    frequency_entropy
    numberOfPeaks
    spectral_entropy
    spectral_activity
    spectral_events
    spectral_cover
    soundscapeIndex
    bioacousticsIndex
    acousticDiversityIndex
    acousticEvenessIndex
    roughness
    audio_LEQ
    spectral_LEQ
    surfaceRoughness
    tfsd
    more_entropy
    acousticGradientIndex
    frequency_raoQ
    regionOfInterestIndex
    all_audio_alpha_indices
    all_spectral_alpha_indices

Temporal features
-----------------
.. autosummary::
    :toctree: generated/
    
    audio_moments
    zero_crossing_rate
    
Spectral features
-----------------
.. autosummary::
    :toctree: generated/
        
    spectral_moments

"""

from .shape import (filter_multires,
                          filter_bank_2d_nodc,
                          opt_shape_presets,
                          shape_features,
                          shape_features_raw,
                          plot_shape,
                          centroid_features,
                          overlay_centroid,
                          all_shape_features)

from .spectral import (spectral_moments)

from .temporal import (audio_moments,
                       zero_crossing_rate)

from .alpha_indices import (audio_median,
                            audio_entropy,
                            acousticRichnessIndex,
                            audio_activity,
                            audio_events,
                            acousticComplexityIndex,
                            frequency_entropy,
                            numberOfPeaks,
                            spectral_entropy,
                            spectral_activity,
                            spectral_events,
                            spectral_cover,
                            soundscapeIndex,
                            bioacousticsIndex,
                            acousticDiversityIndex,
                            acousticEvenessIndex,
                            roughness,
                            audio_LEQ,
                            spectral_LEQ,
                            surfaceRoughness,
                            tfsd,
                            more_entropy,
                            acousticGradientIndex,
                            frequency_raoQ,
                            regionOfInterestIndex,
                            all_audio_alpha_indices,
                            all_spectral_alpha_indices)

__all__ = [
           # shape
           'filter_multires', 
           'filter_bank_2d_nodc',
           'opt_shape_presets',
           'shape_features',
           'shape_features_raw',
           'plot_shape',
           'centroid_features',
           'overlay_centroid',
           'all_shape_features',
           # spectral
           'spectral_moments',
           # temporal
           'audio_moments',
           'zero_crossing_rate',
           # alpha_indices
           'audio_moments',
           'audio_median',
           'audio_entropy',
           'acousticRichnessIndex',
           "audio_activity",
           "audio_events",
           "acousticComplexityIndex",
           "frequency_entropy",
           "numberOfPeaks",
           "spectral_entropy",
           "spectral_moments",
           "spectral_activity",
           "spectral_events",
           'spectral_cover',
           "soundscapeIndex",
           'bioacousticsIndex',
           "acousticDiversityIndex",
           "acousticEvenessIndex",
           "roughness",
           'audio_LEQ',
           'spectral_LEQ',
           "surfaceRoughness",
           "tfsd",
           "more_entropy",
           "acousticGradientIndex",
           "frequency_raoQ",
           "regionOfInterestIndex",
           'all_audio_alpha_indices',
           'all_spectral_alpha_indices']