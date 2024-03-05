class ProgressBar:
  """
  This class return the progress bar.
  """
  def __init__(self, progress_bar_count, process_bar_size):
    self.progress_bar_count = progress_bar_count
    self.progress_bar = process_bar_size
    self.progress_bar_display = ''

  def progress_bar_method(self):
    self.progress_bar_perc = (self.progress_bar_count / self.progress_bar) * 100
    if self.progress_bar_perc != 100:
      self.progress_bar_display = "Processing : ["
      self.progress_bar_display += int(50 * self.progress_bar_perc/100) * "|"
      self.progress_bar_display += (50 - int(50*self.progress_bar_perc/100)) * ' '
      self.progress_bar_display += "] " + '%'
      self.progress_bar_display += str(int(self.progress_bar_perc))
      return self.progress_bar_display

    else:
      self.progress_bar_display = "Done       : ["
      self.progress_bar_display += int(50 * self.progress_bar_perc/100) * "|"
      self.progress_bar_display += (50 - int(50*self.progress_bar_perc/100)) * ' '
      self.progress_bar_display += "] " + '%'
      self.progress_bar_display += str(int(self.progress_bar_perc))
      return self.progress_bar_display

  def execute(self):
    return self.progress_bar_method()

