import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")
import mpld3
from lib.context import ContextHelper

class DataVisualizer:

    plt = plt
    fig = None
    ax = None
    number_of_subcharts = 1

    def __save_fig(self):
        plt.figure(figsize=(60, 48), dpi=80, layout='tight')
        filename = f"./charts/{datetime.now().strftime('%d%m%Y_%H%M%S')}.jpg"
        self.fig.savefig(filename,transparent=None, dpi='figure', format=None,
        metadata=None, bbox_inches=None, pad_inches=0.1,facecolor='auto', edgecolor='auto', backend=None)
        plt.close('all')
        print(f"Figure saved as {filename}")

    def __output_stdout(self):
        plt.show()
    
    def __output_mpld3(self):
        #mpld3.save_html(self.fig,"output.html")
        # mpld3.show()
        # mpld3.save_json(self.fig, "output.json")
        return mpld3.fig_to_html(self.fig)
        
        
    def __output(self):

        self.__output_stdout()

    def __plot_single_chart(self, context, rates_dataframe):

        self.ax.bar(self.xaxis_open_close_cdl, self.yaxis_open_close_cdl, self.width_open_close_cdl, bottom=self.bottom_open_close_cdl, color=self.bar_color)
        self.ax.bar(self.xaxis_high_low_cdl, self.yaxis_high_low_cdl, self.width_high_low_cdl, bottom=self.bottom_high_low_cdl, color=self.bar_color)
        self.ax.tick_params(axis='x')
        self.ax.xaxis.set_major_locator(plt.MaxNLocator(10))
        self.ax.grid(True, which='both', linestyle='--', linewidth=0.5, color=self.grid_color)
        self.ax.set_facecolor(self.background_color)
        self.ax.set_ylabel('PRICE')
        
        for opt in context.get("options_list"):
            if opt == "adr":
                self.ax.plot(rates_dataframe['date_str'], rates_dataframe["avg_daily_range"], label='ADR', color=self.adr_color, linewidth=self.adr_linewidth)
                self.ax.plot(rates_dataframe['date_str'], rates_dataframe["avg_daily_range_lower_band"], label='ADR', color=self.adr_color, linewidth=self.adr_linewidth)
            if opt == "atr":
                self.ax.step(rates_dataframe['date_str'], rates_dataframe['avg_true_range'], label='ATR (Simple)', color=self.atr_smp_color, linewidth=self.atr_smp_linewidth, where='mid')
            if opt == "guppy":
                self.ax.plot(rates_dataframe['date_str'], rates_dataframe['ema_f1'], color=self.guppy_fast_line_color, linewidth=self.guppy_fast_linewidth)
                self.ax.plot(rates_dataframe['date_str'], rates_dataframe['ema_f2'], color=self.guppy_fast_line_color, linewidth=self.guppy_fast_linewidth)
                self.ax.plot(rates_dataframe['date_str'], rates_dataframe['ema_f3'], color=self.guppy_fast_line_color, linewidth=self.guppy_fast_linewidth)
                self.ax.plot(rates_dataframe['date_str'], rates_dataframe['ema_f4'], color=self.guppy_fast_line_color, linewidth=self.guppy_fast_linewidth)
                self.ax.plot(rates_dataframe['date_str'], rates_dataframe['ema_f5'], color=self.guppy_fast_line_color, linewidth=self.guppy_fast_linewidth)
                self.ax.plot(rates_dataframe['date_str'], rates_dataframe['ema_f6'], color=self.guppy_fast_line_color, linewidth=self.guppy_fast_linewidth)
                self.ax.plot(rates_dataframe['date_str'], rates_dataframe['ema_s1'], color=self.guppy_slow_line_color, linewidth=self.guppy_slow_linewidth)
                self.ax.plot(rates_dataframe['date_str'], rates_dataframe['ema_s2'], color=self.guppy_slow_line_color, linewidth=self.guppy_slow_linewidth)
                self.ax.plot(rates_dataframe['date_str'], rates_dataframe['ema_s3'], color=self.guppy_slow_line_color, linewidth=self.guppy_slow_linewidth)
                self.ax.plot(rates_dataframe['date_str'], rates_dataframe['ema_s4'], color=self.guppy_slow_line_color, linewidth=self.guppy_slow_linewidth)
                self.ax.plot(rates_dataframe['date_str'], rates_dataframe['ema_s5'], color=self.guppy_slow_line_color, linewidth=self.guppy_slow_linewidth)
                self.ax.plot(rates_dataframe['date_str'], rates_dataframe['ema_s6'], color=self.guppy_slow_line_color, linewidth=self.guppy_slow_linewidth)
            if opt == "cbl":
                self.ax.step(rates_dataframe['date_str'], rates_dataframe['cbl'], label='CBL', color=self.cbl_color, linewidth=self.cbl_linewidth, where='mid')       

    def __plot_separate_charts(self, context, rates_dataframe, num_subcharts):

        main_chart_index = num_subcharts - 2
        sub_chart_index = num_subcharts - 1

        self.ax[main_chart_index].bar(self.xaxis_open_close_cdl, self.yaxis_open_close_cdl, self.width_open_close_cdl, bottom=self.bottom_open_close_cdl, color=self.bar_color)
        self.ax[main_chart_index].bar(self.xaxis_high_low_cdl, self.yaxis_high_low_cdl, self.width_high_low_cdl, bottom=self.bottom_high_low_cdl, color=self.bar_color)
        self.ax[main_chart_index].tick_params(axis='x')
        self.ax[main_chart_index].xaxis.set_major_locator(plt.MaxNLocator(10))
        self.ax[main_chart_index].grid(True, which='both', linestyle='--', linewidth=0.5, color=self.grid_color)
        self.ax[main_chart_index].set_facecolor(self.background_color)
        self.ax[main_chart_index].set_ylabel('PRICE')

        self.ax[sub_chart_index].tick_params(axis='x')
        self.ax[sub_chart_index].xaxis.set_major_locator(plt.MaxNLocator(10))
        self.ax[sub_chart_index].grid(True, which='both', linestyle='--', linewidth=0.5, color=self.grid_color)
        self.ax[sub_chart_index].set_facecolor(self.background_color)

        for opt in context.get("options_list"):
            if opt == "adr":
                self.ax[main_chart_index].plot(rates_dataframe['date_str'], rates_dataframe["avg_daily_range"], label='ADR', color=self.adr_color, linewidth=self.adr_linewidth)
                self.ax[main_chart_index].plot(rates_dataframe['date_str'], rates_dataframe["avg_daily_range_lower_band"], label='ADR', color=self.adr_color, linewidth=self.adr_linewidth)
            if opt == "atr":
                self.ax[main_chart_index].step(rates_dataframe['date_str'], rates_dataframe['avg_true_range'], label='ATR (Simple)', color=self.atr_smp_color, linewidth=self.atr_smp_linewidth, where='mid')
            if opt == "guppy":
                self.ax[main_chart_index].plot(rates_dataframe['date_str'], rates_dataframe['ema_f1'], color=self.guppy_fast_line_color, linewidth=self.guppy_fast_linewidth)
                self.ax[main_chart_index].plot(rates_dataframe['date_str'], rates_dataframe['ema_f2'], color=self.guppy_fast_line_color, linewidth=self.guppy_fast_linewidth)
                self.ax[main_chart_index].plot(rates_dataframe['date_str'], rates_dataframe['ema_f3'], color=self.guppy_fast_line_color, linewidth=self.guppy_fast_linewidth)
                self.ax[main_chart_index].plot(rates_dataframe['date_str'], rates_dataframe['ema_f4'], color=self.guppy_fast_line_color, linewidth=self.guppy_fast_linewidth)
                self.ax[main_chart_index].plot(rates_dataframe['date_str'], rates_dataframe['ema_f5'], color=self.guppy_fast_line_color, linewidth=self.guppy_fast_linewidth)
                self.ax[main_chart_index].plot(rates_dataframe['date_str'], rates_dataframe['ema_f6'], color=self.guppy_fast_line_color, linewidth=self.guppy_fast_linewidth)
                self.ax[main_chart_index].plot(rates_dataframe['date_str'], rates_dataframe['ema_s1'], color=self.guppy_slow_line_color, linewidth=self.guppy_slow_linewidth)
                self.ax[main_chart_index].plot(rates_dataframe['date_str'], rates_dataframe['ema_s2'], color=self.guppy_slow_line_color, linewidth=self.guppy_slow_linewidth)
                self.ax[main_chart_index].plot(rates_dataframe['date_str'], rates_dataframe['ema_s3'], color=self.guppy_slow_line_color, linewidth=self.guppy_slow_linewidth)
                self.ax[main_chart_index].plot(rates_dataframe['date_str'], rates_dataframe['ema_s4'], color=self.guppy_slow_line_color, linewidth=self.guppy_slow_linewidth)
                self.ax[main_chart_index].plot(rates_dataframe['date_str'], rates_dataframe['ema_s5'], color=self.guppy_slow_line_color, linewidth=self.guppy_slow_linewidth)
                self.ax[main_chart_index].plot(rates_dataframe['date_str'], rates_dataframe['ema_s6'], color=self.guppy_slow_line_color, linewidth=self.guppy_slow_linewidth)
            if opt == "cbl":
                self.ax[main_chart_index].step(rates_dataframe['date_str'], rates_dataframe['cbl'], label='CBL', color=self.cbl_color, linewidth=self.cbl_linewidth, where='mid')
            if opt == "macd": 
                self.ax[sub_chart_index].bar(rates_dataframe['date_str'], rates_dataframe['macd_diff'], color=np.where(rates_dataframe['macd_diff'] >= 0, self.macd_up_color, self.macd_down_color), width=self.macd_width)
                self.ax[sub_chart_index].axhline(0, color='black', linewidth=0.5, linestyle='--')
                self.ax[sub_chart_index].set_ylabel('MACD')
                self.ax[sub_chart_index].legend(loc='upper left')      

    def __set_common_styles(self, context):
        
        c_helper = ContextHelper()
        
        plt.style.use(c_helper.get_context_specific_data(context, "chart", "chart", "style.style_sheet"))
        plt.style.use({ 'font.size' : str(c_helper.get_context_specific_data(context, "chart", "chart", "style.font_size"))})
        plt.style.use({ 'font.family' : c_helper.get_context_specific_data(context, "chart", "chart", "style.font_family")})
        plt.style.use({ 'font.weight' : c_helper.get_context_specific_data(context, "chart", "chart", "style.font_weight")})
        plt.rcParams['text.color'] = c_helper.get_context_specific_data(context, "chart", "chart", "style.font_color")
        plt.rcParams['axes.labelcolor'] = c_helper.get_context_specific_data(context, "chart", "chart", "style.font_color")
        plt.rcParams['xtick.color'] = c_helper.get_context_specific_data(context, "chart", "chart", "style.font_color")         
        plt.rcParams['ytick.color'] = c_helper.get_context_specific_data(context, "chart", "chart", "style.font_color")

        self.candles_up_color = c_helper.get_context_specific_data(context, "chart", "chart", "style.candles_up_color")
        self.candles_down_color = c_helper.get_context_specific_data(context, "chart", "chart", "style.candles_down_color")
        self.background_color = c_helper.get_context_specific_data(context, "chart", "chart", "style.background_color")
        self.grid_color = c_helper.get_context_specific_data(context, "chart", "chart", "style.grid_color")


    def __set_specific_styles(self, context):
        
        c_helper = ContextHelper()
        
        for opt in context.get("options_list"):
            if opt == "adr":
                self.adr_color = c_helper.get_context_specific_data(context,"adr", "indicator", "style.color")
                self.adr_linewidth = c_helper.get_context_specific_data(context,"adr", "indicator", "style.linewidth")
            if opt == "atr":
                self.atr_smp_color = c_helper.get_context_specific_data(context,"atr_smp", "indicator", "style.color")
                self.atr_smp_linewidth = c_helper.get_context_specific_data(context,"atr_smp", "indicator", "style.linewidth")
                self.atr_exp_color = c_helper.get_context_specific_data(context,"atr_exp", "indicator", "style.color")
                self.atr_exp_linewidth = c_helper.get_context_specific_data(context,"atr_exp", "indicator", "style.linewidth")
            if opt == "guppy":
                self.guppy_fast_line_color = c_helper.get_context_specific_data(context,"guppy", "indicator", "style.fast_line_color")
                self.guppy_fast_linewidth = c_helper.get_context_specific_data(context,"guppy", "indicator", "style.fast_linewidth")
                self.guppy_slow_line_color = c_helper.get_context_specific_data(context,"guppy", "indicator", "style.slow_line_color")
                self.guppy_slow_linewidth = c_helper.get_context_specific_data(context,"guppy", "indicator", "style.slow_linewidth")
            if opt == "cbl":
                self.cbl_color = c_helper.get_context_specific_data(context,"cbl", "indicator", "style.color")
                self.cbl_linewidth = c_helper.get_context_specific_data(context,"cbl", "indicator", "style.linewidth")
            if opt == "macd":
                self.macd_up_color = c_helper.get_context_specific_data(context,"macd", "indicator", "style.up_color")
                self.macd_down_color = c_helper.get_context_specific_data(context,"macd", "indicator", "style.down_color")
                self.macd_width = c_helper.get_context_specific_data(context,"macd", "indicator", "style.width")
                self.number_of_subcharts = 2

    def __set_styles_based_on_dataframe_data(self, rates_dataframe): 
        # Convert the date column to a string format
        rates_dataframe['date_str'] = pd.to_datetime(rates_dataframe.index, utc=True)
        rates_dataframe['date_str'] = rates_dataframe['date_str'].dt.strftime('%Y-%m-%d %H:%M:%S').astype(str)

        # setting the High and Low candles
        self.xaxis_high_low_cdl = rates_dataframe['date_str']
        self.yaxis_high_low_cdl = rates_dataframe['high'] - rates_dataframe['low']
        self.width_high_low_cdl = 0.05  # the width of the bars: can also be len(x) sequence
        self.bottom_high_low_cdl = rates_dataframe['low']
        
        # setting the Open and Close candles
        self.xaxis_open_close_cdl = rates_dataframe['date_str']
        self.yaxis_open_close_cdl = rates_dataframe['close'] - rates_dataframe['open']
        self.width_open_close_cdl = 0.3  # the width of the bars: can also be len(x) sequence
        self.bottom_open_close_cdl = rates_dataframe['open']
    
        self.bar_color = np.where(rates_dataframe['close'] > rates_dataframe['open'], self.candles_up_color, self.candles_down_color)

    def execute(self, context, rates_dataframe, **kwargs):
                
        self.__set_common_styles(context)
        self.__set_specific_styles(context)
        self.__set_styles_based_on_dataframe_data(rates_dataframe)
        
        self.fig, self.ax = plt.subplots(self.number_of_subcharts,1, sharex="row", figsize=(16, 9), dpi=80, layout='tight', gridspec_kw={'height_ratios': [3, 1] if self.number_of_subcharts == 2 else [1]})
        
        if self.number_of_subcharts == 1:
            self.__plot_single_chart(context, rates_dataframe) 
        else:
            self.__plot_separate_charts(context, rates_dataframe, self.number_of_subcharts)
            

        print("Plotting chart...")
        plt.legend(loc='upper left')
        fig_manager = plt.get_current_fig_manager()
        fig_manager.resize(1600, 900)

        if context.get("is_backend_request"):
            return self.__output_mpld3()
        else:
            self.__output_stdout()


