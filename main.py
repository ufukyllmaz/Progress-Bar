from progress_bar import ProgressBar
import time

if __name__ == '__main__':
  process_size = 126
  for i in range(process_size + 1):
    """
    Runs for each step
    """
    progress_bar_display = ProgressBar(i, process_size).execute()
    print(progress_bar_display, end='', flush=True)
    time.sleep(0.2)
    print('\b' * len(progress_bar_display), end='', flush=True)
