import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os


fonts_directory = './common/fonts/'

custom_fonts = {}

for filename in os.listdir(fonts_directory):
    if filename.endswith('.ttf'):
        file_path = os.path.join(fonts_directory, filename)
        
        print(f'Found TTF file: {file_path}')
        font_name = os.path.splitext(filename)[0]
        font_properties = FontProperties(fname=file_path)
        custom_fonts[font_name] = font_properties

plt.rcParams['font.family'] = font_properties.get_name()