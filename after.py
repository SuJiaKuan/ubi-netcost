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
ax.text(5, 1.7, 'poverty line', fontsize=8, color='r', ha='center')

# Draw "breakeven point"
ax.axvline(x=6, color='k', linestyle='dashed')
ax.text(6, 10.2, 'Breakeven point\n(\$0 NIT - \$0 in national income taxes)', fontsize=9, style='italic', ha='center')
ax.text(4, 9.5, '$700 billion net income gain', fontsize=9, ha='center')
ax.text(8, 9.5, '$700 billion net income loss', fontsize=9, ha='center')

# Draw "after ubi line"
ax.plot((0, 10), (2, 6), 'b-')

# Draw "before ubi line"
ax.plot((0, 10), (0, 7.333), 'k-')

# Save the plot
plt.savefig('after.jpg')

# Uncomment following line for debug
# plt.show()
