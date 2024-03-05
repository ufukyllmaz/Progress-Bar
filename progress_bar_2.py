import random
import time

bar = chr(9608)

def main():
    bar_proccessed = 0
    total_proccess = 1024
    while bar_proccessed < total_proccess:
        bar_proccessed += random.randint(0, 100)
        get_bar = get_progress_bar(bar_proccessed, total_proccess)
        print(get_bar, end='', flush=True)
        time.sleep(0.2)
        print('\b' * len(get_bar), end='', flush=True)
    
def get_progress_bar(progress, total, bar_width=40):
    progress_bar = ''
    progress_bar += '['
    
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0
    
    number_of_bars = int((progress / total) * bar_width)
    
    progress_bar += bar * number_of_bars
    progress_bar += ' '
    progress_bar += ']'
    
    percnt = round(progress / total * 100, 1)
    progress_bar += ' ' + str(percnt) + '%'
    progress_bar += ' ' + str(progress) + '/' + str(total)
    
    return progress_bar

if __name__ == '__main__':
    main()