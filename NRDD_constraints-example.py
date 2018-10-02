import numpy as np
import matplotlib.pyplot as pl
import NRDD_constraints as NR

## If the interaction between the DM particle, \chi, and the nucleon N=p,n is described by the relativistic operator, 
## Q=\bar{\chi} \gamma^{\mu}\chi \bar{\Psi}_N\gamma_{\mu}\gamma_5\Psi_N
## the non relativistic limit yields a linear combination of the operators O_7 and O_9:

## Q->  -2*O_7+2*m_N/mchi*O_9 = c_7*O_7_c_9*O_9
## so if the starting relativistic lagrangian is :
##
## L= c_rel Q
##
## with c_rel an effective constant of dimension -2 one has in the non-relativistic limit:
##
## L -> c_rel*c_7*O_7+c_rel*c_9*O_9
##
## Assuming dominance either of O_7 or O9 the routine NR.sigma_nucleon_bound returns for O_i a limit
## sigma_ref_N_i on the reference cross section sigma_ref_N_i:
##
## sigma_ref_N_i=max(sigma_ref^p_i,sigma_ref^n_i)=c_rel^2 *max[(c_i^n)^2,(c_i^p)^2]*mu^2/pi<sigma_ref_N_i_max
##
## so the bound on c_rel from O_i, written in terms of an analogous relativistic reference cross section
## sigma_ref_rel=c_rel^2*mu/pi  is given by:
##    
## sigma_ref_rel<sigma_ref_rel_i_max=c_rel^2*mu^2/pi<sigma_ref_N_i_max/max[(c_i^n)^2,(c_i^p)^2]
##
## so the bound on c_rel is given by min_i(sigma_ref_rel_i_max), i.e. is the most stringent bound on c_rel among the interactions ## O_i.


mn=0.931 #nucleon mass

mchi_values=np.logspace(np.log10(2.),np.log10(1000.),200)

sigma_lim_rel_vec=np.array([])

## defines the coefficients. Must take the largest between cp and cn because NR.sigma_nucleon_bound
## returns the limit on max(sigma_p,sigma_n)

def coeff(inter,mchi,r):
    if inter=='O7_O7':
        cp=-2.
        cn=cp*r

    elif inter=='O9_O9':
        cp=2.*mn/mchi
        cn=cp*r
        
    return max(abs(cp),abs(cn))

large_number=1e20
r=1
for mchi in mchi_values:

## initialization before minimization
    sigma_lim_rel_min=large_number 

##cycle on interactions, the most contraining one will be the limit on the relativistic couplings 
    for inter in ['O7_O7','O9_O9']:

## calculates max(abs(c_p),abs(c_n)) 
        c=coeff(inter,mchi,r)
## gets most constraining limit on max(sigma_p,sigma_n) in cm^2
        sigma_lim_nucleon_NR=NR.sigma_nucleon_bound(inter,mchi,r)

## converts the non-relativistic reference cross section to the relativistic one 
        sigma_lim_rel=sigma_lim_nucleon_NR/c**2 

## at fixed WIMP mass selects the most stringent bound among the interactions 'O7_O7' and 'O9_O9'
        if sigma_lim_rel<sigma_lim_rel_min:
            sigma_lim_rel_min=sigma_lim_rel

## saves the output and moves to next WIMP mass value
    sigma_lim_rel_vec=np.append(sigma_lim_rel_vec,sigma_lim_rel_min)

##plots the output using Matplotlib
pl.clf()
pl.xscale('log')
pl.yscale('log')
pl.plot(mchi_values,sigma_lim_rel_vec,'b-',linewidth=3)
pl.show()

## (hbar*c)^2 in GeV^2 * cm^2
hbarc2=0.389e-27 

## WIMP-nucleon reduced mass
mu=mchi_values*mn/(mchi_values+mn) 

## One can convert sigma_lim_rel into an upper bound on the effective scale, lambda_tilde_lim (in GeV) 
## dim=6 for a six dimensional operator 
dim=6

lambda_tilde_lim=(mu/np.sqrt(sigma_lim_rel_vec*np.pi/hbarc2))**(1./(dim-4))
 
## plots the output using Matplotlib
pl.clf()
pl.xscale('log')
pl.yscale('log')
pl.plot(mchi_values,lambda_tilde_lim,'b-',linewidth=3)
pl.xlim(0.1,1e3)
pl.ylim(1.,1e6)
pl.show()


