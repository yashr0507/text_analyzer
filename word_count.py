import string
import csv

class TextAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.text = ""
        self.words = []
        self.word_counts = {}
        self.filtered_words = []
        self.filtered_word_counts = {}
        self.lettercounts = {}
        self.bigrams_counts = {}

    def load_file(self):
        with open(self.filename, 'r') as f:
                self.text = f.read()
        
    def clean_text(self):
        self.text = self.text.lower()
        self.text = self.text.translate(str.maketrans('','',string.punctuation))
        
    def split_words(self):
        self.words = self.text.split()

    def count_words(self, word_list):
        counts = {}
        for word in word_list:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1 
        return counts
    def top(self,word_list, n=10):
        sorted_words = sorted(word_list.items(), key=lambda x: x[1], reverse=True)
        return sorted_words[:n]
    
    def remove_stopwords(self):
        stopwords = ['the','and','is','to','a','of','in']   
        self.filtered_words = [w for w in self.words if w not in stopwords]

    def count_letters(self):
        letters = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
        self.lettercounts = {}
        for i in (self.text):
            if i in letters:
                if i in self.lettercounts:
                    self.lettercounts[i] += 1
                else:
                    self.lettercounts[i] = 1

    def count_bigrams(self):
        bigrams = {}
        for i in range(0, len(self.words)-1):
            bigram = self.words[i] + ' ' + self.words[i+1]
            if bigram in bigrams:
                bigrams[bigram] += 1
            else:
                bigrams[bigram] = 1
        self.bigrams_counts = bigrams
    
    def export_csv(self, data, filename):
        sorted_items = sorted(data.items(), key = lambda x: -x[1])
        with open(filename, 'w', newline = '') as f:
            writer = csv.writer(f)
            writer.writerow(['word', 'count'])
            for word, count in sorted_items:
                writer.writerow([word, count])


    def analyze(self):
        self.load_file()
        self.clean_text()
        self.split_words()
        self.word_counts = self.count_words(self.words)
        self.remove_stopwords()
        self.filtered_word_counts = self.count_words(self.filtered_words)
        self.total_words = len(self.words)
        self.total_filtered_words = len(self.filtered_words)
        self.count_letters()
        self.count_bigrams()

ta = TextAnalyzer("input.txt")
ta.analyze()
print("Total Words:", ta.total_words)
print("Total Words(Without stopwords):",  ta.total_filtered_words)
ta.export_csv(ta.word_counts, "words.csv")
ta.export_csv(ta.filtered_word_counts, "filtered_words.csv")
ta.export_csv(ta.bigrams_counts, "bigrams.csv")
ta.export_csv(ta.lettercounts, "letters.csv")
                
            
                

                    
        


  
        


    

