class Guesser:
    @staticmethod
    def is_even(n):
        if n % 2 == 0:
            return True
        else:
            return False

    @staticmethod
    # Comparing word means that seeing that how many letters are same in word1 and word2
    def compare_words(word1,word2,midpoint): 
        # word1 is incorrect word and word2 is correct that coming from dictionary
        reversed_word2 = word2[::-1]
        right_half_word_1 = word1[:midpoint+1] # I will check right from front and left from back
        left_half_word_1 = word1[midpoint+1:]
        no_of_occurrence = 0

        for index,alphabet in enumerate(right_half_word_1): # right side matching
            if alphabet == word2[index]:
                no_of_occurrence = no_of_occurrence + 1
            else:
                no_of_occurrence = no_of_occurrence + 0
        
        for index,alphabet in enumerate(reversed(left_half_word_1)): # lef side matching
            if alphabet == reversed_word2[index]:
                no_of_occurrence = no_of_occurrence + 1
            else:
                no_of_occurrence = no_of_occurrence + 0
        return no_of_occurrence

    @staticmethod
    def give_me_max_(parm_dict): # This Function will give me the max occurrence word
        pass

    @staticmethod
    def guess(word):
        first_char = word[0]
        length_of_word = len(word)

        # Opening the appropriate file
        with open(f'words/{first_char}.txt') as word_list_file:
            all_word_occurence = {}  # This dict will store that how much probability of word
            mid_point_of_param_word = 0
            spilited_word_list_file = word_list_file.read().split('\n')
            if not Guesser.is_even(length_of_word): 
                # Means if word of a odd length then its midpoint will be fixed
                mid_point_of_param_word = round(length_of_word / 2)
                for word_list_word in spilited_word_list_file:
                    if len(word_list_word) > mid_point_of_param_word:
                        no_of_occurence = Guesser.compare_words(word,word_list_word,mid_point_of_param_word)
                        all_word_occurence.update({word_list_word:no_of_occurence})
            else:
                for word_list_word in spilited_word_list_file:
                    """Conditioning which midpoint will be selcted. 
                    Exp In 'abcd' i can select both b and c as midpoint.
                    But i have to select which will i select"""
                    if len(word_list_word) > int((length_of_word / 2)):
                        mid_point_of_param_word = int((length_of_word / 2) - 1)
                        if word[mid_point_of_param_word] == word_list_word[mid_point_of_param_word]:
                            no_of_occurence = Guesser.compare_words(word,word_list_word,mid_point_of_param_word)
                            all_word_occurence.update({word_list_word:no_of_occurence})
                        else:
                            mid_point_of_param_word = int(length_of_word / 2)
                            no_of_occurence = Guesser.compare_words(word,word_list_word,mid_point_of_param_word)
                            all_word_occurence.update({word_list_word:no_of_occurence})
                    elif len(word_list_word) > int(length_of_word / 2):
                        mid_point_of_param_word = int(length_of_word / 2)
                        no_of_occurence = Guesser.compare_words(word,word_list_word,mid_point_of_param_word)
                        all_word_occurence.update({word_list_word:no_of_occurence})
            print(all_word_occurence)

if __name__ == "__main__":
    test_case_word = 'elephant'
    Guesser.guess(test_case_word)
    
