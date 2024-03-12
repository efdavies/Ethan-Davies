# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import pytest

import Prob2
import Prob3


class Test_Prob2:
    words = ['cold', 'good', 'bright']

    def test_negate_exists(self):
        assert "negate" in dir(Prob2), "No function called negate found. Did you name it correctly?"
    
    def test_intensify_exists(self):
        assert "intensify" in dir(Prob2), "No function called intensify found. Did you name it correctly?"
   
    def test_reinforce_exists(self):
        assert "reinforce" in dir(Prob2), "No function called reinforce found. Did you name it correctly?"

    def test_negate(self):
        sols = ['uncold', 'ungood', 'unbright']
        for word,sol in zip(self.words, sols):
            sub = Prob2.negate(word)
            assert sub.lower() == sol, f"The negation of {word} should be {sol}, but instead is {sub}."

    def test_intensify(self):
        sols = ['pluscold', 'plusgood', 'plusbright']
        for word,sol in zip(self.words, sols):
            sub = Prob2.intensify(word)
            assert sub.lower() == sol, f"The intensifying of {word} should be {sol}, but instead is {sub}."

    def test_reinforce(self):
        sols = ['doublecold', 'doublegood', 'doublebright']
        for word,sol in zip(self.words, sols):
            sub = Prob2.reinforce(word)
            assert sub.lower() == sol, f"The reinforcing of {word} should be {sol}, but instead is {sub}."

    def test_multi_modifiers(self):
        assert Prob2.reinforce(Prob2.intensify("bright")).lower() == "doubleplusbright"
        assert Prob2.intensify(Prob2.negate("bad")).lower() == "plusunbad"
        assert Prob2.reinforce(Prob2.intensify(Prob2.negate("fair"))).lower() == "doubleplusunfair"

class Test_Prob3:
    
    def test_partA_prints_something(self, capsys):
        Prob3.print_divisible_by_six_or_seven()
        captured = capsys.readouterr().out.rstrip()
        assert len(captured) > 0, "Is your code actually printing out anything from inside the function? It should be!"

    def test_partA_multiples_of_six_or_seven(self, capsys):
        Prob3.print_divisible_by_six_or_seven()
        captured = capsys.readouterr().out.rstrip()
        values = [int(n) for n in captured.split('\n')]
        for num in values:
            assert num % 6 == 0 or num % 7 == 0, f"The number {num} was printed to the screen but that is not divisible by either 6 or 7."

    def test_partA_multiples_of_six_and_seven(self,capsys):
        Prob3.print_divisible_by_six_or_seven()
        captured = capsys.readouterr().out.rstrip()
        values = [int(n) for n in captured.split('\n')]
        for num in values:
            assert not (num % 6 == 0 and num % 7 == 0), f"The number {num} was printed to the screen, but it is divisible by both 6 AND 7, and thus should not be printed."
        
    def test_partB_returns_something(self):
        sol = Prob3.list_divisible_by_six_or_seven(1,100)
        assert type(sol) == list, "Is your code returning a list type object? It should be!"

    def test_partB_multiples_of_six_or_seven(self):
        sol = Prob3.list_divisible_by_six_or_seven(1,100)
        for num in sol:
            assert num % 6 == 0 or num % 7 == 0, f"The number {num} was included in your list but it is not divisible by either 6 or 7."

    def test_partB_multiples_of_six_and_seven(self):
        sol = Prob3.list_divisible_by_six_or_seven(1,100)
        for num in sol:
            assert not (num % 6 == 0 and num % 7 == 0), f"The number {num} was included in your list, but it is divisible by both 6 AND 7, and thus should not be included."


    def test_partB_within_thresholds(self):
        sol = Prob3.list_divisible_by_six_or_seven(50,75)
        for num in sol:
            assert 50 <= num and num <= 75, f"With inputs of 50 and 75, you should only have numbers in the list between 50 and 75, but you currently have the number {num} in the list."
