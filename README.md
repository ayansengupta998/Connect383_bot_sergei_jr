# Connect383_bot_sergei_jr

Team:
Achuthan Panikath
Ayan Sengupta

Bot name:
Sergie Jr.

Evaluation Function thinking:

When at a certain depth we find a similar symbol in two consecutive spots, we call ahead the utlity of having a sequence of three and pass that upwards.
Though greedy in behavior such that it prematurely calls for earliest sequence of 3, this has been found to be a good predictor of behavior. The function is
fast for small boards but as the size gets more complex, this prediction becomes less accurate because of the innate nature of nudging solutions to the 
earliest sequence of three.

Test boards in test_boards.py are meant to test specific scenarios such as a full board, board with obstacles, a large board, board that calls for an efficient
choice and a small and direct board. These account for a large spectrum of plays that can efficiently capture the efficacy of our code and whether or not
it behaves as expected.

Notes:

We got all the basic functionality working. We do have some issue with particularly large boards where behavior gets slightly erratic and slow. 
Because most testing was done on paper and directly via terminal, we didn;t use test-boards to implement our own tests which in hindsight we probably should
have leveraged better.


