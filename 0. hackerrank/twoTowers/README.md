# <a href="https://www.hackerrank.com/challenges/one-week-preparation-kit-tower-breakers-1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-three">Two Towers</a>

Two players are playing a game of Tower Breakers! Player 1 always moves first, and both players always play optimally. The rules of the game are as follows:

Initially there are towers.
Each tower is of height `m`.
The players move in alternating turns.
In each turn, a player can choose a tower of height `x` and reduce its height to `y`, where and evenly divides .
If the current player is unable to make a move, they lose the game.
Given the values of and , determine which player will win. If the first player wins, return . Otherwise, return .

Example.

There are towers, each units tall. Player has a choice of two moves:

-   remove pieces from a tower to leave as
-   remove pieces to leave

Let Player remove . Now the towers are and units tall.

Player matches the move. Now the towers are both units tall.

Now Player has only one move.

Player removes pieces leaving . Towers are and units tall.
Player matches again. Towers are both unit tall.

Player has no move and loses. Return .

Function Description

Complete the towerBreakers function in the editor below.

towerBreakers has the following paramter(s):

int n: the number of towers
int m: the height of each tower
Returns

int: the winner of the game
Input Format

The first line contains a single integer , the number of test cases.
Each of the next lines describes a test case in the form of space-separated integers, and .
