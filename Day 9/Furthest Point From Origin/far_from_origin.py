class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        s1=moves.replace("_","L")
        s2=moves.replace("_","R")
        return(max(abs(s1.count("R")-s1.count("L")), abs(s2.count("R")-s2.count("L"))))
