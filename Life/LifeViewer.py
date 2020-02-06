

class LifeViewer:

    @staticmethod
    def show_world(world,  fix_window, legend):
        if world.get_empty():
            print("**********AVERYBODY IS DEAD IN GENERATION {0}************".format(world.get_generation()))
            return
        str = '--------------GENERATION {0}--------------\n'.format(world.get_generation())
        for row in world.get_world():
            for col in row:
                if col == 0:
                    str = str + '   '
                else:
                    str = str + ' # '
            str = str + '\n'
        # print(str, end='')
        print("\033[2J\033[1;1H" + str)
        # print("---------------------")
        # for ii in (0, self.__size):
        #    print("\033[F                                      ", end='')
        # print("=====================")
