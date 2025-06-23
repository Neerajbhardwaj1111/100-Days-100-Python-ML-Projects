import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from matplotlib.colors import ListedColormap

iris = load_iris()
X = iris.data[:,2:4] #only Petal length and petal width
y = iris.target
target_names =iris.target_names

model=DecisionTreeClassifier().fit(X,y)

#mesh grid
x_min,x_max =X[:,0].min()-1,X[:,0].max()+1
y_min,y_max =X[:,1].min()-1,X[:,1].max()+1

xx,yy=np.meshgrid(np.arange(x_min,x_max,0.02),np.arange(y_min,y_max,0.02))

Z=model.predict(np.c_[xx.ravel(),yy.ravel()])
Z=Z.reshape(xx.shape)

plt.figure(figsize=(10, 6))
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

plt.contourf(xx, yy, Z, cmap=cmap_light)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor='k', s=50)

plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.title('Decision Boundaries - Iris Classification (Petal Features)')

plt.legend(handles=[
    plt.Line2D([], [], marker='o', color='w', label=target_names[0],
               markerfacecolor='#FF0000', markersize=10),
    plt.Line2D([], [], marker='o', color='w', label=target_names[1],
               markerfacecolor='#00FF00', markersize=10),
    plt.Line2D([], [], marker='o', color='w', label=target_names[2],
               markerfacecolor='#0000FF', markersize=10)
])
plt.show()
