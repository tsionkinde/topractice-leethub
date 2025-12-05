class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        score1=0
        score2=0
        for i in range(len(player1)):
            if (i>1 and player1[i-2] ==10) or (i>0 and player1[i-1] ==10):
               
                score1+=2*player1[i]
            else:
              
                score1+=player1[i]
               
        for i in range(len(player2)):
            if( i>1 and player2[i-2] ==10) or ( i>0 and player2[i-1] ==10):
               
                score2+=2*player2[i]
            else:
               
                score2+=player2[i]
              
        if score1 > score2:
            return 1
        elif score1==score2:
            return 0
        else:
            return 2    
                                



        