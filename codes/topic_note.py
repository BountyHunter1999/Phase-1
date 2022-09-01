#!/bin/python3

import csv
from sre_parse import State
from codes.n_grams import generate_N_grams

NOTES_LOCATION = "data/3_govt_urls_state_only.csv"
STATES_LOCATION = "data/states.txt"

BI_SAVE_LOCATION = "data/bi_grams_note.txt"
TRI_SAVE_LOCATION = "data/tri_grams_note.txt"

TOPIC_NOTE_LOCATION = "data/topic_note.csv"

def get_notes(location):
    """
    Gets a location of the csv of data and return list notes
    Args:
        location (str): location of where the csv is located

    Returns:
        notes : list of notes
    """
    notes = []
    with open(location) as f:
        next(f)
        r = csv.reader(f)
        for i in r:

            notes.append(i[5])
            # break
    
    return notes

def get_states(location):
    """
    Gets a location of the text file containing states and return list states
    Args:
        location (str): location of where the text file is located

    Returns:
        states : list of states
    """
    with open(location) as f:
        states = [s.strip() for s in f.readlines()]
    return states

def get_1_2_3_gram(notes):
    """
    args:
        notes(list): list of notes
    returns:
        tri_gram(list): list of 3-grams
        bi_gram(list): list of 2-grams
        o_gram(list): list of 1-grams
    """
    tri_gram = []
    bi_gram = []
    o_gram = []
    for i in notes:
        j = i.split("--")[0].strip()
        # j = "".join([j.replace(s, "") for s in states if s in j]).strip()
        tri_gram += generate_N_grams(j, 3)
        bi_gram += generate_N_grams(j, 2)
        o_gram += generate_N_grams(j, 1)
    
    return tri_gram, bi_gram, o_gram

def get_tri_bi_gram(notes, states, with_state = False):
    """
    args:
        notes(list): list of notes
        states(list): list of states
    returns:
        tri_gram(list): list of 3-grams
        bi_gram(list): list of 2-grams
    """
    tri_gram = []
    bi_gram = []
    for i in notes:
        j = i.split("--")[0].strip()
        
        if not with_state:
            j = "".join([j.replace(s, "") for s in states if s in j]).strip()
        
        tri_gram += generate_N_grams(j, 3)
        bi_gram += generate_N_grams(j, 2)
    
    return tri_gram, bi_gram

def get_count_of_ngrams(tri_gram, bi_gram):
    """
    Get a list of tri_gram and bi_gram and 
    return the actual count of occurence of each in descending order
    Args:
        tri_gram (list): list of 3-grams
        bi_gram (list): list of 2-grams
    returns:
        t (dict): key-> 3-grams, values-> occurence
        b (dict): key-> 2-grams, values-> occurence
    """
    tri_count = {}
    for i in tri_gram:
        tri_count[i] = tri_count.get(i, 0)  + 1
        
    bi_count = {}
    for i in bi_gram:
        bi_count[i] = bi_count.get(i, 0)  + 1
    
    t = sorted(tri_count.items(), key=lambda k:k[1], reverse=True)
    b = sorted(bi_count.items(), key=lambda k:k[1], reverse=True)
    
    return t, b

def save_grams(t, b, t_save, b_save):
    """
    Takes sorted tri-grams and bi-grams and 
    save 20 of them to a text file
    Args:
        t (dict): reverse sorted tri_gram 
        b (dict): reverse sorted bi_gram 
        t_save (str): location to save 3-grams
        d_save (str): location to save 2-grams
    """
    with open(t_save, "w") as f:
        for i in t[:21]:
            f.write(str(i) + "\n")
            
    with open(b_save, "w") as f:
        for i in b[:21]:
            f.write(str(i)+ "\n")
    
def get_grams(t_save, b_save):
    """
    Takes location of the sorted tri-grams and bi-grams and 
    return them
    Args:

        t_save (str): location to save 3-grams
        d_save (str): location to save 2-grams
    Returns:
        t (list): reverse sorted tri_gram 
        b (list): reverse sorted bi_gram 
    """
    
    with open(t_save) as f:
        t = [i.strip().split(",")[0].strip("('") for i in f.readlines()]
    
    with open(b_save) as f:
        b = [i.strip().split(",")[0].strip("('") for i in f.readlines()]

    return t, b

def get_topic_notes(notes, t, b):
    """
    Gets notes and 3-grams and 2-grams to give a dictionary 
    of notes and topic
    
    topic matching n-grams present in the notes
    Args:
        notes (list): notes obtained from the csv file
        t (list): 20 3-grams
        b (list): 20 2-grams

    Returns:
        d (dict): key(notes) values(topic)
    """
    d= {}
    for x, i in enumerate(notes):
        for a, bi in zip(t,b):
            if i not in list(d.keys()):
                if a in i:
                    d[i] = a
                if bi in i:
                    d[i] = bi
    
    return d

def get_notes_states_topic(d, states):
    """

    Args:
        d (dict): dictionary containing {notes: topic}
        states (list): list of states 

    Returns:
        d (dict): dictionary containing {notes: [state, topic]}
    """
    for k, v in d.items():
        # j = k.split("--")[0].strip()
        j = k
        t_g = generate_N_grams(j, 3)
        in_t = " ".join(set([t for t in t_g if t in states]))
        if in_t:
            d[k] = [in_t, v]
            continue
        b_g = generate_N_grams(j, 2)
        in_b = " ".join(set([t for t in b_g if t in states]))
        if in_b:
            d[k] = [in_b, v]
            continue
        o_g = generate_N_grams(j, 1)
        in_o = " ".join(set([t for t in o_g if t in states]))
        if in_o:
            d[k] = [in_o, v]
        continue
    
    return d


def save_topic_note(d, t_n_save):
    """
    saves the topic, notes obtained from d into the csv file
    Args:
        d (dict): key(notes) values(topic)
        t_n_save (str): save location for the csv file
    """
    with open(t_n_save, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Note"])
        for key, value in d.items():
            writer.writerow([value, key])


def save_topic_state_note(d, t_n_save):
    """
    saves the topic, notes obtained from d into the csv file
    Args:
        d (dict): key(notes) values(topic)
        t_n_save (str): save location for the csv file
    """
    with open(t_n_save, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "State", "Note"])
        for key, value in d.items():
            writer.writerow([value[1], value[0], key]) 

if __name__ == "__main__":
    notes = get_notes(NOTES_LOCATION)
    states = get_states(STATES_LOCATION)
    
    tri_gram, bi_gram = get_tri_bi_gram(notes, states)
    t, b = get_count_of_ngrams(tri_gram, bi_gram)
    
    save_grams(t, b, TRI_SAVE_LOCATION, BI_SAVE_LOCATION)
    
    t20, b20 = get_grams(TRI_SAVE_LOCATION, BI_SAVE_LOCATION)
    
    d = get_topic_notes(notes, t20, b20)
    
    # save_topic_note(d, TOPIC_NOTE_LOCATION)
    d = get_notes_states_topic(d, states)
    save_topic_state_note(d, TOPIC_NOTE_LOCATION)
    
    
    
    