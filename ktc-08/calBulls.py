def calBall(input, answer):
    total = 0
    for i in range(4):
       if input[i] in answer and input[i] != answer[i]:
           total = total + 1;
    return total


if __name__ == "__main__":
    input = [1, 2, 3, 4]
    answer = [1, 2, 4, 3]
    ball = calBall(input, answer)
    print(ball, "Bull")
    

