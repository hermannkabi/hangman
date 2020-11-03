class HangmanUtils:
    words = ["tere", "alasi", "kitarr", "sukeldu", "lauljanna", "baleriin", "golfar", "arst", "planeet", "sülearvuti", "kompromiss", "seljakott"]


    def is_input_int(self,inpt):
        try:
            int(inpt)
            return True
        except ValueError:
            return False
