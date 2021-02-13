#Created by Nic Holaday 2016
#nic.holaday@comfyapp.com

import random
import time
import readchar

navigation = {
    "Move left one character": 'h',
    "Move down one line": 'j',
    "Move up one line": 'k',
    "Move right one character": 'l',
    "Move to last line of screen": 'L',
    "Move to next word": "w",
    "Move to first line of screen": 'H',
    "Move to middle line of screen": 'M',
    "Move to beginning of line:": '0',
    "Move to end of line": '$',
    "Move to beginning of word": 'b',
    "Move to previous word": 'b',
    "Move to end of word": 'e',
}

cycles = 1
wronglist = []
correct_counter = 0
total_counter = 0
answertime = []

for i in range(0, cycles):
    print "Navigation!"
    print "List of %d commands running %d cycle(s)" % (len(navigation), cycles)
    keys = navigation.keys()

    random.shuffle(keys)

    for question in keys:
        start = time.time()

        print question, "> ",
        answer = repr(readchar.readchar())
        print answer

        if navigation[question] in answer:
            correct_counter += 1
#            print "Correct!"
        else:
            print "Incorrect, answer is: %s" % (navigation[question])
            wronglist.append(navigation[question])

        total_counter += 1
        end = time.time()

        answertime.append(end - start)

print "\nCongrats! Score: %d / %d" % (correct_counter, total_counter)
accuracy = (float(correct_counter) / float(total_counter) * 100)
print "Average answer time: %.2fs, Accuracy: %.0f" % (sum(answertime)/len(answertime), accuracy), "%"

print "You got these commands incorrect: "
print wronglist, "\n"
