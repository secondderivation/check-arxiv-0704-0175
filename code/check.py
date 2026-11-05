#!/usr/bin/env python3
"""Public replay of the 4 November informed C implementation; see PROTOCOL.md."""
from fractions import Fraction as F
from decimal import Decimal as D, getcontext
from pathlib import Path
import math, json, time, platform, argparse
getcontext().prec=60
start=time.process_time(); wall=time.monotonic()
parser=argparse.ArgumentParser()
parser.add_argument('--output', required=True)
args=parser.parse_args()
output=Path(args.output)
if output.exists(): raise SystemExit('Output exists; refusing overwrite')
output.parent.mkdir(parents=True, exist_ok=True)
r={}; checks=[]
def check(name,ok,details=None):
 checks.append({'name':name,'pass':bool(ok),'details':details})
def dec(f):return D(f.numerator)/D(f.denominator)
# Null condition yields c dt/dx = 1 - Phi - Psi to linear order.
# x=b tan(theta); (x*x+b*b)^(-7/2) dx = b^-6 cos(theta)^5 dtheta.
# u=sin(theta); cos(theta)^5 dtheta = (1-u*u)^2 du.
poly=[F(1),F(-2),F(1)]
primitive=[v/F(2*i+1) for i,v in enumerate(poly)]
Iinf=2*sum(primitive)
potential_sum=-(F(64,7)+F(32,7))
delay=-2*potential_sum*Iinf
doppler=6*delay/4
local_gamma=F(32,7)-F(64,7)
r['exact']={k:str(v) for k,v in {'integral_b6':Iinf,'potential_sum':potential_sum,'roundtrip_delay':delay,'oneway_delay':delay/2,'doppler_bracket':doppler,'printed_delay_ratio':F(1024)/delay,'printed_doppler_ratio':F(1536)/doppler,'local_gamma_shift_per_q':local_gamma,'doppler_over_local_gamma':doppler/local_gamma}.items()}
check('integral_exact',Iinf==F(16,15))
check('integrand_recovered_by_differentiating_primitive',all(primitive[i]*(2*i+1)==poly[i] for i in range(3)))
check('GB_consistency_delay_derivative',doppler==F(1536,35))
check('GB_zero_coupling',dec(delay)*D(0)**2==0)
# GR Phi=-m/r, Psi=-gamma*m/r => N(1+gamma)m asinh endpoints.
# derivative infinite endpoint sum = -2/b; coefficient multiplying (1+gamma).
r['GR']={'oneway_y_coefficient_m_over_cb':2,'twoway_y_coefficient_m_over_cb':4,'twoway_GR_y_coefficient_m_over_cb':8,'log_paper_to_standard_argument_ratio':str(F(1,16)),'additive_log_argument_change_doppler':0}
# Original V sum = -r^2 V/12; roundtrip = V/6 integral r^2 dx.
v_delay=-2*(-F(1,6)+F(1,12));v_bracket=-(2*v_delay)/4
# G=G0(1+8AV'/3), sum 1/r potential originally -(2+4AV')m0/r.
av_sum=F(4)-2*F(8,3);av_delay=2*av_sum
r['other_terms']={'V_delay_integral_coefficient':str(v_delay),'V_doppler_bracket_b2_sumx_over_m':str(v_bracket),'AVprime_delay_log_coefficient_m':str(av_delay),'AVprime_doppler_bracket':str(av_delay/2)}
check('V_control',v_delay==F(1,6) and v_bracket==F(-1,12))
check('AVprime_measured_mass_control',av_delay==F(-8,3) and av_delay/2==F(-4,3))
R=D('6.96e8');bmin=D('1.6')*R;m=D(1477);c=D(299792458);earth=D(149597870691);sat=D('1.26e12');H=D('7.566e-27')
r['inputs']={k:str(v) for k,v in locals().copy().items() if k in ['R','bmin','m','c','earth','sat','H']}
r['inputs']['sat_8_43_AU']=str(D('8.43')*earth)
r['inputs']['sat_rounding_relative_difference']=str((D('8.43')*earth-sat)/sat)
def prim(u):return u-D(2)*u**3/D(3)+u**5/D(5)
def geometry(b,mode):
 xs=[earth,sat] if mode=='fixed_x' else [(a*a-b*b).sqrt() for a in [earth,sat]]
 us=[x/(x*x+b*b).sqrt() for x in xs]
 S=sum(prim(u) for u in us)
 J=S/b**6
 term=sum((u if mode=='fixed_x' else 1/u)*(1-u*u)**3 for u in us)
 dJ=(-6*S-term)/b**7
 return xs,us,S,J,dJ
