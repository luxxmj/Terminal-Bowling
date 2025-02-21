from random import randint


class Bowling:
    def __init__(self):
        self.pins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.pin_amt = len(self.pins)
        self.score = []
        self.frame_scores = []

    def reset_pins(self):
        self.pins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def reset_score(self):
        self.score = []

    def change_frame_scores(self):
        for i, frame in enumerate(self.frame_scores):

            if frame[1] == 'strike':
                if i == 0:
                    self.frame_scores[i] = [frame[0], 10]
                    try:
                        self.frame_scores[i][1] += self.frame_scores[i+1][2][0] + self.frame_scores[i+1][2][1]
                    except TypeError:
                        try:
                            self.frame_scores[i][1] += self.frame_scores[i+1][2] + self.frame_scores[i+2][2][0]
                        except TypeError:
                            self.frame_scores[i][1] += self.frame_scores[i+1][2] + self.frame_scores[i+2][2]
                elif i == 8:
                    self.frame_scores[i] = [frame[0], self.frame_scores[i-1][1] + 10]
                    self.frame_scores[i][1] += (self.frame_scores[i+1][2][0] + self.frame_scores[i+1][2][1])
                else:
                    self.frame_scores[i] = [frame[0], self.frame_scores[i-1][1] + 10]
                    try:
                        self.frame_scores[i][1] += self.frame_scores[i+1][2][0] + self.frame_scores[i+1][2][1]
                    except TypeError:
                        try:
                            self.frame_scores[i][1] += self.frame_scores[i+1][2] + self.frame_scores[i+2][2][0]
                        except TypeError:
                            self.frame_scores[i][1] += self.frame_scores[i+1][2] + self.frame_scores[i+2][2]
            elif frame[1] == 'spare':
                if i == 0:
                    self.frame_scores[i] = [frame[0], 10]
                    try:
                        self.frame_scores[i][1] += self.frame_scores[i+1][2][0]
                    except TypeError:
                        self.frame_scores[i][1] += self.frame_scores[i+1][2]
                else:
                    self.frame_scores[i] = [frame[0], self.frame_scores[i-1][1] + 10]
                    try:
                        self.frame_scores[i][1] += self.frame_scores[i+1][2][0]
                    except TypeError:
                        self.frame_scores[i][1] += self.frame_scores[i+1][2]
            elif frame[1] == 'blank':
                if i == 0:
                    self.frame_scores[i] = [frame[0], frame[2][0] + frame[2][1]]
                else:
                    self.frame_scores[i] = [frame[0], (self.frame_scores[i-1][1] + frame[2][0] + frame[2][1])]
            elif frame[1] == 'final':
                self.frame_scores[i] = [frame[0], self.frame_scores[i-1][1]]
                self.frame_scores[i][1] += (self.score[0] + self.score[1] + self.score[2])

    def display_frame_scores(self):
        return self.frame_scores


class Frame(Bowling):
    frame = 1

    def __init__(self):
        super().__init__()
        self.pins_hit = randint(0, len(self.pins))

    def roll(self):
        self.pins_hit = randint(0, len(self.pins))

        if self.pins_hit != 10:
            for index in range(self.pins_hit):
                del self.pins[0]

        self.score.append(self.pins_hit)

    def create_frame_score(self, frame_number, enter, score):
        lst = ['Frame ' + str(frame_number), enter, score]
        self.frame_scores.append(lst)

    def display_scores(self, enter):
        if enter == 'reg':
            print(f"You hit {self.pins_hit} pins")
        elif enter == 'strike':
            print(f"You hit a strike on Frame {self.frame}")
        elif enter == 'spare':
            print(f"You hit a spare on Frame {self.frame}")
        elif enter == 'blank':
            print(f"You hit {self.score[0] + self.score[1]} pins total on Frame {self.frame}")
        elif enter == 'final blank':
            print(f"You hit {self.score[0] + self.score[1]} pins total on Frame {self.frame}")
        elif enter == 'final total':
            print(f"You hit {self.score[0] + self.score[1] + self.score[2]} pins total on Frame {self.frame}")


test = Frame()


def play():
    while True:
        print(f"\n\nCurrently on Frame {test.frame}")
        if test.frame != 10:
            turns = 2
        else:
            turns = 3
        while turns != 0:
            input("Press enter to roll the ball: ")
            test.roll()
            if test.pins_hit != 10 or test.frame == 10:
                test.display_scores('reg')
            else:
                test.display_scores('strike')
                test.create_frame_score(test.frame, 'strike', 10)
                break
            if test.frame == 10:
                if turns == 2:
                    if len(test.pins) == 0 or test.score[0] == 10:
                        if test.score[0] == 10:
                            turns -= 1
                            continue
                        else:
                            test.reset_pins()
                            turns -= 1
                            continue
                    else:
                        test.display_scores('final_blank')
                        test.create_frame_score(test.frame, 'blank', test.score)
                        break
                elif turns == 3:
                    turns -= 1
                elif turns == 1:
                    test.display_scores('final_total')
                    test.create_frame_score(test.frame, 'final', test.score)
                    break
            else:
                turns -= 1
        if test.frame != 10:
            if len(test.pins) != 0 and test.pins_hit != 10:
                test.display_scores('blank')
                test.create_frame_score(test.frame, 'blank', test.score)
            elif len(test.pins) == 0 and test.pins_hit != 10:
                test.display_scores('spare')
                test.create_frame_score(test.frame, 'spare', test.score)
            test.frame += 1
            test.reset_score()
            test.reset_pins()
            continue
        else:
            break

    test.change_frame_scores()
    print('\n')
    for k, v in test.display_frame_scores():
        print(f'after {k} your score was {v}')


play()
