# NRDD-constraints : A python module for calculating the exclusion plot for Dark Matter interactions with the Standard Model in non-relativistic Effective Theory Model. 

<code> NRDD-constraints</code> tool provides simple interpolating function written in python
for a given generalized non-relativistic (NR) term among those listed in Table 2 of [arXiv: 1809.XXXXX](https://arxiv.org/). The package contains three files:

* The code, **NR_DD_constraints.py** 
* A simple driver, **NR_DD_constraints_example.py**
* A data file, **all_nr_interactions_planes.npy**

You can get the latest version of <code> NRDD-constraints</code> from [github](https://github.com/NRDD-constraints/NRDD).

# Installation

The module can be downloaded from [https://github.com/NRDD-constraints/NRDD/archive/master.zip](https://github.com/NRDD-constraints/NRDD/archive/master.zip) or cloned by,

<code> git clone https://github.com/NRDD-constraints/NRDD </code>

# Usage

Here is a simple example for using NRDD constraints:

Import the package:

<code> import NR_DD_constraints as NR </code>

This defines two functions:

<code> sigma_p_bound(**int, mchi, r**) </code> which calculates cross-section as a function of the wimp mass 
mchi and of the ratio (DM-neutron to DM-proton couplings) r in the ranges 0.1 GeV < mchi < 100 GeV, -10000 < r < 10000.

The <code> **int** </code> parameter is a string that selects the interaction term
and can be chosen in the list provided by second function <code> print_interactions() </code>.

<code> NR.print_interactions()</code> gives the possible interactions.

['O12_O12', 'O6_O6_qm4', 'O14_O14', 'O7_O7', 'O4_O4',
'O13_O13', 'O5_O5', 'O8_O8', 'O11_O11', 'O9_O9',
'O3_O3', 'O5_O5_qm4', 'O10_O10', 'O11_O11_qm4',
'O6_O6', 'O1_O1', 'O15_O15'] 

The output of <code> sigma_p_bound(**int, mchi, r**) </code> corresponds to the results of 
[1805.06113](https://arxiv.org/abs/1805.06113) (updated to
the latest XENON1T bound) with the exception of the interaction terms with momentum
dependence in the Wilson coefficient. 

# Citation

If you use <code> NRDD constraints code </code> please cite the following papers: [arXiv: 1809.XXXXX](https://arxiv.org/),
[1805.06113](https://arxiv.org/abs/1805.06113)

# Authors

* Stefano Scopel (Sogang University)
* Gaurav Tomar (Sogang University)
* Jong–Hyun Yoon (Sogang University)
* Sunghyun Kang (Sogang University)

# License

<code> NRDD constraints code </code> is distributed under the MIT license.
