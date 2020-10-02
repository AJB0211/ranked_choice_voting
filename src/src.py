from collections import Counter


first_elems = lambda lstlst: [i[0] for i in lstlst if i]


rm_empty = lambda lstlst: [lst for lst in lstlst if lst]


rm_candidate = lambda lstlst, cand: [[i for i in lst if i != cand] for lst in lstlst]


rm_candidates = lambda lstlst, cands: [[i for i in lst if i not in cands] for lst in lstlst]


get_missing = lambda lstlst, cands: list(set(flatten(lstlst)) - set(cands))


rm_missing = lambda lstlst, cands: rm_candidates(lstlst, get_missing(lstlst, cands))


get_min_cand = lambda cands: [k for k, _ in sorted(Counter(cands).items(), key=lambda item: item[1])][0]


def InstantRunoffVoting(ballots, threshold = 0.5):
    """ Takes a List[List] of ballots and returns the winner who achieves more than threshold of vote over the runoff process """
    def inner(ballots, n_ballots=0):
        if not rm_empty(ballots):
            raise ValueError("This Ballot is Undecidable")
            
        cands = first_elems(ballots)
        
        ## Win condition
        if Counter(cands).most_common(1)[0][1] >= n_ballots*0.5: 
            return Counter(cands).most_common(1)[0][0]
        
        min_cand = get_min_cand(cands)
        print(min_cand)
        return inner(
            rm_candidate(
                rm_missing(ballots, cands),
                min_cand
            ),
            n_ballots
        )
        
    return inner(ballots, len(ballots))