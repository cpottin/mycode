import html


trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }


question = html.unescape(trivia["question"])

correct_answer = html.unescape(trivia["correct_answer"])

incorrect_answer1 = html.unescape(trivia["incorrect_answers"][0])
incorrect_answer2 = html.unescape(trivia["incorrect_answers"][1])
incorrect_answer3 = html.unescape(trivia["incorrect_answers"][2])

print("Trivia Question: " + question)
print("A: " + incorrect_answer1)
print("B: " + incorrect_answer2)
print("C: " + correct_answer)
print("D: " + incorrect_answer3)
