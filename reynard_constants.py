'''
Reynard is an agent that uses reasoning to solve cryptograms. 

These are the constants that are used within Reynard

Anthony Sheller
Reasoning Under Uncertainty
EN.605.745

''' 
# Define letter freqeuncy based on https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
# This is ranked from most frequent to least frequent
letter_frequency = {}        
letter_frequency['E'] = .111607
letter_frequency['A'] = .084966
letter_frequency['R'] = .075809
letter_frequency['I'] = .075448 
letter_frequency['O'] = .071635
letter_frequency['T'] = .069509
letter_frequency['N'] = .066544
letter_frequency['S'] = .057351
letter_frequency['L'] = .054893
letter_frequency['C'] = .045388
letter_frequency['U'] = .036308
letter_frequency['D'] = .033844
letter_frequency['P'] = .031671
letter_frequency['M'] = .030129
letter_frequency['H'] = .030034
letter_frequency['G'] = .024705
letter_frequency['B'] = .020720
letter_frequency['F'] = .018121
letter_frequency['Y'] = .017779
letter_frequency['W'] = .012899
letter_frequency['K'] = .011016
letter_frequency['V'] = .010074
letter_frequency['X'] = .002902
letter_frequency['Z'] = .002722
letter_frequency['J'] = .001965
letter_frequency['Q'] = .001962

# This table from https://en.wikipedia.org/wiki/Letter_frequency
letter_frequency_wiki = {}        
letter_frequency_wiki['E'] = .12702
letter_frequency_wiki['T'] = .09056
letter_frequency_wiki['A'] = .08167
letter_frequency_wiki['O'] = .07507
letter_frequency_wiki['I'] = .06966
letter_frequency_wiki['N'] = .06749
letter_frequency_wiki['S'] = .06327
letter_frequency_wiki['H'] = .06094
letter_frequency_wiki['R'] = .05987
letter_frequency_wiki['D'] = .04253
letter_frequency_wiki['L'] = .04025
letter_frequency_wiki['C'] = .02782 
letter_frequency_wiki['U'] = .02758
letter_frequency_wiki['M'] = .02406
letter_frequency_wiki['W'] = .02360
letter_frequency_wiki['F'] = .02228
letter_frequency_wiki['G'] = .02015
letter_frequency_wiki['Y'] = .01974
letter_frequency_wiki['P'] = .01929
letter_frequency_wiki['B'] = .01492
letter_frequency_wiki['V'] = .00978
letter_frequency_wiki['K'] = .00772
letter_frequency_wiki['J'] = .00153
letter_frequency_wiki['X'] = .00150
letter_frequency_wiki['Q'] = .00095
letter_frequency_wiki['Z'] = .00074


# Letter Frequency tables
# This is stored in an array with the order presereverd
# From Most frequent to least frequent
# http://letterfrequency.org/#Letter_Frequency_of_the_Most_Common_1st_Letter_in_Words
letter_frequency_in_english_language = 'e t a o i n s r h l d c u m f p g w y b v k x j q z'.split(' ')
most_common_first_letter_in_words = 't o a w b c d s f m r h i y e g l n p u j k'.split(' ')
most_common_second_letter_in_words = 'h o e i a u n r t'.split(' ')
most_common_third_letter_in_words = 'e s a r n i'.split(' ')
most_common_last_letter_of_words = 'e s t d n r y f l o g h a k m p u w'.split(' ')
digrph_frequency = 'th he an in er on re ed nd ha at en es of nt ea ti to io le is ou ar as de rt ve'.split(' ')
trigraph_frequency = 'the and tha ent ion tio for nde has nce tis oft men'.split(' ')
double_letter_frequency = 'ss ee tt ff ll mm oo'.split(' ')

# Word frequency tables
# This is stored in an array with the order preserved
# From most frequent to least frequent
# http://letterfrequency.org/word-frequency-english-language/
top_tweenty_most_used_words_in_written_english = 'the of to in and a for was is that on at he with by be it an as his'.split(' ')
top_tweenty_most_used_words_in_spoken_english = 'the and I to of a you that in it is yes was this but on well he have for'.split(' ')

two_letter_word_frequency = 'of to in it is me be as at so we us he by or on do if my up an go no am'.split(' ')
three_letter_word_frequency = 'the and for are but not you all any can had her was one our out day get has \
him his how man new now old see two way who boy did its let put say she too use cut off fan nba air joy awe sky sea bar'.split(' ')
four_letter_word_frequency = 'that with have this will your from they know want been good much some time very \
when come here just like long make many more only over such take than them well were real does live dare tire \
keep lost play draw love what tell kids give foul thin miss most slow down body find move even eyed true mean \
mote life best away less home'.split(' ')
word_frequency_most_common_words = 'the of and to in a is that be it by are for was as he with on his at which \
but from has this will one have not were or all their an i there been many more \
so when had may today who would time we about after dollars if my other some \
them being its no only over very you into most than they day even made out first \
great must these can days every found general her here last new now people \
public said since still such through under up war well where while years before \
between country debts good him interest large like make our take upon what'.split(' ')
