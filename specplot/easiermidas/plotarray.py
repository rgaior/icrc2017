import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
file = 'StationGPSCoordinates.dat'
pos = pd.read_table(file,sep=" ",names=['id','y','x','z'])
listid_gdc = np.array([384,385,422,427,431,432,433])
listid_gdl = np.array([313,328,329,330,334,339,340])
listid_ea61 = np.array([306,308,315,328,334,403,408,
                        425,434,354,125,199,
                        300,307,310,311, 356,375,383,394,405,410,
                        121,196,197,201,296,
                        305,312,319,325,329,337,340,
                        376,386,387,390,396,412,
                        429,438,441,1802,332,333,
                        341,342,343,344,419])

posea61  = pos.loc[pos['id'].isin(listid_ea61)]
poseagdc  = pos.loc[pos['id'].isin(listid_gdc)]
poseagdl  = pos.loc[pos['id'].isin(listid_gdl)]

fig = plt.figure(figsize=(6,5))

plt.plot(pos.x,pos.y,'o',markersize=2,alpha=0.5,label='Auger SD')
plt.plot(posea61.x,posea61.y,'o',markersize=4,label = 'EASIER61')
plt.plot(poseagdc.x,poseagdc.y,'o',markersize=4,label = 'GIGADuck-C')
plt.plot(poseagdl.x,poseagdl.y,'o',markersize=4,label = 'GIGADuck-L')
xm = 459000
ym = 6072000
xa = 468500
ya = 6129500
xb = 450200
yb = 6122500

plt.plot(np.array([xm,xa]),np.array([ym,ya]),'b--',lw=2, label='MIDAS FOV')
plt.plot(np.array([xm,xb]),np.array([ym,yb]),'b--',lw=2)
plt.xlabel('X position')
plt.ylabel('Y position')
xlabels = plt.gca().get_xticklabels()
plt.setp(xlabels, rotation=30, fontsize=10)
ylabels = plt.gca().get_yticklabels()
plt.setp(ylabels, rotation=30, fontsize=10)
fig.tight_layout()
plt.legend()
plt.savefig('layoutGHz.png')
plt.show()
