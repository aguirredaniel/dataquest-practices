import pandas as pd
import matplotlib.pyplot as plt


# - Add the title The Death Toll Worldwide Is 1.5M+. The title should have the following properties:
#   - The x-coordinate is -80000
#   - The y-coordinate is 23.5
#  -  It is in bold text
#   - It has a font size of 17
# - Add the subtitle Top 20 countries by death toll (December 2020). The subtitle should have the following properties:
#   - The x-coordinate is -80000
#  -  The y-coordinate is 22.5
#   - It has a font size of 12
def main():
    top20_deathtoll = pd.read_csv('../top20_deathtoll.csv')
    figure, axes = plt.subplots(figsize=(4.5, 6))
    axes.barh(top20_deathtoll['Country_Other'], top20_deathtoll['Total_Deaths'],
              height=0.45, color='#af0b1e')

    for spin in ['left', 'bottom', 'right', 'top']:
        axes.spines[spin].set_visible(False)

    axes.set_xticks([0, 150000, 300000])

    axes.xaxis.tick_top()
    axes.tick_params(axis='x', colors='grey')
    axes.tick_params(top=False, left=False)

    axes.text(x=-80000, y=23.5, s='The Death Toll Worldwide Is 1.5M+', size=17, weight='bold')
    axes.text(x=-80000, y=22.5, s='Top 20 countries by death toll (December 2020)', size=12)
    
    plt.show()


if __name__ == '__main__':
    main()