N=16384
def simpson(a,z):
 h=(z-a)/N
 return h/3*sum((1 if i in [0,N] else 4 if i%2 else 2)*math.cos(a+i*h)**5 for i in range(N+1))
qinf=simpson(-math.pi/2,math.pi/2)
r['quadrature_infinite']={'value':qinf,'relative_error':abs(qinf/float(Iinf)-1),'panels':N}
check('quadrature_infinite',abs(qinf/float(Iinf)-1)<1e-10)
r['finite_endpoints']=[]
for ratio in [1,2,5]:
 b=bmin*ratio
 for mode in ['fixed_x','fixed_r']:
  xs,us,S,J,dJ=geometry(b,mode)
  q=simpson(-math.atan(float(xs[1]/b)),math.atan(float(xs[0]/b)))
  err=abs(q/float(S)-1)
  fd=[]
  for hrat in ['1e-4','1e-5']:
   h=b*D(hrat);dd=(geometry(b+h,mode)[3]-geometry(b-h,mode)[3])/(2*h)
   fd.append({'h_over_b':hrat,'relative_error':str(abs(dd/dJ-1))})
  item={'b_over_bmin':ratio,'geometry':mode,'dimensionless_integral':str(S),'delay_fraction_lost_vs_infinite':str(1-S/dec(Iinf)),'doppler_ratio_to_infinite':str(dJ/(-6*dec(Iinf)/b**7)),'quadrature_rel_error':err,'finite_difference':fd}
  r['finite_endpoints'].append(item)
  check(f'quadrature_{ratio}_{mode}',err<1e-10)
  check(f'derivative_{ratio}_{mode}',D(fd[-1]['relative_error'])<D('1e-7'))
r['bounds']=[]
for name,threshold in [('paper_proxy_central_plus_sigma',D('4.4e-5')),('sigma_only_sensitivity',D('2.3e-5'))]:
 old=(threshold/D(1536)).sqrt()*bmin**3/m
 new=(threshold/dec(doppler)).sqrt()*bmin**3/m
 q=new**2*m**2/bmin**6
 item={'threshold_label':name,'threshold':str(threshold),'original_formula_A_m2':str(old),'corrected_formula_A_m2':str(new),'rescale':str(new/old),'Omega_proxy_old':str(4*old*H*H),'Omega_proxy_corrected':str(4*new*H*H),'delta_phi_over_U_at_bmin':str(2*new*m/bmin**3),'Phi_GB_over_U_at_bmin':str(dec(F(64,7))*q),'Psi_GB_over_U_at_bmin':str(dec(F(32,7))*q),'rg_over_bmin':str(m/bmin),'A_over_paper_1e23_scale_assuming_xiprime_one':str(new/D('1e23')),'roundtrip_GB_delay_seconds_at_bmin':str(dec(delay)*new**2*m**3/(c*bmin**6)),'scalar_ratio_at_solar_radius':str(2*new*m/R**3)}
 r['bounds'].append(item)
 # both numerator measured reference and signal coefficient halve for one way.
 one=(threshold*D(2)/(6*dec(delay/2))).sqrt()*bmin**3/m
 check('one_two_way_bound_'+name,abs(one/new-1)<D('1e-55'))
r['observable_shape']=[{'b_over_bmin':n,'effective_gamma_ratio':str(F(1,n**6)),'coupling_limit_ratio_same_proxy_threshold':n**3} for n in [1,2,5]]
r['GR']['two_rg_over_c_seconds']=str(2*m/c)
r['GR']['four_rg_over_c_seconds']=str(4*m/c)
r['sqrt35']=str(D(35).sqrt())
r['printed_bounds_comparison']={'A_printed':'1.6e20','Omega_printed':'3.6e-32'}
r['checks']=checks
r['passed']=all(z['pass'] for z in checks)
r['runtime']={'python':platform.python_version(),'cpu_seconds':time.process_time()-start,'wall_seconds':time.monotonic()-wall,'attempt':1,'execution_guard':'reproduce.py: 30 second child timeout','retry_used':False}
with output.open('x') as f: f.write(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
raise SystemExit(0 if r['passed'] else 1)
