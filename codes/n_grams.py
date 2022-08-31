import nltk
from nltk.corpus import stopwords



def generate_N_grams(text, ngram=1):
    nltk.download('stopwords', download_dir="../data/nltk_data/")
    nltk.data.path = ["../data/nltk_data/"]
    words = [word for word in text.split(" ") if word not in set(stopwords.words('english'))]
    temp = zip(*[words[i:] for i in range(ngram)])
    ans = [' '.join(ngram) for ngram in temp]
    return ans

# def check_ngrams(l, ngram):
#     # print(l, ngram)
#     # print(l[0].split(" "))
#     return all([True if len(d.split(" ")) == ngram else False for d in l])

if __name__ == "__main__":
    text = "This is a nice way of doing things"
    
    for i in range(1,4):
        p = generate_N_grams(text, i)
        file_name = f"data/ngram/{i}.txt"
        with open(file_name, "w") as d:
            d.write("\n".join(p))
    

    