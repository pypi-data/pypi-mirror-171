# findpeaks

[![Python](https://img.shields.io/pypi/pyversions/findpeaks)](https://img.shields.io/pypi/pyversions/findpeaks)
[![PyPI Version](https://img.shields.io/pypi/v/findpeaks)](https://pypi.org/project/findpeaks/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/findpeaks/blob/master/LICENSE)
[![Github Forks](https://img.shields.io/github/forks/erdogant/findpeaks.svg)](https://github.com/erdogant/findpeaks/network)
[![GitHub Open Issues](https://img.shields.io/github/issues/erdogant/findpeaks.svg)](https://github.com/erdogant/findpeaks/issues)
[![Project Status](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![Downloads](https://pepy.tech/badge/findpeaks)](https://pepy.tech/project/findpeaks)
[![Downloads](https://pepy.tech/badge/findpeaks/month)](https://pepy.tech/project/findpeaks/month)
[![DOI](https://zenodo.org/badge/260400472.svg)](https://zenodo.org/badge/latestdoi/260400472)
[![Sphinx](https://img.shields.io/badge/Sphinx-Docs-Green)](https://erdogant.github.io/findpeaks/)
<!---[![BuyMeCoffee](https://img.shields.io/badge/buymea-coffee-yellow.svg)](https://www.buymeacoffee.com/erdogant)-->
<!---[![Coffee](https://img.shields.io/badge/coffee-black-grey.svg)](https://erdogant.github.io/donate/?currency=USD&amount=5)-->

The library ``findpeaks`` aims to detect peaks in a 1-dimensional vector and 2-dimensional arrays (images) without making any assumption on the peak shape or baseline noise. To make sure that peaks can be detected across global and local heights, and in noisy data, multiple pre-processing and denoising methods are implemented.


# 
**⭐️ Star this repo if you like it ⭐️**
#

#### Install findpeaks from PyPI

```bash
pip install findpeaks
```

#### Import findpeaks package

```python
from findpeaks import findpeaks
```
# 


### [Documentation pages](https://erdogant.github.io/findpeaks/)

On the [documentation pages](https://erdogant.github.io/findpeaks/) you can find detailed information about the working of the ``findpeaks`` with many examples. 

# 

### Examples

* [Example: Find peaks in 1D-vector with low number of samples](https://erdogant.github.io/findpeaks/pages/html/Examples.html#find-peaks-in-low-sampled-dataset)

<p align="left">
  <a href="https://erdogant.github.io/findpeaks/pages/html/Examples.html#find-peaks-in-low-sampled-dataset">
  <img src="https://github.com/erdogant/findpeaks/blob/master/docs/figs/fig1_raw.png" width="400" />
  <img src="https://github.com/erdogant/findpeaks/blob/master/docs/figs/fig1_interpol.png" width="400" />  
  </a>
</p>


#

* [Example: Comparison peak detection methods](https://erdogant.github.io/findpeaks/pages/html/Examples.html#comparison-methods-1)

<p align="left">
  <a href="https://erdogant.github.io/findpeaks/pages/html/Examples.html#comparison-methods-1">
  <img src="https://github.com/erdogant/findpeaks/blob/master/docs/figs/fig2_peakdetect_int.png" width="400" />  
  <img src="https://github.com/erdogant/findpeaks/blob/master/docs/figs/fig2_topology_int.png" width="400" />    
  </a>
</p>

#

* [Example: Find peaks in 1D-vector with high number of samples](https://erdogant.github.io/findpeaks/pages/html/Examples.html#find-peaks-in-high-sampled-dataset)

<p align="left">
  <a href="https://erdogant.github.io/findpeaks/pages/html/Examples.html#find-peaks-in-high-sampled-dataset">
  <img src="https://github.com/erdogant/findpeaks/blob/master/docs/figs/fig3.png" width="600" />
  </a>
</p>

<p align="left">
  <a href="https://erdogant.github.io/findpeaks/pages/html/Examples.html#find-peaks-in-high-sampled-dataset">
  <img src="https://github.com/erdogant/findpeaks/blob/master/docs/figs/fig3_persistence_limit.png" width="600" />
  </a>
</p>

#

* [Example: Find peaks in an image (2D-array)](https://erdogant.github.io/findpeaks/pages/html/Examples.html#d-array-image)

<p align="left">
  <a href="https://erdogant.github.io/findpeaks/pages/html/Examples.html#d-array-image">
 <img src="https://github.com/erdogant/findpeaks/blob/master/docs/figs/2dpeaks_raw.png" width="115" />
 <img src="https://github.com/erdogant/findpeaks/blob/master/docs/figs/2dpeaks_mask.png" width="500" />
  </a>
</p>

* [Example: Conversion from 2d to 3d mesh plot)](https://erdogant.github.io/findpeaks/pages/html/Plots.html#d-mesh)

<p align="left">
  <a href="https://erdogant.github.io/findpeaks/pages/html/Plots.html#d-mesh">
  <img src="https://github.com/erdogant/findpeaks/blob/master/docs/figs/2dpeaks_mesh1.png" width="400" />
  <img src="https://github.com/erdogant/findpeaks/blob/master/docs/figs/2dpeaks_mesh2.png" width="400" />
  </a>
</p>


#

* [Example: Find peaks and valleys in stockmarkets (Bitcoin)](https://erdogant.github.io/findpeaks/pages/html/Use-cases.html#bitcoin)
* [Example: Find peaks and valleys in stockmarkets (Facebook)](https://erdogant.github.io/findpeaks/pages/html/Use-cases.html#facebook-stocks)

<p align="left">
  <a href="https://erdogant.github.io/findpeaks/pages/html/Use-cases.html#facebook-stocks">
  <img src="https://github.com/erdogant/findpeaks/blob/master/docs/figs/fig_facebook_minperc5.png" width="600" />
  </a>
</p>

#

* [Example: Find peaks in SAR/SONAR images)](https://erdogant.github.io/findpeaks/pages/html/Use-cases.html#sonar)

<p align="left">
  <a href="https://erdogant.github.io/findpeaks/pages/html/Use-cases.html#sonar">
  <img src="https://github.com/erdogant/findpeaks/blob/master/docs/figs/sonar_plot.png" width="600" />
  </a>
</p>


<p align="left">
  <a href="https://erdogant.github.io/findpeaks/pages/html/Use-cases.html#sonar">
  <img src="https://github.com/erdogant/findpeaks/blob/master/docs/figs/sonar_mesh1.png" width="300" />
  <img src="https://github.com/erdogant/findpeaks/blob/master/docs/figs/sonar_mesh2.png" width="300" />
  </a>
</p>

<p align="left">
  <a href="https://erdogant.github.io/findpeaks/pages/html/Use-cases.html#sonar">
  <img src="https://github.com/erdogant/findpeaks/blob/master/docs/figs/sonar_mesh3.png" width="300" />
  <img src="https://github.com/erdogant/findpeaks/blob/master/docs/figs/sonar_mesh4.png" width="300" />
  </a>
</p>


#

* [Example: Denoising images using Lee, Kuan, Fastnl, Bilateral, Frost, Mean, median)](https://erdogant.github.io/findpeaks/pages/html/Denoise.html#)

<p align="left">
  <a href="https://erdogant.github.io/findpeaks/pages/html/Denoise.html#">
  <img src="https://github.com/erdogant/findpeaks/blob/master/docs/figs/noise_distr_examples.png" width="600" />
  </a>
</p>


<hr> 


### References
* https://github.com/erdogant/findpeaks
* https://github.com/Anaxilaus/peakdetect
* https://www.sthu.org/blog/13-perstopology-peakdetection/index.html


### Contribute
* All kinds of contributions are welcome!

### Citation
Please cite ``findpeaks`` in your publications if this is useful for your research. See column right for citation information.

### Maintainer
* Erdogan Taskesen, github: [erdogant](https://github.com/erdogant)
* Contributions are welcome.
* If you wish to buy me a <a href="https://erdogant.github.io/donate/?currency=USD&amount=5">Coffee</a> for this work, it is very appreciated :)
