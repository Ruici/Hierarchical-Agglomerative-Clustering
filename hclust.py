import sys
import math, heapq
#calulate the distance from each cluster
dimenstion = 1
point = dict()

def distance(Cen1, Cen2):
	res = 0
	# print "centrod 1" ,Cen1
	# print "centrod 2", Cen2
	for i in range(0, dimenstion):
		res += math.pow((Cen1[i] - Cen2[i]), 2)
		#print 
	res = math.sqrt(res)
	return res

class Cluster(object):
	def __init__(self, C):
		self.C = C
		#centrood:
		# print "C is", C
		coo = list()
		centroid = list()
		for i in range (0, dimenstion):
			coo.append(0.0)
			for x in C:
				coo[i] += float(point[x]['coor'][i])
				#print "x is", 
		#print coo
		for i in range(0, dimenstion):
			coo[i] = coo[i] / len(C)
			centroid.append(coo[i])
		self.centroid = centroid
		#else:

		
class Node(object):

	def __init__(self, C1, C2):
		self.C1 = C1
		self.C2 = C2
		self.distance = distance(C1.centroid, C2.centroid)
		

def main(inputFile, no_cluster):
	global dimenstion
	global point
	node_no = 0
	
	cluster = dict()
	relevant_doc = dict()
	#initially
	for line in inputFile:

		array = line.strip().split(',')
		cluster_type = array[-1]
		array.pop(-1)
		coor = array
		dimenstion = len(coor)
		#print array, cluster_type
		idx = tuple([node_no])
		point[node_no] = dict()
		point[node_no]['coor'] = coor
		#point[node_no]['label'] = cluster_type
		if cluster_type not in relevant_doc:
			relevant_doc[cluster_type] = list()
		relevant_doc[cluster_type].append(node_no)
		#print point[i]
		
		cluster[node_no] = Cluster(idx)
		# print i
		#print cluster[i].C, cluster[i].centroid
		node_no += 1
		# if i == 3:
		# 	break

	cluster_no = node_no

	h = list()
	for i in range(0, node_no):
		for j in range(i+1, node_no):
			one = Node(cluster[i], cluster[j])
			#print one.distance
			h.append((one.distance, one))

	#initially build the heap
	heapq.heapify(h)
	mergedset = dict()

	#cluster_no = 2
	while(cluster_no > no_cluster):
	#then find the min value
		mini = heapq.heappop(h)
	
	
	#check if it's in the merged set
		while((mini[1].C1.C) in mergedset or (mini[1].C2.C) in mergedset):
			mini = heapq.heappop(h)


	#set they are merged
		mergedset[mini[1].C1.C] = 1
		mergedset[mini[1].C2.C] = 1

	#merge two cluster
		c1 = mini[1].C1.C
		c2 = mini[1].C2.C
		
		c = c1 + c2
		if c2 == (12, 10, 13):
			print mini[1].C2.centroid
			print mini[1].C1.centroid

		cluster[node_no] = Cluster((c))
		node_no += 1

		
	#calculate the distance between other cluster, and put into the heap
		for i in range(0, node_no):
			if i != node_no - 1 and cluster[i].C not in mergedset:
				one = Node(cluster[i], cluster[node_no - 1])
				heapq.heappush(h, (one.distance, one))
				# print cluster[i].C, cluster[node_no - 1].C
				# print one.distance
				
		cluster_no -= 1
	#print cluster[c1].C
	#delete key from cluster
	relevant_set = set()
	retrieved_set = set()

	for i in range (0, node_no):
		if cluster[i].C not in mergedset:
			res_list =  sorted(list(cluster[i].C))
			#print res_list
			for i in range (0, len(res_list)):
				for j in range(i+1, len(res_list)):
					retrieved_set.add((res_list[i], res_list[j]))
	for key in relevant_doc:
		for i in range (0, len(relevant_doc[key])):
				for j in range(i+1, len(relevant_doc[key])):
					relevant_set.add((relevant_doc[key][i], relevant_doc[key][j]))

	inter = retrieved_set.intersection(relevant_set)
	# print "inter len", len(inter)
	# print len(retrieved_set)
	# print len(relevant_set)
	precision = float(len(inter))/ len(retrieved_set)
	print precision
	recall = float(len(inter))/ len(relevant_set)
	print recall
	
	for i in range (0, node_no):
		if cluster[i].C not in mergedset:
			res_list =  sorted(list(cluster[i].C))
			print res_list

	
if __name__ == '__main__':
	inputFile = open(sys.argv[1])#file name
	no_cluster = int(sys.argv[2])
	main(inputFile, no_cluster)
	