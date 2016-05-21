#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
hmm homework: flip the coins

Viterbi HMM alignment
for each sequence, find the maximum likelihood state path.
print out the maximum likelihood guess for which position was the first flip of the biased coin

format:
input:
	HTHHHHTTTH
output:
	state_seq trans_position(counting starts from 1)
	111112222 6

2015.11.28 by xnm
'''

#viterbi algorithm
def viterbi(obs_seq,states,start_p,trans_p,emit_p,end_p):
	#set the saving matrix
	T = {}
	for state in states:
		#            prob.   path
		T[state] = (1,[])
	
	#calculate the max prob. & optimal path
	count = 0
	for obs in obs_seq:
		U = {} #temp vector fot saving the prob. calculated
		for current_state in states:
			prob_max = 0
			path_max = []
			count += 1	
			if count == 1:
				prob_max = start_p[current_state] * emit_p[state][obs]
				#path_max = [current_state] #no, for the first step, there is no result. The second step generate the first path.
			else:
				for source_state in states:
					(prob,path) = T[source_state]
					p = trans_p[source_state][current_state] * emit_p[current_state][obs]
					prob *= p
					#choose the max one (prob & path)
					if prob > prob_max:
						prob_max = prob
						path_max = path + [source_state] #source_state or current_state?	
			U[current_state] = (prob_max,path_max)
		T = U

	#final choose:
	prob_max = 0
	path_max = None
	for state in states:
		(prob,path) = T[state]
		#add end_prob to take into account: 
		end_prob = prob * end_p[state]
		#choose the max end_prob, and return the accordant path
		if end_prob >prob_max:
			prob_max = end_prob
			path_max = path + [state] #append the final state as the specific pathway was determined by the final max prob.
	return path_max

#conditions

states = ('1', '2')
start_probability = {'1': 1, '2': 0}
transition_probability = {
	'1' : {'1' : 0.99, '2' : 0.01},
	'2' : {'1' : 0, '2' : 0.95}
}
emission_probability = {
	'1' : {'H' : 0.5, 'T' : 0.5},
	'2' : {'H' : 0.8, 'T' : 0.2}
}
end_probability = {'1' : 0, '2' : 0.05}

#data process
file_in = open('example','r')
file_out = open('Viterbi_output.txt','w')

file_out.write('state_sequence trans_position(counting starts from 1)\n')

for line in file_in:
	obs_seq = line.rstrip()
	path = viterbi(obs_seq, states, start_probability, transition_probability, emission_probability, end_probability)
	#use element appending to str the list:
	path_str = ''
	for i in path:
		path_str += i
	#use count to get the position -- suit for this particular situation
	count = path_str.count('1')
	count += 1
	file_out.write(path_str+' '+str(count)+'\n')

file_in.close()
file_out.close()

