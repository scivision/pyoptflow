try:
    from matplotlib.pyplot import figure,subplots,draw,pause,gca,show
except (ImportError,RuntimeError):
    figure=None

def plotderiv(fx,fy,ft):
    if figure is None:
        return

    fg,ax = subplots(1,3,figsize=(18,5))
    for f,a,t in zip((fx,fy,ft),ax,('$f_x$','$f_y$','$f_t$')):
        h=a.imshow(f,cmap='bwr')
        a.set_title(t)
        fg.colorbar(h,ax=a)

def compareGraphs(u,v,Inew,scale=3, quivstep=5):
    """
    makes quiver
    """
    if figure is None:
        return

    ax = figure().gca()
    ax.imshow(Inew,cmap = 'gray', origin='lower')
    # plt.scatter(POI[:,0,1],POI[:,0,0])
    for i in range(0,len(u), quivstep):
        for j in range(0,len(v), quivstep):
            ax.arrow(j,i, v[i,j]*scale, u[i,j]*scale, color='red',
                     head_width=0.5, head_length=1)

	# plt.arrow(POI[:,0,0],POI[:,0,1],0,-5)

    draw(); pause(0.01)


def compareGraphsLK(imgOld, imgNew, POI, V,scale=1.):
    if figure is None:
        return

    ax = gca()
    ax.imshow(imgNew,cmap = 'gray')
    # plt.scatter(POI[:,0,1],POI[:,0,0])
    for i in range(len(POI)):
        ax.arrow(POI[i,0,1],POI[i,0,0],
                    V[i,1]*scale, V[i,0]*scale,
                    color = 'red')
    # plt.arrow(POI[:,0,0],POI[:,0,1],0,-5)
    show()