# Everyone
# has
# noticed, there is a
# spell
# check
# while we are typing any word in MS word.
#
# Similar
# thing
# we
# want
# to
# achieve
# by
# creating
# a
# function.The
# function
# should
# correct
# spelling
# mistake as well as should
# substitute
# multiple
# spaces
# into
# a
# single
# space
# between
# two
# words.
#
# There
# will
# be
# a
# predefined
# dictionary
# of
# words as below: -
#
# environment
#
# always
#
# protect
#
# irreplaceable
#
# different
#
# absolutely
#
# greatest
#
# glory
#
# predictable
#
# flavor
#
# should
# order
# just
# different
#
# Spell
# check
# will
# be
# based
# on
# string
# matching
# with this above dictionary.If there is a word that is not matched with any of these words then, the word should be printed as it is, even though there might be a spelling mistake.And the words that will be compared must have equal length.
#
# For
# example, consider
# below
# sentence: -
#
# “We
# should
# protect
# our
# envaronment
# alwoys”


def spell_check_test(sentence,dict):
    correct_words = []

    for word_test in sentence:
        correct_word = []
        correct_word = word_test
        for i in dict:
            count = 0


            if len(word_test) == len(i):


                length = len(word_test)
                for j in range(len(i)):


                    if word_test[j] == i[j]:
                        count += 1


                    if count == length - 1 or count == length:
                        correct_word = i
        correct_words.append(correct_word)
    return correct_words

dict= [
    "environment",
    "always",
    "protect",
    "irreplaceable",
    "different",
    "absolutely",
    "greatest",
    "glory",
    "predictable",
    "flavor",
    "should",
    "order",
    "just",
    "different"
]

sentence = " HI gltry  jpertyy"
word = sentence.split()

list_crr =spell_check_test(word,dict)
c=' '.join(list_crr)

print(c)






























