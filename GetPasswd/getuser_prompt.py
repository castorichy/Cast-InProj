import getpass as gp
"""This module show how to use getpass to display security quastions"""

def secQuiz():
    defoult_ans = "blue"
    user_ans = gp.getpass(prompt="Whats Your fevorite color? ")
    if user_ans.lower() == defoult_ans:
        print("Your fevorite color is ", user_ans)
    else:
        print("Wrong anser")

secQuiz()
