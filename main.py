import pandas as pd
df = pd .read _csv('train.csv)
df . head()

from pandas profilling import profileReport
prof = profileReport(df)
prof.to_file(output_file = 'output.html')
