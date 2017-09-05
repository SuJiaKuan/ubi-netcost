import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# Labels
ax.set_xlabel('Population of Taiwan citizens from lowest to highest annual income percentiles')
ax.set_ylabel('Annual income (NT$)')

# Set ticks and tick labels
ax.ticklabel_format(useOffset=False)
ax.set_yticklabels(['$0', '$120k'])
ax.set_xticklabels([])
ax.tick_params(axis="both", which="both", bottom="off", top="off",
    labelbottom="on", left="off", right="off", labelleft="on")

# Hide top spines
ax.spines['top'].set_visible(False)

# Set range of axis
ax.axis([0, 10, 0, 10])

# Draw "poverty line"
ax.plot((0, 10), (2, 2), 'r--')
ax.fill_between(x=(0, 10), y1=(0, 0), y2=(2, 2), color='#37efe9')
ax.text(5, 1.7, 'poverty line', fontsize=8, color='r', ha='center')
ax.text(3, 0.8, '$1.7 trillion in UBI for bottom 56%', fontsize=9, ha='center')
ax.text(8, 0.8, '$1.4 trillion in UBI for top 54%', fontsize=9, ha='center')

# Draw "breakeven point"
ax.axvline(x=6, color='k', linestyle='dashed')
ax.text(6, 10.2, 'Breakeven point\n(\$120k UBI - \$120k in new taxes)', fontsize=9, style='italic', ha='center')
ax.text(4, 9.5, '$700 billion net income gain', fontsize=9, ha='center')
ax.text(8, 9.5, '$700 billion net income loss', fontsize=9, ha='center')

# Draw "after ubi line"
ax.plot((0, 10), (2, 6), 'b-')
ax.text(6, 3.2, 'Total income earned above $120k UBI after taxes', fontsize=9, color='b', ha='center', rotation=5)

# Draw "before ubi line"
ax.plot((0, 10), (2, 9.333), 'k-')
ax.text(4.2, 4.7, '$700 billion in taxes', fontsize=9, ha='center', rotation=20)
ax.text(8, 6.5, '$2.4 trillion in taxes', fontsize=9, ha='center', rotation=20)

# Save the plot
plt.savefig('before.jpg')

# Uncomment following line for debug
# plt.show()
