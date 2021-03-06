from collections import defaultdict

def group_by_owners(files):
    d = defaultdict(list)
    for k, v in files.items():
        d[v].append(k)
    return d

if __name__ == "__main__":    
    books = {
        'Smile': 'Amy',
        'Resistance': 'Jamie',
        'Guts': 'Amy'
    }   
    print(group_by_owners(books))