import pandas as pd
import numpy as np
import seaborn as sb
import datetime
import os
import sys
import logging
from logging import StreamHandler, Formatter
from matplotlib import pyplot as plt

class Plots():
    """Graphs for model"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        handler = StreamHandler(stream=sys.stdout)
        handler.setLevel(logging.INFO)
        handler.setFormatter(Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
        if self.logger.hasHandlers()==False:
            self.logger.addHandler(handler)

        self.logger.info('Logging started') 
    
    @staticmethod
    def generate_path(plot_type):
        """Generate filenames and create path to save plots"""
        suffix = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        mypath = os.path.join(
                os.path.abspath('plots'), plot_type + suffix + '.png')
        return mypath
    
    def draw_plots(self, filename):
        """
        Draw pairplots for dependence of max, mean and min from other columns
        and plot to compare max and min values
        """
        result_path = {}
        
        # read json-file
        try:
            self.logger.info('Reading file...')
            df = pd.read_json(filename)
        except FileNotFoundError:
            self.logger.error('File not found!')
            return None
        except  Exception:
            self.logger.error('Reading file error!')
            return None
        
        # plot pairplots for dependence of max, mean and min from other columns
        self.logger.info('Plotting pairplots...')
        cols = ['rb_corners', 'mean', 'max', 'min', 'floor_mean', 'floor_max', 'floor_min', 'ceiling_mean', 'ceiling_max', 'ceiling_min']
        pp = sb.pairplot(
            df[cols],
            x_vars=['floor_mean', 'floor_max', 'floor_min', 'ceiling_mean', 'ceiling_max', 'ceiling_min'],
            y_vars=['mean', 'max', 'min'],
            hue='rb_corners',
            palette={4: 'blue', 6: 'red', 8: 'green', 10: 'black'},
            height=2
        )
        fig = pp.fig
        pair_path = self.generate_path('pairplot')
        fig.savefig(pair_path)
        result_path['pairplot'] = pair_path
        plt.show()
        
        # plot lineplot to compare max and min values
        self.logger.info('Plotting plot for min and max values...')
        t = np.array(df.index)
        y1 = np.array(df['max'])
        y2 = np.array(df['min'])
        plt.plot(t, y1, label='max')
        plt.plot(t, y2, label='min')
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2)
        plt.title('Min and max values')
        min_max_path = self.generate_path('minmaxplot')
        result_path['min-max-plot'] = min_max_path
        plt.savefig(min_max_path)
        plt.show()
        
        return result_path