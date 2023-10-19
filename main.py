from progress_bar import ProgressBar

if __name__ == '__main__':
  process_size = 126
  for i in range(process_size + 1):
    ProgressBar(i, process_size).execute()


