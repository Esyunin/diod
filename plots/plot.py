
# coding: utf-8

# In[27]:


from pylab import *
from scipy import interpolate
rc('text', usetex=True)
rc('text.latex',preamble = [
    r'\usepackage[russian]{babel}',
    r'\usepackage{amsmath}',
    r'\usepackage{amssymb}',
])
rc('font',family='serif',size = 14)
rc('axes',labelsize=22)
rc('figure',figsize=[10/2.5*4/3,10/2.5])
## Р’РђРҐ
U1 = array([0,0.1,0.15,0.2,0.26,0.3,0.34,0.36,0.38,0.4,0.44])
I1 = array([0,1,1,1,8,14,28,38,54,74,100])
U2 = array([0,2,10,20,30,40,50,60,70,80,90,100])/100
I2 = array([0,20,22,22,24,24,25,26,26,27,28,28])

f1=interpolate.interp1d(U1,I1,kind='quadratic')
f2=interpolate.interp1d(-U2,-I2,kind='linear')
figure()
color='darkblue'
U_0 = sort(hstack((-U2,U1)))
I_0 = sort(hstack((-I2,I1)))
plot(U_0,I_0, marker='o',label=r'$t=t_{\text{РєРѕРјРЅ}}$',color=color)
x = linspace(0,0.44,1000)
plot(x,f1(x),color=color)
x = linspace(-1,0,1000)
plot(x,f2(x),color=color)
xlabel(r'$U,\text{ Р’}$')
ylabel(r'$I,\text{ РјРђ}$')
# R = (100-38)/(0.44-0.36)
# print(R)
# y = log(I1[1:])
# x =U1[1:]
# fit = polyfit(x,y,1)
# phi = fit[0]**-1
# Is = 2.7**(fit[1])
# print('phi',phi,'\t','Is', Is)
# x = linspace(0,0.44,1000)
# y = Is*(exp(x/phi)-1)
# plot(x,y,'r')
# show()
U1 = array([0,0.1,0.2,0.3,0.36,0.38,0.4,0.42])
I1 = array([0,0,4,20,38,64,76,100])
U2 = array([0,2,10,20,30,40,50,60,70,80,90,100])/100
I2 = array([2,82,86,88,90,90,92,92,92,93,94,94])
U_0 = sort(hstack((-U2,U1)))
I_0 = sort(hstack((-I2,I1)))
xticks([-1,-0.8,-0.6,-0.4,-0.2,0,0.2,0.4],
        ['-100','-80','-60','-40','-20','0','0.2','0.4'])
yticks([-100,-80,-60,-40,-20,0,20,40,60,80,100],
        ['-0.1','-0.08','-0.06','-0.04','-0.02','0','20','40','60','80','100'])
plot(U_0,I_0,marker='x',label=r'$t \gg t_{\text{РєРѕРјРЅ}}$',color='red')
plot(U_0,I_0,'-',color='red',linestyle='dashed')
legend()
#savefig('/home/kannab/documents/diod/VAC.pdf',bbox_inches='tight')
show()

# figure()
# U = array([0,2,6,10,20,30,40,42])
# F = array([503.7,1241,1274,1282,1296,1307,1307,1307])
# plot(U,F,)

# xlabel(r'$U^{\text{РѕР±СЂ}},\text{ Р’}$')
# ylabel(r'$\nu^{\text{СЂРµР·}},\text{ РєР“С†}$')

# show()

