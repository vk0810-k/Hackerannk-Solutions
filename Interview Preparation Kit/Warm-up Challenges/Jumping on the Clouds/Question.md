There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game.

For each game, you will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided.

## Example
![image](https://user-images.githubusercontent.com/68016633/144066650-408e16e0-20c7-4a35-9774-10e0367c1f80.png)

Index the array from 0...6. The number on each cloud is its index in the list so the player must avoid the clouds at indices 1 and 5. They could follow these two paths: ![image](https://user-images.githubusercontent.com/68016633/144066824-d4a079dd-10a1-4c66-b81e-4337543d6222.png)
 or ![image](https://user-images.githubusercontent.com/68016633/144066866-f91f82bf-be45-4207-a5d4-84e4fde30ce1.png). The first path takes 3 jumps while the second takes 4. Return 3.

## Function Description

Complete the jumpingOnClouds function in the editor below.

jumpingOnClouds has the following parameter(s):
- int c[n]: an array of binary integers

## Returns

- int: the minimum number of jumps required

## Input Format

The first line contains an integer n, the total number of clouds. The second line contains n space-separated binary integers describing clouds c[i] where ![image](https://user-images.githubusercontent.com/68016633/144067176-0d2b4922-d6d0-408d-bd18-148f6a31a847.png).

## Constraints

![image](https://user-images.githubusercontent.com/68016633/144067247-49f2810c-0cbd-43ba-9823-4f6804dabab2.png)


## Output Format

Print the minimum number of jumps needed to win the game.

## Sample Input 0
```
7
0 0 1 0 0 1 0
```

## Sample Output 0
```
4
```

## Explanation 0:
The player must avoid c[2] and c[5]. The game can be won with a minimum of 4 jumps:

![image](https://user-images.githubusercontent.com/68016633/144067958-a24715a0-1cb0-439c-b49c-77d9549b7454.png)


## Sample Input 1
```
6
0 0 0 0 1 0
```

## Sample Output 1
```
3
```
## Explanation 1:
The only thundercloud to avoid is c[4]. The game can be won in 3 jumps:

![image](https://user-images.githubusercontent.com/68016633/144068273-dfbe3894-b587-4590-835a-2209f6d323c4.png)
