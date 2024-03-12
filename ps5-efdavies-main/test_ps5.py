# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import pytest

import Prob1
import Prob2

class Test_Prob1:
    def test_returns_string(self):
        student = Prob1.to_obenglobish("english")
        assert type(student) == str, f"You should be returning a string, but are currently returning a {type(student)}."

    def test_easy_vowels(self):
        words = ["english", "fish", "panda"]
        sols = ["obenglobish", "fobish", "pobandoba"]
        for w,s in zip(words, sols):
            student = Prob1.to_obenglobish(w)
            assert student == s, f"{w} translated to {student} but should have been {s}."

    def test_repeat_vowels(self):
        words = ["gooiest", "fruit", "books"]
        sols = ["gobooiest", "frobuit", "bobooks"]
        for w,s in zip(words, sols):
            student = Prob1.to_obenglobish(w)
            assert student == s, f"{w} translated to {student} but should have been {s}."

    def test_ending_ees(self):
        words = ["amaze", "apple", "eerie"]
        sols = ["obamobaze", "obapple", "obeerobie"]
        for w,s in zip(words, sols):
            student = Prob1.to_obenglobish(w)
            assert student == s, f"{w} translated to {student} but should have been {s}."

class Test_Prob2:
    def test_PartA_returns_list_of_desired_length(self):
        imaxes = [10, 26, 8]
        for i in imaxes:
            student = Prob2.create_histogram_array(i,[1,2,3])
            assert len(student) == i, f"You are not returning a list of the proper length. An imax of {i} is giving a list of length {len(student)}."

    def test_PartA_returns_correct_counts(self):
        data = [
            (10,[3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]),
            (2, [1,0,1,1,0,0,0,1,0,1,1,0,1,0,0,1,0,1,0,1,0,1]),
            (20,[i % 20 for i in range(56)]),
            (10,[8,8,8,8,8,8,8]),
        ]
        sols = [
            [0,2,1,2,1,4,1,1,1,3],
            [11,11],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2],
            [0,0,0,0,0,0,0,0,7,0],
        ]
        for i,o in zip(data, sols):
            student = Prob2.create_histogram_array(*i)
            assert student == o, f"Your histograms do not match. create_histogram_array{i} should give {o} but is instead giving {student}."

    def test_PartA_counts_consistant_with_input(self):
        data = [
            (10,[3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]),
            (2, [1,0,1,1,0,0,0,1,0,1,1,0,1,0,0,1,0,1,0,1,0,1]),
            (20,[i % 20 for i in range(56)]),
            (10,[8,8,8,8,8,8,8]),
        ]
        for i in data:
            student = Prob2.create_histogram_array(*i)
            assert sum(student) == len(i[1]), "The sum of all the elements in your histogram array should be equal to the original number of elements in the data list!"

    def test_PartB_returns_nothing(self):
        h = [2,4,6,8,1,3,7,2,9,4]
        student = Prob2.print_histogram(h)
        assert student is None, "print_histogram should only print, not return anything!"

    def test_PartB_lines_start_with_digit(self, capsys):
        h = [2,4,6,8,1,3,7,2,9,4]
        Prob2.print_histogram(h)
        captured = capsys.readouterr().out.splitlines()
        for i,line in enumerate(captured):
            assert line[0].isdigit(), "Each line of your printout should start with a number!"
            assert line[0] == str(i), "Your numbering pattern should start at 0 and count up!"

    def test_PartB_line_have_cor_num_stars(self, capsys):
        h = [2,4,6,8,1,3,7,2,9,4]
        Prob2.print_histogram(h)
        captured = capsys.readouterr().out.splitlines()
        for i,(line,c) in enumerate(zip(captured, h)):
            assert line.count('*') == c, f"For a histogram array of {h}, you should have {h[i]} stars in the {i}th line, but you seem to have only {line.count('*')}."

