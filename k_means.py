from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
class KMeans():
	def __init__(self, n_clusters=2, random_state=1):
		self.n_clusters = n_clusters
		self.random_state = random_state
		np.random.seed(random_state)
		self.ys = []

	def get_starting_clusters(self,X):
		return X[np.random.randint(len(X), size=self.n_clusters), :]

	def cluster_for(self,x,current_clusters):
		min_dist = 999999999
		min_val = -1
		for i in range(len(current_clusters)):
			dist = np.linalg.norm(x-current_clusters[i])
			if dist < min_dist:
				min_dist = dist
				min_val = i
		return min_val


	def mean_for(self,X,y_curr,cluster):
		to_mean = []
		for i in range(len(X)):
			if y_curr[i] == cluster:
				to_mean.append(X[i])
		return np.array(to_mean).mean(axis=0)

	def fit_predict(self,X):
		current_clusters =  self.get_starting_clusters(X)
		y_prev = [0]*len(X)
		y_curr = []
		while y_curr != y_prev:
			y_prev = y_curr
			y_curr = []
			for i in range(len(X)):
				y_curr.append(self.cluster_for(X[i],current_clusters))
			new_clusters = []
			for i in range(len(current_clusters)):
				new_clusters.append(self.mean_for(X, y_curr, i))
			current_clusters = new_clusters
			self.ys.append(y_curr)
		return y_curr



X, y = make_blobs(n_samples=1000, random_state=1, centers=5)
kmeans = KMeans(n_clusters=5, random_state=1)
kmeans.fit_predict(X)

rows = (len(kmeans.ys))/2 +1

for i in range(len(kmeans.ys)):
	plt.subplot(rows, 2, i+1)
	plt.scatter(X[:, 0], X[:, 1], c=kmeans.ys[i])

plt.subplot(rows, 2, rows*2)
plt.scatter(X[:, 0], X[:, 1], c=y)

plt.show()


