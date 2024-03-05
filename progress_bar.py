
class ProgressBar:
  """
  This class print screen the progress bar.
  """
  def __init__(self, progress_bar_count, process_bar_size):
    self.progress_bar_count = progress_bar_count
    self.progress_bar = process_bar_size

  def progress_bar_method(self):
    self.progress_bar_perc = (self.progress_bar_count / self.progress_bar) * 100
    print("Processing : [" + int(50 * self.progress_bar_perc/100) * "|" + (50 - int(50*self.progress_bar_perc/100)) * ' ' +"] " + '%' + str(int(self.progress_bar_perc)))

  def execute(self):
    self.progress_bar_method()

