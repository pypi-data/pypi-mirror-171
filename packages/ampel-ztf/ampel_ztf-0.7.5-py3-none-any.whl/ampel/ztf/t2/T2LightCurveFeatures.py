#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : Ampel-ZTF/ampel/ztf/t2/T2LightCurveFeatures.py
# License           : BSD-3-Clause
# Author            : Jakob van Santen <jakob.van.santen@desy.de>
# Date              : 15.04.2021
# Last Modified Date: 15.04.2021
# Last Modified By  : Jakob van Santen <jakob.van.santen@desy.de>

from typing import Any, Dict, List, Optional

import numpy as np
import light_curve

from ampel.abstract.AbsLightCurveT2Unit import AbsLightCurveT2Unit
from ampel.type import T2UnitResult
from ampel.view.LightCurve import LightCurve


class T2LightCurveFeatures(AbsLightCurveT2Unit):
    """
    Calculate various features of the light curve using the light-curve
    package described in https://ui.adsabs.harvard.edu/abs/2021MNRAS.502.5147M%2F/abstract
    """

    #: Features to extract from the light curve.
    #: See: https://docs.rs/light-curve-feature/0.2.2/light_curve_feature/features/index.html
    features: Dict[str, Optional[Dict[str, Any]]] = {
        "InterPercentileRange": {"quantile": 0.25},
        "LinearFit": None,
        "StetsonK": None,
    }
    #: Bandpasses to use
    bands: Dict[int, str] = {1: "g", 2: "r", 3: "i"}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.extractor = light_curve.Extractor(
            *(getattr(light_curve, k)(**(v or {})) for k, v in self.features.items())
        )

    def run(self, lightcurve: LightCurve) -> T2UnitResult:
        result = {}
        for fid, band in self.bands.items():
            if (
                in_band := lightcurve.get_ntuples(
                    ["jd", "magpsf", "sigmapsf"],
                    {"attribute": "fid", "operator": "==", "value": fid},
                )
            ) is None:
                continue
            t, mag, magerr = np.array(sorted(in_band)).T

            try:
                result.update(
                    {
                        f"{k}_{band}": v
                        for k, v in zip(
                            self.extractor.names, self.extractor(t, mag, magerr)
                        )
                    }
                )
            except ValueError:
                # raised if too few points
                ...
        return result
