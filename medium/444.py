"""
Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 <= n <= 104. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

Example 1:
Input:
org: [1,2,3], seqs: [[1,2],[1,3]]
Output:
false
Explanation:
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.

Example 2:
Input:
org: [1,2,3], seqs: [[1,2]]
Output:
false
Explanation:
The reconstructed sequence can only be [1,2].

Example 3:
Input:
org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]
Output:
true
Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].

Example 4:
Input:
org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]
Output:
true
"""

def sequenceReconstruction(org, seqs):
    n = len(org)
    in_bound = [0] * n
    out_bound = [set() for _ in xrange(n)]
    for seq in seqs:
        if any(s > n or s < 1 for s in seq):
            return False
        for i in xrange(1, len(seq)):
            if seq[i]-1 not in out_bound[seq[i-1]-1]:
                in_bound[seq[i]-1] += 1
                out_bound[seq[i-1]-1].add(seq[i]-1)
    queue = [i-1 for i in org if in_bound[i-1] == 0]
    for i in xrange(n):
        if len(queue) != 1 or queue[0] != org[i]-1:
            return False
        num = queue.pop()
        for each in out_bound[num]:
            in_bound[each] -= 1
            if in_bound[each] == 0:
                queue.append(each)
    return True
